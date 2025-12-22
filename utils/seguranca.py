import hashlib

def calcular_sha256(texto: str) -> str:
    """Calcula o hash SHA-256 de um texto."""
    sha256 = hashlib.sha256()
    sha256.update(texto.encode('utf-8'))
    return sha256.hexdigest()

def verificar_senha(senha_texto: str, senha_hash: str) -> bool:
    """Verifica se uma senha em texto plano corresponde ao hash armazenado."""
    return calcular_sha256(senha_texto) == senha_hash