from pydantic import field_serializer

from app.schemas.data_collection.address.base import AddressBaseSchema
from app.exceptions import InvalidFieldsException

class AddressCreateSchema(AddressBaseSchema):
    
    @field_serializer("addressId", mode="plain")
    def serialize_post_code(self, value: str) -> str:
        return value.replace("-", "").replace(".", "")
