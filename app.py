from flask import Flask, render_template
import keys
app = Flask(__name__)
@app.route("/")

#part 1
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]

    filtered_fruits = []
    for fruit in fruits:
        if fruit["quantity"] < 3 and fruit["name"].startswith("o"):
            filtered_fruits.append(fruit)

    return render_template("index.html", fruits=fruits, filtered_fruits=filtered_fruits,key_1=keys.MY_SECRET_API_KEY_1, key_2=keys.MY_SECRET_API_KEY_2)

#part 2
def do_cool_things():
    print("I print the API key here, without having it in this file: ", keys.MY_SECRET_API_KEY_1)

