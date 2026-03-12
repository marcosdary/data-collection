from sqlalchemy import Column, VARCHAR, CHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel

class AddressModel(BaseModel):

    __tablename__ = "address"
    
    addressId = Column(VARCHAR(9), primary_key=True)
    peopleId = Column(VARCHAR(255), ForeignKey("people.peopleId"), nullable=False)
    street = Column(VARCHAR(255), nullable=False)
    number = Column(VARCHAR(10))
    complement = Column(VARCHAR(255))
    neighborhood = Column(VARCHAR(100), nullable=False)
    city = Column(VARCHAR(100), nullable=False)
    state = Column(CHAR(2), nullable=False)

    people = relationship("PeopleModel", back_populates="addresses")
    