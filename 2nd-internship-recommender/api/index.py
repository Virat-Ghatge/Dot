from flask import Flask, render_template, request
from recommender import recommend_internships
from flask_cors import CORS
from mangum import Mangum

app = Flask(__name__, template_folder="../templates")
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_skills = request.form['skills']
    recommendations = recommend_internships(user_skills)
    return render_template("result.html", recommendations=recommendations)

handler = Mangum(app)
