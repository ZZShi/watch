from fastapi import APIRouter

app = APIRouter(tags=["用户相关"])


@app.get("/users", summary="用户列表")
def user_list():
    pass


@app.post("/users", summary="新增用户")
def user_create():
    pass


@app.put("/users/{pk}", summary="修改用户")
def user_update(pk: int):
    pass


@app.put("/users/{pk}", summary="删除用户")
def user_delete(pk: int):
    pass
