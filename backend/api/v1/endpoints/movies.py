from fastapi import APIRouter

app = APIRouter(tags=["电影相关"])


@app.get("/movies", summary="电影列表")
def movie_list():
    pass


@app.post("/movies", summary="新增电影")
def movie_create():
    pass


@app.put("/movies/{pk}", summary="修改电影")
def movie_update(pk: int):
    pass


@app.put("/movies/{pk}", summary="删除电影")
def movie_delete(pk: int):
    pass
