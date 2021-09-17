import requests
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/random_joke')
def random_joke():
  response = requests.get('https://api.chucknorris.io/jokes/random')
  newJoke = response.json()
  
  conn = sqlite3.connect('jokes.db')
  cursor = conn.cursor()

  cursor.execute(f"""INSERT INTO jokes VALUES("{newJoke['id']}", "{newJoke['url']}", "{newJoke['value']}")""")

  conn.commit()
  cursor.close()
  conn.close()

  return newJoke['value']



@app.route('/saved_jokes')
def saved_jokes():
  data_json = []

  conn = sqlite3.connect('jokes.db')
  cursor = conn.cursor()

  raws = cursor.execute(f"""SELECT * FROM jokes""")
  jokes = raws.fetchall()

  for i in jokes:
    data_json.append({"id": i[0], "url": i[1], "joke": i[2]})


  conn.commit()
  cursor.close()
  conn.close()

  return jsonify(data_json)



if __name__ == "__main__":
  app.run(debug=True)