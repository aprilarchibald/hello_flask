from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase = "hello", times=5)

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi, " + name + "!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return f"{word * num}"


@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id




if __name__=="__main__":
    app.run(debug=True)