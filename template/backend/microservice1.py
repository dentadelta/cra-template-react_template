from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/helloworld")
async def helloworld():
    return_data = {
        'data1': 'Hello World',
        'data2': 'Love is the answer',
        'data3': [1, 2, 3, 4, 5],
        'data4': {'a': 1, 'b': 2, 'c': 3}
        }
    return return_data