import sqlite3

conn = sqlite3.connect('jokes.db')
cursor = conn.cursor()

cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS jokes(
      id TEXT,
      url TEXT,
      joke TEXT
    )
  """
)

conn.commit()
cursor.close()
conn.close()