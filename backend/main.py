import uvicorn
from fastapi import FastAPI

from api.v1 import v1
from common.db import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(v1, prefix="/api/v1")


if __name__ == '__main__':
    uvicorn.run('main:app', host="0", port=8000, reload=True, debug=True, workers=1)
