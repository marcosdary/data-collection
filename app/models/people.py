from sqlalchemy import Column, VARCHAR, INTEGER, BOOLEAN, Enum, ForeignKey, DATETIME, func
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.models.base import BaseModel
from app.enums import (
    MaritialStatusEnum, 
    EducationLevelEnum, 
    CommunityTypeEnum, 
    RaceEnum, 
    SexEnum
)

class PeopleModel(BaseModel):

    __tablename__ = "people"

    peopleId = Column(VARCHAR(255), primary_key=True, default=lambda: str(uuid4()))
    age = Column(INTEGER, nullable=False)
    familyMembers = Column(INTEGER, nullable=False)
    race = Column(Enum(RaceEnum, name="race_enum"), nullable=False)
    sex = Column(Enum(SexEnum, name="sex_enum"), nullable=False)
    familyGuardianName = Column(VARCHAR(255))
    receivesSocialBenefit = Column(BOOLEAN)
    socialBenefitDescription = Column(VARCHAR(255))
    maritalStatus = Column(Enum(MaritialStatusEnum, name="marital_status_enum"))
    occupation = Column(VARCHAR(150))
    educationLevel = Column(Enum(EducationLevelEnum, bname="education_level_enum"))
    communityType = Column(Enum(CommunityTypeEnum, name="community_type_enum"))
    createdAt = Column(DATETIME, default=func.current_timestamp())
    updatedAt = Column(DATETIME, server_default=func.current_timestamp(), server_onupdate=func.current_timestamp())

    addresses = relationship("AddressModel", back_populates="people", cascade="all, delete-orphan")