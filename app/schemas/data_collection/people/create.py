from typing import List

from app.schemas.data_collection.address.create import AddressCreateSchema
from app.schemas.data_collection.people.base import PeopleBaseSchema

class PeopleCreateSchema(PeopleBaseSchema):
    addresses: List[AddressCreateSchema]
    familyMembers: int = 1