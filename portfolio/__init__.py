from flask import Flask, render_template, abort
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    projects = [
        {
            "name": "Postit",
            "thumb": "img/postit.png",
            "hero": "img/postit-hero.jpg",
            "categories": ["python", 'css', 'html'],
            'slug': 'postit',
            'prod': 'https://postit-3n3g.onrender.com'
        },
        {
            "name": "A simple Cookie Clicker style game",
            "thumb": "img/weight.jpg",
            "hero": "img/weight-hero.jpg",
            "categories": ["python", 'css', 'html'],
            'slug': 'weight-clicker',
            'prod': 'https://weight-clicker.onrender.com/'
        },
        {
            "name": "Habit tracking app using Flask and MongoDB",
            "thumb": "img/habit-tracking.png",
            "hero": "img/habit-tracking-hero.png",
            "categories": ["python", 'css', 'html', 'Udemy'],
            'slug': 'habit-tracking',
            'prod': 'https://flask-habit-tracker-91g6.onrender.com/'
        },
        {
            "name": "Movie Watchlist",
            "thumb": "img/movie.jpg",
            "hero": "img/movie-hero.jpg",
            "categories": ["python", 'css', 'html', 'Udemy'],
            'slug': 'movie-watchlist',
            'prod': 'https://movie-watchlist-eyzg.onrender.com/'
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

    @app.errorhandler(404)
    def pagenotfound(error):
        return render_template("404.html"), 404

    return app