from typing import Union

from pydantic import BaseModel


class Rocket(BaseModel):
    id: str
    name: str
    description: str
    wikipedia: str

    class Config:
        orm_mode = True


class Launch(BaseModel):
    id: str
    details: str
    mission_name: str

    class Config:
        orm_mode = True
