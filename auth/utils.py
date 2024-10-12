import hashlib

def hash_email(email: str) -> str:
    # Eliminamos los espacios en blanco
    email = email.strip()
    # Forzamos todos los caracteres en minúscula
    email = email.lower()

    # Obtenemos el hash md5
    hash = hashlib.md5(email.encode())

    return hash.hexdigest()


print(hash_email("jjjarac@eafit.edu.co"))