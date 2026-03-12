from typing import List
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.constants import Session
from app.models import AddressModel, PeopleModel
from app.schemas.data_collection import people

from app.exceptions import (
    EntityValidationError,
    NotFoundError,
    ForeignKeyReferenceError
)

class UnionRepository:

    def _verify_exists_address_id(self, addressId: str) -> None:
        with Session() as session:
            exist_address = session.query(AddressModel).filter(AddressModel.addressId == addressId).first() 
            if exist_address:
                raise ForeignKeyReferenceError("Informação de endereço já cadastrada no sistema.")

    def insert_people(self, schema: people.PeopleCreateSchema) -> people.PeopleReadSchema:
        
        with Session() as session:
            try: 
                people_model = PeopleModel(**schema.model_dump(exclude="addresses"))

                for row in schema.addresses:
                    model = AddressModel(**row.model_dump())
                    self._verify_exists_address_id(model.addressId)
                    people_model.addresses.append(model)
                    
                session.add(people_model)
                session.commit()
                response = people.PeopleReadSchema.model_validate(people_model)
               
                return response
            
            except IntegrityError as exc:
                session.rollback()
                raise EntityValidationError(f"Erro de integridade: {exc}")

            except Exception as exc:
                raise exc

    def get_by_id_people(self, peopleId: str) -> people.PeopleReadSchema:
        
        with Session() as session:
            try:
                stmt = select(PeopleModel).where(
                    PeopleModel.peopleId == peopleId
                )

                p = session.execute(stmt).scalar_one_or_none()

                if not p:
                    raise NotFoundError("Pessoa referida não foi encontrada.")
            
                return people.PeopleReadSchema.model_validate(p)
            
            except IntegrityError as exc:
                raise EntityValidationError(f"Erro de integridade: {str(exc)}")
        
    def get_all_people(self) -> List[people.PeopleReadSchema]:
        with Session() as session:
            stmt = select(PeopleModel)
            ind = session.execute(stmt).scalars().all()

            return [
                people.PeopleReadSchema.model_validate(p)
                for p in ind
            ]
        
    def delete_people(self, people_id: str) -> None:
        with Session() as session:
            try: 
                p = session.query(PeopleModel).filter(PeopleModel.peopleId == people_id).first()

                if not p:
                    raise NotFoundError("Pessoa referida não foi encontrada.")
                
                session.delete(p)
                session.commit()
                
            except IntegrityError as exc:
                raise EntityValidationError(f"Erro de integridade: {str(exc)}")

        