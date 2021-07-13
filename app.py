from flask import Flask, render_template
from config import MONGO_DB

from routes.user_bp import user_bp

app = Flask(__name__)
app.config.from_object("config")
MONGO_DB.init_app(app)


app.register_blueprint(user_bp, url_prefix="/users")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()