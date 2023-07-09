from flask import Flask, render_template, abort

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
# create a dictionary to map slugs to projects so that we don't have to loop through all projects
# whenever we want to get a slug
slug_to_project = {project['slug']: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    # if the slug doesn't exist return a 404 error
    if slug not in slug_to_project:
        abort(404)
    # return a render template using the slug to get the needed html page
    return render_template(f"project_{slug}.html", 
                           project=slug_to_project[slug]
                           )