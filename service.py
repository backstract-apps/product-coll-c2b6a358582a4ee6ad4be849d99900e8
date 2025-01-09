from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_product(db: Session):

    product_all = db.query(models.Product).order_by(models.Product.id).all()
    res = {
        'product_all': product_all,
    }
    return res

async def get_product_id(db: Session, id: int):

    product_one = db.query(models.Product).filter(models.Product.id == 'id').first()
    res = {
        'product_one': product_one,
    }
    return res

async def post_product(db: Session, raw_data: schemas.PostProduct):
    id:int = raw_data.id
    username:str = raw_data.username
    password:str = raw_data.password


    record_to_be_added = {'id': id, 'username': username, 'password': password}
    new_product = models.Product(**record_to_be_added)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    product_inserted_record = new_product
    res = {
        'product_inserted_record': product_inserted_record,
    }
    return res

async def put_product_id(db: Session, raw_data: schemas.PutProductId):
    id:str = raw_data.id
    username:str = raw_data.username
    password:str = raw_data.password


    product_edited_record = db.query(models.Product).filter(models.Product.id == id).first()
    for key, value in {'id': id, 'username': username, 'password': password}.items():
          setattr(product_edited_record, key, value)
    db.commit()
    db.refresh(product_edited_record)
    product_edited_record = product_edited_record

    res = {
        'product_edited_record': product_edited_record,
    }
    return res

async def delete_product_id(db: Session, id: int):

    product_deleted = None
    record_to_delete = db.query(models.Product).filter(models.Product.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        product_deleted = record_to_delete
    res = {
        'product_deleted': product_deleted,
    }
    return res

