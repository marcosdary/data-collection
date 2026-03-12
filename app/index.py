from flask import Flask, render_template, request, jsonify, redirect, url_for
from typing import List

from app.repositories.union_repository import UnionRepository
from app.utils import build_response
from app.schemas.api_error import ApiErrorModel
from app.schemas.api_response import ApiResponseModel
from app.schemas.data_collection.people import (
    PeopleCreateSchema,
    PeopleReadSchema
)
from app.schemas.data_collection.address import (
    AddressCreateSchema
)

class _MockRepo:
    def __init__(self):
        self.union_repo = UnionRepository()

    def get_all_people(self) -> ApiResponseModel[List[PeopleReadSchema], ApiErrorModel]:
        try:
            response = self.union_repo.get_all_people()
            return build_response(True, data=response)
        except Exception as exc:
            return build_response(False, exc=exc)

    def get_by_id_people(self, pid): 
        try:
            response = self.union_repo.get_by_id_people(pid)
            return build_response(True, data=response)
        except Exception as exc:
            return build_response(False, exc=exc)

    def insert_people(self, schema: PeopleCreateSchema) -> ApiResponseModel[PeopleReadSchema, ApiErrorModel]:
        try:
            response = self.union_repo.insert_people(schema)
            return build_response(True, data=response)
        except Exception as exc:
            return build_response(False, exc=exc)

    def delete_people(self, pid):
        try:
            self.union_repo.delete_people(pid)
            return build_response(True)
        except Exception as exc:
            return build_response(False, exc=exc)

mock_repo = _MockRepo()
# ─────────────────────────────────────────────────────────────────────────────

# ── Flask app ─────────────────────────────────────────────────────────────────
app = Flask(__name__, template_folder="templates")
app.secret_key = "people-manager-secret"


@app.route("/")
def index():
    res = mock_repo.get_all_people().model_dump()
    return render_template("index.html", res=res)

@app.route("/people/<pid>")
def detail(pid):
    res = mock_repo.get_by_id_people(pid).model_dump()
    return render_template("detail.html", res=res)
    
@app.route("/people/new", methods=["GET", "POST"])
def create():
    RACES    = ("AMARELA", "BRANCO", "INDIGENA", "PARDO", "PRETO")
    SEXES    = ("MASCULINO", "FEMININO")
    MARITAL  = ("SOLTEIRO", "CASADO", "DIVORCIADO", "VIUVO")
    EDUC     = (
        "SEM_INSTRUCAO", "ENSINO_FUNDAMENTAL_INCOMPLETO", 
        "ENSINO_FUNDAMENTAL_COMPLETO", "ENSINO_MEDIO_COMPLETO",
        "ENSINO_MEDIO_INCOMPLETO", "EDUCACAO_SUPERIOR_COMPLETO",
        "EDUCACAO_SUPERIOR_INCOMPLETO"
    )
    COMM     = (
        "QUILOMBOLA", "RIBEIRINHA", 
        "INDIGENA", "OUTROS"
    )
    STATES   = (
        "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
        "Espirito Santo", "Goiás", "Maranhão", "Mato Grosso do Sul", "Mato Grosso", 
        "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí",
        "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
        "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins",
    )

    if request.method == "POST":
        f = request.form
        schema = PeopleCreateSchema(
            familyGuardianName=f.get("familyGuardianName"),
            age=int(f.get("age", 0)),
            communityType=f.get("communityType"),
            familyMembers=int(f.get("familyMembers", 1)),
            educationLevel=f.get("educationLevel"),
            maritalStatus=f.get("maritalStatus"),
            occupation=f.get("occupation") or None,
            race=f.get("race"),
            sex=f.get("sex"),
            receivesSocialBenefit=f.get("receivesSocialBenefit") == "true",
            socialBenefitDescription=f.get("socialBenefitDescription") or None,
            addresses=[
                AddressCreateSchema(
                    addressId=f.get("addressId"),
                    city=f.get("city"),
                    complement=f.get("complement") or None,
                    neighborhood=f.get("neighborhood"),
                    number=f.get("number"),
                    state=f.get("state"),
                    street=f.get("street")
                )
            ]
        )
    
        response = mock_repo.insert_people(schema)
        if response.success:
            data = response.data
            return redirect(url_for("detail", pid=data.peopleId))
        else:
            return render_template("form.html",
            races=RACES, sexes=SEXES, marital=MARITAL,
            educ=EDUC, comm=COMM, stat=STATES,
            error=response.error.errorName, form_data=f), 422

    return render_template("form.html",
        races=RACES, sexes=SEXES, marital=MARITAL,
        educ=EDUC, comm=COMM, stat=STATES,
        error=None, form_data={})


@app.route("/people/<pid>/delete", methods=["POST"])
def delete(pid):
    response = mock_repo.delete_people(pid)
    if response.success:
        return redirect(url_for("index"))
    return render_template("index.html", res=response)

