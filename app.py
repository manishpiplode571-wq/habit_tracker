from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "habit_tracker_secret"


# ---------- Database Helper ----------
def get_db():
    conn = sqlite3.connect("habit.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------- Table Banao ----------
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


init_db()


# ---------- Home: List (READ) ----------
@app.route("/")
def index():
    conn = get_db()
    habits = conn.execute("SELECT * FROM habits").fetchall()
    conn.close()
    return render_template("index.html", habits=habits)


# ---------- Add (CREATE) ----------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"].strip()

        if not name:
            flash("Habit name cannot to empty", "error")
            return render_template("add.html")

        conn = get_db()
        conn.execute("INSERT INTO habits (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        flash("Habit added sucessfully!", "success")
        return redirect(url_for("index"))

    return render_template("add.html")


# ---------- Edit (UPDATE) ----------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()

    if request.method == "POST":
        name = request.form["name"].strip()

        if not name:
            flash("Habit name cannot to empty", "error")
            habit = conn.execute("SELECT * FROM habits WHERE id=?", (id,)).fetchone()
            conn.close()
            return render_template("edit.html", habit=habit)

        conn.execute("UPDATE habits SET name=? WHERE id=?", (name, id))
        conn.commit()
        conn.close()

        flash("Habit updated sucessfully!", "success")
        return redirect(url_for("index"))

    habit = conn.execute("SELECT * FROM habits WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", habit=habit)


# ---------- Delete (DELETE) ----------
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM habits WHERE id=?", (id,))
    conn.commit()
    conn.close()

    flash("Habit delete sucessfully!", "success")
    return redirect(url_for("index"))


# ---------- Toggle Done/Not Done ----------
@app.route("/toggle/<int:id>")
def toggle(id):
    conn = get_db()
    habit = conn.execute("SELECT * FROM habits WHERE id=?", (id,)).fetchone()

    new_done = 0 if habit["done"] == 1 else 1
    conn.execute("UPDATE habits SET done=? WHERE id=?", (new_done, id))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# ---------- Run ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
