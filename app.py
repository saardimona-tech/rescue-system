from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>מערכת חילוץ</h1>
    <p>האתר עובד 🚑</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)