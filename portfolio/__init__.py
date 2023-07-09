from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app using Flask and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", 'css', 'html'],
        'slug': 'habit-tracking',
        'prod': 'https://flask-habit-tracker-91g6.onrender.com/'
    },
    {
        "name": "Microblog app using Flask and MongoDB",
        "thumb": "img/microblog.png",
        "hero": "img/microblog-hero.png",
        "categories": ["python", 'css', 'html'],
        'slug': 'microblog',
        'prod': 'https://flask-microblog-utz5.onrender.com/'
    },
]


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
