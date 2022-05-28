from fastapi import APIRouter

app = APIRouter(tags=["认证相关"])


@app.post("/user", summary="新增用户")
def user_create():
    pass


@app.post("/login", summary="登录")
def user_login():
    pass


@app.put("/logout", summary="退出")
def user_logout():
    pass
