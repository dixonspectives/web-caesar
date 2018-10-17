from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!doctype html>
<html>
  <head>
    <style>
       form {
           background-color: #eee;
           padding: 20px;
           margin: 0 auto;
           width: 540px;
           font: 16px sans-serif;
           border-radius: 10px;
       }
       textarea {
           margin: 10px 0;
           width: 540px;
           height: 120px;
       }
    </style>
  </head>
  <body>  
    <form method="post">
      <label for ="rot">Rotate by:</label>
      <input name="rot" type="text" value="0" />
      <textarea form="text-area" name="text"> </textarea>
      <input type="submit" />
    </form>

  </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():

    rot = request.form['rot'] 
    rot = int(rot)
    
    text = request.form['text']

    encrypted = caesar.rotate_string(text, rot)

    encrypted_element = "<h1>" + encrypted + "</h1>"
    content = form + encrypted_element


    return content

app.run()