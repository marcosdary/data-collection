from datetime import datetime
from typing import List
from pydantic import field_serializer

from app.schemas.data_collection.address.read import AddressReadSchema
from app.schemas.data_collection.people.base import PeopleBaseSchema

class PeopleReadSchema(PeopleBaseSchema):
    peopleId: str
    addresses: List[AddressReadSchema] | None = None
    createdAt: datetime
    updatedAt: datetime

    @field_serializer("createdAt", "updatedAt", mode="plain")
    def serialize_dates(self, value: datetime) -> str:
        return value.strftime("%d-%m-%Y, %H:%M")
    
    
    