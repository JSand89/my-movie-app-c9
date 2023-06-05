from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder


from service.genres import GenresService
from schemas.genres import Genres 
from config.database import Session



genres_router = APIRouter()

@genres_router.get('/genres_hello', tags=['genres'], status_code=200)
def get_genres_hello():
    """function to check the route"""
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')


@genres_router.get('/genres', tags = ['genres'], status_code=200)
def get_genres():
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)


@genres_router.get('/genres_for_id', tags=['genres'], status_code=200)
def get_genres_for_id(id:int):
    db = Session()
    result = GenresService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)

@genres_router.post('/genres', tags=['genres'], status_code=201)
def create_genres(genres:Genres):
    db = Session()
    GenresService(db).create_genre(genres)
    return JSONResponse(content={"message":"genre created successfully",'status_code':201}, status_code=201)


@genres_router.put('/genres{id}',tags=['genres'])
def update_genre(id:int,data:Genres):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"genre don't found", "status_code":404})
    GenresService(db).update_genre(data)
    return JSONResponse(content={"message":"genre update successfully",'status_code':200}, status_code=200)

@genres_router.delete('/genres{id}', tags=['genres'])
def delete_genre(id:int):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"genre don't found", "status_code":404})
    GenresService(db).delete_genre(id)
    return JSONResponse(content={"message":"genre delete successfully",'status_code':200}, status_code=200)



