import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/random_joke')
def joke():
  response = requests.get('https://api.chucknorris.io/jokes/random')
  print(response.json())
  return f"<p>{response.json()['value']}</p>"


if __name__ == "__main__":
  app.run(debug=True)