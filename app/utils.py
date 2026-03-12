from app.schemas.api_error import ApiErrorModel
from app.schemas.api_response import ApiResponseModel

def build_response(success: bool, data=None, exc: Exception | None = None) -> ApiResponseModel:
    """Constrói um ApiResponse padronizado.

    Args:
        success: Indica se a operação foi bem‑sucedida.
        data: Valor a ser retornado quando success=True.
        exc: Exceção capturada quando success=False.

    Returns:
        ApiResponse: objeto pronto para ser retornado ao cliente.
    """
    if success:
        return ApiResponseModel(success=True, data=data)

    # Caso de erro
    return ApiResponseModel(
        success=False,
        error=ApiErrorModel(
            typeError=exc.__class__.__name__ if exc else "Error",
            errorName=str(exc) if exc else "",
            statusCode=getattr(exc, "status_code", 500),
        ),
    )
