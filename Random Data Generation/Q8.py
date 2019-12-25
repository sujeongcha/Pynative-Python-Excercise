#Generate random secure token of 64 bytes and random URL

#My Solution
import secrets

token = secrets.token_bytes(64)
url = secrets.token_urlsafe(64)

print("Random secure Hexadecimal token is ", token)
print("Random secure URL is ", url)
