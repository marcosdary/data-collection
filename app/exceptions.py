# =============================================================================
# EXCEÇÕES DE RECURSO / CONSULTA
# =============================================================================
class NotFoundError(Exception):
    """Recurso solicitado não foi localizado."""
    status_code=404


class NotFoundFile(Exception):
    """Arquivo solicitado não foi encontrado."""
    status_code=404

# =============================================================================
# EXCEÇÕES DE VALIDAÇÃO DE DADOS
# =============================================================================
class EntityValidationError(Exception):
    """Falha de validação ao inserir ou atualizar dados."""
    status_code=422

class InvalidFieldsException(Exception):
    """Campos obrigatórios ausentes ou inválidos."""
    status_code=422

class UnprocessableEntity(Exception):
    """Erro de consistência ou semântica nos dados."""
    status_code=422


# =============================================================================
# EXCEÇÕES DE AUTENTICAÇÃO / CREDENCIAIS
# =============================================================================
class InvalidCredentialsException(Exception):
    """Credenciais de autenticação inválidas."""
    status_code=401

# =============================================================================
# EXCEÇÕES DE INTEGRIDADE / DUPLICIDADE
# =============================================================================
class DuplicateReviewError(Exception):
    """Tentativa de inserir registro duplicado."""
    status_code=409


class ForeignKeyReferenceError(Exception):
    """Falha de integridade referencial."""
    status_code=409


# =============================================================================
# EXCEÇÕES GENÉRICAS / DESCONHECIDAS
# =============================================================================
class UnknownError(Exception):
    """Erro não identificado – fallback genérico."""
    status_code=500


# =============================================================================
# EXCEÇÕES DE SESSÃO
# =============================================================================
class SessionError(Exception):
    """Erro relacionado à sessão do usuário ou ao gerenciamento de sessão."""
    status_code=401

# =============================================================================
# EXCEÇÃO DE LIMITE DE REQUISIÇÕES
# =============================================================================
class TooManyRequestsError(Exception):
    """Número de requisições excedido – limite de taxa atingido."""
    status_code=429


# =============================================================================
# EXCEÇÃO DE EXPIRAÇÃO
# =============================================================================
class ExpirationError(Exception):
    """Recurso ou sessão expirada."""
    status_code=401

# =============================================================================
# EXCEÇÃO DE ROTA PROTEGIDA
# =============================================================================
class ProtectedRouteError(Exception):
    """Acesso a rota protegida sem permissão adequada."""
    status_code=403