from sqlmodel import Field, SQLModel


class ItemBase(SQLModel):
    name: str
    price_cents: int


class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
