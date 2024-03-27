from flask import Flask, render_template
from forms import RegisterForm, LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "1234"


posts = [
    {
    "Author": "AL",
    "Post": "Post 1",
    "Date": "1/1/1111",
},
{
    "author": "BL",
    "post": "Post 2",
    "date": "2/2/2222",
}
]


@app.route("/")
def hello_world():
    return render_template("home.html", posts=posts)


@app.route("/register")
def register():
    form = RegisterForm()
    return form


@app.route("/faruz")
def faruz():
    return "Faruz Rocks!!!"





if __name__ == "__main__":
    app.run(debug=True)