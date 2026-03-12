from pydantic import BaseModel, ConfigDict

class AddressBaseSchema(BaseModel):
    addressId: str  # CEP
    street: str  # Rua
    number: str  # Número
    complement: str | None = None  # Complemento
    neighborhood: str  # Bairro
    city: str  # Cidade
    state: str  # Estado

    model_config = ConfigDict(from_attributes=True)