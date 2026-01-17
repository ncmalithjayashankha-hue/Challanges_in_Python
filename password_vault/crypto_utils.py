import hashlib
from cryptography.fernet import Fernet
import base64

def hash_master_password(password: str)->str:
    hash_bytes = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash_bytes).decode()

def verify_master_password(password: str,stored_hash:str)->bool:
    return hash_master_password(password) == stored_hash

def generate_key() ->bytes:
    return Fernet.generate_key()

def encrypt_data(key:bytes, data:str)->str:
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted.decode()

def decrypt_data(key:bytes, token:str)-> str:
    fernet = Fernet(key)
    decrypted = fernet.decrypt(token.encode())
    return decrypted.decode()