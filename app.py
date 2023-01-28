from flask import Flask, request
from random import choice

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

about_me = {
   "name": "Наталья",
   "surname": "Загребина",
   "email": "deira@bk.ru"
}

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
   }
]


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/quotes")
def get_quotes():
    return quotes


# Задания 1-2
@app.route("/quotes/<int:quote_id>")
def show_quote_by_id(quote_id):
    for quote in quotes:
        if quote["id"] == quote_id:
            return quote, 200
    return f"Quote with id={quote_id} not found", 404


# Задание 3
@app.route("/quotes/count")
def quotes_count():
    quotes_total = {
        "quotes_total": len(quotes)
    }
    return quotes_total


# Задание 4
@app.route("/quotes/random")
def get_random_quote():
    return choice(quotes)


@app.route("/about")
def about():
    return about_me


# Практика 1.2 Задания 1-2
@app.route("/quotes", methods=["POST"])
def create_quote():
    new_quote = request.json
    last_quote = quotes[-1]
    new_id = last_quote["id"] + 1
    new_quote["id"] = new_id
    quotes.append(new_quote)
    return new_quote, 201


# Задание 4
@app.route("/quotes/<int:quote_id>", methods=['PUT'])
def edit_quote(quote_id):
    for quote in quotes:
        if quote_id == quote["id"]:
            new_data = request.json
            if "author" in new_data:
                quote["author"] = new_data['author']
            if "text" in new_data:
                quote['text'] = new_data['text']
            return quote, 200
    return f"Quote with id={quote_id} not found", 404


# Задание 5
@app.route("/quotes/<int:quote_id>", methods=['DELETE'])
def delete(quote_id):
    for quote in quotes:
        if quote["id"] == quote_id:
            del quotes[quote_id - 1]
            return f'Quote with id = {quote_id} is delete', 204
    return f"Quote with id={quote_id} not found", 404


if __name__ == "__main__":
    app.run(debug=True)
