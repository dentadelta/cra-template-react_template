from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import os
import numpy as np

class SummariseRequest(BaseModel):
    x_axis: str
    y_axis: str
    csv_file: str
    group_by: str
    filter_by: str
    order_by: str
    limit: int

router = APIRouter()

@router.post("/data")
async def summarise_data(request: SummariseRequest):
    x_axis = request.x_axis
    y_axis = request.y_axis
    csv_file = request.csv_file
    filter_by = request.filter_by
    filter_by = filter_by.split('=')
    filter_by = [i.strip() for i in filter_by]
    filter_column = filter_by[0]
    filter_value = filter_by[1]
    current_dir = os.path.dirname(os.path.realpath(__file__))
    csv_file = os.path.join(current_dir, csv_file)
    df = pd.read_csv(csv_file)
    df = df.loc[df[filter_column] == filter_value]
    df = df.groupby(request.group_by)[request.y_axis].sum().reset_index()

    try:
        
        df = df.sort_values(request.order_by, ascending=False)
        df = df.head(request.limit)
        df = df.rename(columns={request.y_axis: 'value', request.group_by: 'name'})
        df = df.to_dict('records')
        random_rgb = np.random.randint(0, 255, size=(len(df), 3)).tolist()
        backgroundColor = ['rgba({}, {}, {}, 1)'.format(*i) for i in random_rgb]
        borderColor = ['rgba({}, {}, {}, 1)'.format(*i) for i in random_rgb]
        df = [{'name': i['name'], 'value': i['value'], 'backgroundColour': backgroundColor[index], 'borderColor': borderColor[index]} for index, i in enumerate(df)]
        df = pd.DataFrame(df)
        return df.to_dict('records')
    except Exception as e:
        print ({'error', str(e)})
        return e

