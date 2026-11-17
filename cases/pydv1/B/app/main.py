from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Customer(BaseModel):
    id: int
    name: str
    email: str


CUSTOMERS = {1: Customer(id=1, name="Ada", email="ada@example.com")}


@app.get("/customers/{customer_id}", response_model=Customer)
def get_customer(customer_id: int) -> Customer:
    return CUSTOMERS[customer_id]
