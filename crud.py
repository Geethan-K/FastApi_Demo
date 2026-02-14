from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
    "id":1,
    "title":"Alchemist",
    "author":"Paulo Coelho"
    },
     {
    "id":2,
    "title":"Alchemist",
    "author":"Paulo Coelho"
    },
     {
    "id":3,
    "title":"Alchemist",
    "author":"Paulo Coelho"
    },
     {
    "id":4,
    "title":"Alchemist",
    "author":"Paulo Coelho"
    },

]

@app.get("/get_books")
def get_books():
    return books

class book(BaseModel):
    id:int
    title:str
    author:str

@app.post("/add_book")
def add_book():
    new_book = book.model_dump()
    books.append(new_book)
    return books

@app.get("get_book_by_id/{bookid}")
def get_book_by_id(bookid:int):
    for book in books:
        if book["id"] == bookid:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Book not found")

class UpdateBookFormt(BaseModel):
    title:str
    author:str

@app.put("/update_book/{bookid}")
def update_book(bookid:int , new_details:UpdateBookFormt):
    for book in books:
        if book["id"] == bookid:
            book["title"] = new_details.title
            book["author"] = new_details.author
        return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")