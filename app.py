from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    @app.route("/")
    def home():
        return render_template("base.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
