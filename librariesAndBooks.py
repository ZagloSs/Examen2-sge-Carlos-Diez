import json
from datetime import date

import pandas as pd


readHashedUserJson = open("secure-users.json", "r")
UserData = json.load(readHashedUserJson)

class Book:

    def __init__(self, bookId, bookTitle, bookEditorial, bookPublication, libraryId):
        self.bookId = bookId
        self.bookTitle = bookTitle
        self.bookEditorial = bookEditorial
        self.bookPublication = bookPublication
        self.libraryId = libraryId
    def getBookTitle(self):
        return self.bookTitle
    def getId(self):
        return self.bookId
    def getLibrary(self):
        return self.libraryId



LibraryTemplate = {
    "IdLibrary": "",
    "books": [{
        "bookId": "",
        "bookTitle": "",
        "bookEditorial": "",
        "bookPublication": "",
        "UserId": "",
        "userFullName":""
    }
    ]
}
libraryId = []
for i in UserData:
    for j in range(len(i["books"])):
        if not (i["books"][j]["libraryId"] in libraryId):
            libraryId.append(i["books"][j]["libraryId"])



AllBooks=[]
for i in UserData:
    for j in i["books"]:
        LibroNuevo =  Book(j["bookId"], j["bookTitle"], j["bookEditorial"], j["bookPublication"], j["libraryId"])
        AllBooks.append(LibroNuevo)


Libraries=[]
for e in libraryId:
    books = []
    for b in AllBooks:
        if b.getLibrary() == e:

            book = {
                "bookId": b.getId(),
                "bookTitle": b.getBookTitle(),
                "bookEditorial": b.bookEditorial,
                "bookPublication": b.bookPublication
            }
            books.append(book)
    Libraries.append({
        "IdLibrary": e,
        "books": books
    })

print(Libraries)

newJson = open("libraries-and-books.json", "x")
newJson.write(json.dumps(Libraries, indent=4))

hoy = str(date.today())
fecha = hoy.split("-")

idLibraries = []
idLibros = []
titulo = []
editorial = []
aPubli = []

for i in Libraries:
    idLibraries.append(i["IdLibrary"])
    for e in range(len(i["books"]) -1):
        idLibros.append(i["books"][e]["bookId"])
        titulo.append(i["books"][e]["bookTitle"])
        editorial.append(i["books"][e]["bookEditorial"])
        aPubli.append(i["books"][e]["bookPublication"])

a = {"Id de libreria" : idLibraries, "Id de libro": idLibros, "Titulo": titulo, "Editorial": editorial, "Año de publicacion":aPubli}

pf = pd.DataFrame.from_dict(a, orient='index')
nombreExcel = fecha[0] + "-" + fecha[1] +"-libros-prestados.xlsx"
pf = pf.transpose()
pf.to_excel(nombreExcel)




