# Create a registration system that converts your entered text to md5
import hashlib

def text_to_md5(text):
    hashed = hashlib.md5(text.encode())
    md5_hash = hashed.hexdigest()
    return md5_hash

if __name__ == '__main__':
    name = "carlos"
    email = "carlopoblete@gmail.com"
    password = "password"
    # password = input("enter password: ")

    print("--REGISTRATION FORM---")
    print(f"name: {name}")
    print(f"email: {email}")
    print(f"password: {'*' * len(password)}")
    print(f"md5hashed password: {text_to_md5(password)}")
