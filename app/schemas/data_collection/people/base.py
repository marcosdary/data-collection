from pydantic import BaseModel, ConfigDict

from app.enums import CommunityTypeEnum, MaritialStatusEnum, RaceEnum, SexEnum, EducationLevelEnum

class PeopleBaseSchema(BaseModel):
    age: int
    race: RaceEnum
    sex: SexEnum
    familyGuardianName: str
    receivesSocialBenefit: bool
    socialBenefitDescription: str | None = None
    maritalStatus: MaritialStatusEnum
    occupation: str | None = None
    educationLevel: EducationLevelEnum
    communityType: CommunityTypeEnum

    model_config = ConfigDict(from_attributes=True)

    