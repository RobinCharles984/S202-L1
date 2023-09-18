from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import BookCRUD

db = Database(database="relatorio_05", collection="pessoas")
bookModel = BookModel(database=db)


bookCLI = BookCRUD(bookModel)
bookCLI.run()