from argon2 import PasswordHasher
from argon2.exceptions import VerificationError


class PasswordService:
    def __init__(self, password_hasher: PasswordHasher | None = None) -> None:
        self._hasher = password_hasher or PasswordHasher()

    def hash_password(self, password: str) -> str:
        return self._hasher.hash(password)

    def verify_password(self, password: str, password_hash: str) -> bool:
        try:
            return self._hasher.verify(password_hash, password)
        except VerificationError:
            return False


password_service = PasswordService()

password_hash = password_service.hash_password("name!123")
print(password_hash)

is_valid = password_service.verify_password(
    "name!123",
    password_hash,
)

print("Password is correct" if is_valid else "Invalid password")
