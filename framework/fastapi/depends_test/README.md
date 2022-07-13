# Depends 検証用

![無題の図形描画](https://user-images.githubusercontent.com/61643054/178749185-855e1426-5bdd-4058-b8a6-5fa9b166c6c1.png)

## Dependency Injectionの説明

https://qiita.com/hshimo/items/1136087e1c6e5c5b0d9f

https://fastapi.tiangolo.com/tutorial/dependencies/


## pros, cons

- pros
    - PytestでDependsで指定した値をOverrideできる
    - リクエストのたびにDependsの中に指定した関数を実行できる
    - 同じ処理を何度も記載しなくて良い   

- cons
    - 特になし

## 検証結果

- CRUD処理内で「db: Session = Depends(get_db)」を使用
    - ルーティングしているところ以外でDependsを行なってもただのDependsという変数になった。
```python
def create_new_job(job: JobCreate, owner_id: int, db: Session = Depends(get_db)):
```    


- CRUD処理内でSessionを定義する。
    - 可能そうだけど、　SessionをそれぞれのCRUDファイルで定義する必要がある。
    - 毎回Close処理が必要
    - PytestでもそれぞれのCRUD処理に対するSessionのOverrideが必要
```python
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db_session = SessionLocal()
def create_new_job(job: JobCreate, owner_id: int):
    db = db_session
    # print('test:', db)
    # print('test:', type(db))
    job = Job(**job.dict(), owner_id=owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    db.close()
    return job
```

- SessionってCRUDの中だけで使うからCRUD処理内だけで使ったら良いのでは？
    - PytestのOverrideができない
    - 処理を1箇所で管理する記載はこのやり方の方が良い
    - sessionをpytestで置き換えたりする場合はこのやり方が1箇所で管理できてベストな気がする、

## 動作コマンド
処理起動
```
uvicorn main:app --reload
```

Test
```
pytest
```

