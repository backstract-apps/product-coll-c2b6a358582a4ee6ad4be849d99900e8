from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/product/')
async def get_product(db: Session = Depends(get_db)):
    try:
        return await service.get_product(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/product/id')
async def get_product_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_product_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/product/')
async def post_product(raw_data: schemas.PostProduct, db: Session = Depends(get_db)):
    try:
        return await service.post_product(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/product/id/')
async def put_product_id(raw_data: schemas.PutProductId, db: Session = Depends(get_db)):
    try:
        return await service.put_product_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/product/id')
async def delete_product_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_product_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

