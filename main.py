from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

page_header = """
<!DOCTYPE html>
<html>
  <head>
    <title>Web-Caesar</title>
  </head>
  <body>
"""

page_footer = """
    </body>
</html>
"""

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
    <form action="/" method="post">
      <label for ="rot">Rotate by:</label>
      <input name="rot" type="text" value="0" />
      <textarea name="text"> </textarea>
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

    user_rot = request.form['rot'] 
    user_rot = int(user_rot)
    
    user_text = request.form['text']

    encrypted = rotate_string(user_text, user_rot)

    encrypted_element = "<h1>" + encrypted + "</h1>"
    content = page_header + encrypted_element + page_footer


    return content

app.run()