from flask import Flask, request

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
    <form action="/caesar" method="post">
      <label for ="rot">Rotate by:</label>
      <input name="rot" type="text" value="0" />
    </form>
    <br>
    <textarea form="text-area" name="text">
      <input type="submit" />
    </textarea>

  </body>
</html>
  """
@app.route("/")
def index():
    #caesar_form = request.form[rot]
    return form