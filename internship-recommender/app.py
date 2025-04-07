from flask import Flask, render_template, request
from recommender import recommend_internships

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_skills = request.form['skills']
    recommendations = recommend_internships(user_skills)
    return render_template("result.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
