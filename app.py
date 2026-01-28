import os
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "secret"

# Mock database
birthdays = [
    {"id": 1, "name": "Harry Potter", "month": 7, "day": 31},
    {"id": 2, "name": "Hermione Granger", "month": 9, "day": 19}
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        if not name or not month or not day:
            flash("Missing information!")
            return redirect("/")

        birthdays.append({
            "id": len(birthdays) + 1,
            "name": name,
            "month": int(month),
            "day": int(day)
        })
        return redirect("/")

    else:
        return render_template("index.html", birthdays=birthdays)

if __name__ == "__main__":
    app.run(debug=True)
