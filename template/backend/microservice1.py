from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

class Input(BaseModel):
    input1: Optional[str]
    input2: Optional[str]


router = APIRouter()

@router.get("/Appjs")
async def helloworld():
    return_data = {
        'header': 'Heavy Vehicle',
        'page_description': 'This application allows you to extract data from the heavy vehicle database',
        'page_detail1':'This app contains the following functionality:',
        'page_detail2':'This app contains the following roads',
    }

    return_array_data = {
            'page_bullet_point': ['Eat', 'Sleep', 'Code', 'Repeat']
    }

    return_dict_data = {
         'page_dict': {'road1': 'Road 1 description',
                       'road2': 'Road 2 description',
                       'road 3': 'Road 3 description'},
                       
         'url': {'logoUrl': 'logo192.png'}
        }
       
    return {'data': return_data, 'dataarray': return_array_data, 'datadict': return_dict_data}

@router.post("/Appjs/Button")
async def processButton(input: Input):
    input = input.input1
    if input.find('+') != -1:
        input = input.split('+')
        input = [int(i) for i in input]
        input = sum(input)

        return input
    else:
        return "Invalid input, addition command only"
