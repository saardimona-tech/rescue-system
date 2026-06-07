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

# ======================
# מסך ראשי
# ======================
@app.route("/")
def home():

    team_options = ""

    for team in TEAMS:
        team_options += f'<option value="{team}">{team}</option>'

    return f"""
    <html dir="rtl">
    <body style="font-family:Arial;text-align:center;margin-top:50px">

    <h1>🚑 מערכת חילוץ</h1>

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

    <br>

    <a href="/who">
        <button>👥 מי בזירה</button>
    </a>

    </body>
    </html>
    """

# ======================
# הרשמה
# ======================
@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    team = request.form["team"]

    found = False

    for user in users:
        if user["name"] == name:
            found = True

    if not found:
        users.append({
            "name": name,
            "team": team,
            "status": False
        })

    return user_page(name)

# ======================
# מסך משתמש
# ======================
def user_page(name):

    user = None

    for u in users:
        if u["name"] == name:
            user = u
            break

    return f"""
    <html dir="rtl">
    <body style="font-family:Arial;text-align:center;margin-top:50px">

    <h2>שלום {user['name']}</h2>

    <p>צוות: {user['team']}</p>

    <form action="/arrived" method="post">
        <input type="hidden" name="name" value="{user['name']}">

        <button type="submit">
            ✅ הגעתי לזירה
        </button>
    </form>

    <br>

    <form action="/left" method="post">
        <input type="hidden" name="name" value="{user['name']}">

        <button type="submit">
            ❌ יצאתי מהזירה
        </button>
    </form>

    <br>

    <a href="/who">
        <button>
            👥 מי בזירה
        </button>
    </a>

    </body>
    </html>
    """

# ======================
# הגעה לזירה
# ======================
@app.route("/arrived", methods=["POST"])
def arrived():

    name = request.form["name"]

    for user in users:
        if user["name"] == name:
            user["status"] = True

    return user_page(name)

# ======================
# יציאה מהזירה
# ======================
@app.route("/left", methods=["POST"])
def left():

    name = request.form["name"]

    for user in users:
        if user["name"] == name:
            user["status"] = False

    return user_page(name)

# ======================
# מי בזירה
# ======================
@app.route("/who")
def who():

    html = """
    <html dir="rtl">
    <body style="font-family:Arial;margin:30px">

    <h1>👥 מי בזירה</h1>
    """

    total = 0

    for team in TEAMS:

        html += f"<h3>{team}</h3>"

        team_count = 0

        for user in users:

            if user["team"] == team and user["status"]:

                team_count += 1
                total += 1

                html += f"{team_count}. {user['name']}<br>"

        html += f"<b>סה״כ בצוות: {team_count}</b><br><br>"

    html += f"""
    <hr>
    <h2>סה״כ בזירה: {total}</h2>

    <a href="/">
        <button>חזרה</button>
    </a>

    </body>
    </html>
    """

    return html

# ======================
# הפעלה
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)