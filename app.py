from flask import Flask, render_template, request, redirect, url_for, flash
from topsis_service.topsis_handler import run_topsis
from topsis_service.email_service import send_email
import os

app = Flask(__name__)
app.secret_key = "secret_key"
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"csv", "xlsx"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        weights = request.form.get("weights")
        impacts = request.form.get("impacts")
        email = request.form.get("email")

        if not file or not weights or not impacts or not email:
            flash("All fields are required!")
            return redirect(url_for("index"))

        if not allowed_file(file.filename):
            flash("Invalid file format! Please upload a .csv or .xlsx file.")
            return redirect(url_for("index"))

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)

        try:
            result_file = run_topsis(input_path, weights, impacts, RESULT_FOLDER)
            send_email(email, result_file)
            flash(f"Result file sent to {email}!")
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)