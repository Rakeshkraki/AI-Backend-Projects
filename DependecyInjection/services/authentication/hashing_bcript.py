from bcrypt import gensalt, hashpw, checkpw


class BcryptHashing:

    def bcrypt_hashing(self, password: str) -> bytes:
        salt = gensalt()
        return hashpw(password.encode("utf-8"), salt)

    def verify_hash(
        self,
        password: str,
        stored_hashcode: bytes
    ) -> bool:
        return checkpw(
            password.encode("utf-8"),
            stored_hashcode
        )


bcrypt_hash = BcryptHashing()

stored_hash = bcrypt_hash.bcrypt_hashing("name@123")

print("Stored hash:", stored_hash)

verification = bcrypt_hash.verify_hash(
    "name@123",
    stored_hash
)

print("valid" if verification else "invalid")