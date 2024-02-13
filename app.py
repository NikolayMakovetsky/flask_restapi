from flask import Flask

app = Flask(__name__)


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


@app.route("/quotes")
def get_qoutes():
   return quotes



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
    

@app.route('/quotes/count')
def get_count():
    """return count of quotes"""
    num = len(quotes)
    return {"count": num}
        


if __name__ == "__main__":
    app.run(debug=True)