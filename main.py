from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "this is a test, if you see this jump for joy"

if __name__ == "__main__":
    app.run(debug=True, port=7000)

