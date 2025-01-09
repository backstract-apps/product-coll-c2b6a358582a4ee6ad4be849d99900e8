from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Product(BaseModel):
    id: int
    username: str
    password: str


class ReadProduct(BaseModel):
    id: int
    username: str
    password: str
    class Config:
        from_attributes = True




class PostProduct(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        from_attributes = True



class PutProductId(BaseModel):
    id: str
    username: str
    password: str

    class Config:
        from_attributes = True

