from flask import Flask, request

app = Flask(__name__)

TEAMS = [
    "צוות 1",
    "צוות 2",
    "צוות 3",
    "צוות רפואה",
    "מודיעין אוכלוסייה",
    "צוות פיקוד"
]

users = []

@app.route("/")
def home():
    team_options = ""

    for team in TEAMS:
        team_options += f'<option value="{team}">{team}</option>'

    return f"""
    <html dir="rtl">
    <body style="font-family:Arial;text-align:center;margin-top:50px">

    <h1>מערכת חילוץ 🚑</h1>

    <form action="/register" method="post">

        <input
            type="text"
            name="name"
            placeholder="שם מלא"
            required
        >

        <br><br>

        <select name="team">
            {team_options}
        </select>

        <br><br>

        <button type="submit">
            כניסה
        </button>

    </form>

    </body>
    </html>
    """

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    team = request.form["team"]

    users.append({
        "name": name,
        "team": team,
        "status": False
    })

    return f"""
    <html dir="rtl">
    <body style="font-family:Arial;text-align:center;margin-top:50px">

    <h2>שלום {name}</h2>

    <p>צוות: {team}</p>

    <button>✅ הגעתי לזירה</button>

    <br><br>

    <button>❌ יצאתי מהזירה</button>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)