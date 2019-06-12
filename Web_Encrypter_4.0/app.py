import Encrypter
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      keytext = result['key']
      textinput = result['textin'] 
      if request.form.get('Decrypt'):
        textout = Encrypter.decode_text(keytext,textinput)
      else:
        textout = Encrypter.encode_text(keytext,textinput)                        

      return render_template("result.html",result = textout)

if __name__ == "__main__":
    app.run(debug=True)