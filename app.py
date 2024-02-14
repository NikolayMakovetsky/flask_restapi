from flask import Flask, jsonify, g
from random import choice
from pathlib import Path
from werkzeug.exceptions import HTTPException

BASE_DIR = Path(__file__).parent
path_to_db = BASE_DIR / "test.db"  # <- тут путь к БД
# DATABASE = BASE_DIR / "test.db"  # <- тут путь к БД

# -----------------------------------------

app = Flask(__name__)


@app.route("/quotes")
def get_qoutes():
    # получение данных из бд
    select_quotes = "SELECT * from quotes"
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute(create_table)
    quotes_db = cursor.fetchall() # get list[tuple]
    connection.commit()
    cursor.close()
    connection.close()
    # подготовка данных для возврата
    # необходимо выполнить преобразование:
    # list[tuple] -> list[dict]
    keys = ["id", "author", "text"]
    quotes = []
    for quote_db in quotes_db:
        quote = dict(zip(keys, quote_db))
        quotes.append(quote)

    return jsonify(quotes)








@app.route("/")
def hello_world():
    return "Hello, World!"


about_me = {
   "name": "Николай",
   "surname": "Маковецкий",
   "email": "nicholasmakovetsky@gmail.com"
}


@app.route("/about")
def about():
   return about_me


quotes = [
   {
       "id": 3,
       "author": "Rick Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
   },
   {
       "id": 5,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
   },
   {
       "id": 6,
       "author": "Mosher’s Law of Software Engineering",
       "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
   },
   {
       "id": 8,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так."
   },

]


# @app.route("/quotes")
# def get_qoutes():
#    return quotes


# @app.route('/quotes/<int:id>') # тестовый вариант 1
# def get_qoute(id):
#     # return bool(quotes[id])
#     return quotes[id] if len(quotes) > id else "ошибка 404"


# 3, 5, 6, 8 - cуществующие цитаты
@app.route('/quotes/<int:quote_id>') # пытаемся привести строку к int
def get_qoute_by_id(quote_id):
    """ function return the quote by id.
        Type of quote is dict -> json"""
    for quote in quotes:
        if quote["id"] == quote_id:
            return quote, 200
    return f"Quote with id={quote_id} not found", 404


# dict -> json str  
@app.route('/quotes/count')
def get_count():
    """return count of quotes"""
    num = len(quotes)
    return {"count": num}, 200


# dict -> json str       
@app.route('/quotes/random')
def get_rnd_qoute():
    """return random quote"""
    return choice(quotes), 200


# post
@app.route('/quotes', methods=['POST'])
def create_qoute():
    new_quote = request.json
    last_quote = quotes[-1]
    new_id = last_quote['id'] + 1
    new_quote
    return choice(quotes)

@app.delete("/quotes/<int:quote_id>")
def delete_quote(quote_id):
    for quote in quotes:
        if quote["id"] == quote_id:
            quotes.remove(quote)
            return jsonify({"message": f'Quote with id={quote_id} has deleted'}), 200 # CTRL+. импортирование библиотеки по функции
    return {"error": f'Quote with id={quote_id} not found'}, 404



if __name__ == "__main__":
    app.run(debug=True)