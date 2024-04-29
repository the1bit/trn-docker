from flask import Flask, request


app = Flask(__name__)

# Kezdőoldal
@app.route("/", methods=["GET"])
def info():
    return "Docker alkalmazás"

# Helló Világ!
@app.route("/hello", methods=["GET"])
def hello():
    return "Helló Világ!"

# Paraméterezett Helló
@app.route("/name", methods=["GET"])
def name():
    try:
        username = request.args.get("name")
        return "Helló " + username + "!"
    except Exception as e:
        return "Hiányzó paraméter: Így használd: `?name={név}`"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
