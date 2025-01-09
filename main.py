from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - product-coll-c2b6a358582a4ee6ad4be849d99900e8',debug=False,docs_url='/dazzling-kirch-8b69eb86cdc511ef81f80242ac12000331/docs',openapi_url='/dazzling-kirch-8b69eb86cdc511ef81f80242ac12000331/openapi.json')

app.include_router(router, prefix='/dazzling-kirch-8b69eb86cdc511ef81f80242ac12000331/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()