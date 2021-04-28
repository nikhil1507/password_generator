from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


password = None
secured_password = None


@app.route('/', methods=['POST', 'GET'])
def initRoute():
    password = request.form.get('password')

    if password == None:
        return render_template("pass.html", password=" ")

    secured_password = myHashFunc(password)

    return render_template("pass.html", password=secured_password)


def myHashFunc(password):
    given_pass = password
    str_len = len(password)
    for i in range(str_len):
        given_pass = "$" + given_pass + "#"
    return given_pass


if __name__ == "__main__":
    app.run(debug=True)
