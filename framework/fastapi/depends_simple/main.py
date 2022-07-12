from typing import Union

from fastapi import Depends, FastAPI

app = FastAPI()


def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}

# デフォルトの実行結果を出力
@app.get("/items/")
def read_items(commons: dict = common_parameters()):
    return commons


# パラメーターを受け取って出力
@app.get("/users/")
def read_users(commons: dict = Depends(common_parameters)):
    return commons