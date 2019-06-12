import Encrypter
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    if request.form:
        print(request.form)
    return render_template("index.html")

Encrypter.encode_text("A000000000000000" , "Hello World")

"""@app.route("/convert")
def convert():
    return render_template("convert.html")

@app.route("/result")
def result():
    return render_template("result.html")"""

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == "__main__":
    app.run(debug=True)