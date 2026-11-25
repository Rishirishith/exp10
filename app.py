from flask import Flask
import os
app = Flask(__name__)
@app.route("/")
def home():
  version = os.getenv("APP_VERSION","V1.0")
  RETURN F"<h1>Hello Student! Running container Build:
  {version}</h1>"
  if __name__==" __main__":
     app.run(host="0.0.0.0" ,port=5000)
