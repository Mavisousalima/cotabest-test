from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    minimun: int
    amount_per_package: int
    max_availability: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Ração para cachorro",
                "price": 50.0,
                "minimun": 10,
                "amount_per_package": 2,
                "max_availability": 50000
            }
        }
        
class ProductName(BaseModel):
    name: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Ração para cachorro",
            }
        }
        
class ProductID(BaseModel):
    id: int
    amount: int