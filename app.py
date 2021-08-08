from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy, Model



app = Flask(__name__)

#@app.route("/")
@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        print("Hii")
        uname = request.form["uname"]
        print(uname)
        with open("test.tfvars", "w") as fo:
            fo.write("name = "+ uname)
        return render_template('Ok.html')
    return render_template('app.html')




if __name__ == "__main__":
    app.run(debug=True, port=5026)