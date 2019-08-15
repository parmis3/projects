from flask import Flask

app = Flask("My_app")


@app.route("/")
def main():
    return "Salam"

app.run()