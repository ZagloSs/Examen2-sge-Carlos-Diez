import json
import pandas as pd
from openpyxl.workbook import Workbook

readHashedUserJson = open("secure-users.json", "r")
UserData = json.load(readHashedUserJson)

userId = []
userPass = []

for i in UserData:
    userId.append(i["userId"])
    userPass.append(i["password"])

print(userId)
print(userPass)

pf = pd.DataFrame({"Id de Usuario":userId, "contraseña": userPass})
excelName = "usuarios.xlsx"
pf.to_excel(excelName)