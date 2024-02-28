import hashlib
import json

def hashing(str):
    encrypted = hashlib.sha256(str.encode()).hexdigest()
    return encrypted

writeable = open("users.json", "r")
users = open("users.json")
usersData = json.load(users)

passwordstoHash = []
for i in usersData:
    passwordstoHash.append(i["password"])


passwordHashed =  []
for a in passwordstoHash:
    passwordHashed.append(hashing(a))
print(passwordstoHash)
print(passwordHashed)

for e in range(len(passwordHashed) -1):
    usersData[e]["password"] = passwordHashed[e]

newJson = open("secure-users.json", "x")
newJson.write(json.dumps(usersData))






