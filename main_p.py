import flask
from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()
#print(f"ALL ENVS: {dict(os.environ)}")



def get_discord_webhook(message):
   webhook =os.getenv('WEBHOOK')
   print(f"DEBUG: Webhook value is: {webhook}") # תבדוק מה מודפס בטרמינל
   if not webhook:
       print(" שגיאה: המשתנה WEBHOOK לא נמצא ב-env!")
       return "error"
   data_1 = {'content': message}
   response_1 = requests.post(webhook, json=data_1)
   try:
      response_1.raise_for_status()
      return response_1.text
   except requests.exceptions.ConnectionError:
      # זה יקרה כשאין אינטרנט או שה-URL לא קיים בכלל
      print(" שגיאה: אין חיבור לאינטרנט!")
      return "connection_error"


def send_text_db(name, age, review):
   try:
      connection = sqlite3.connect('MY_DATABASE.db')
      cursor = connection.cursor()
      cursor.execute('''insert into MY_TABLE(name,age,review) values(?,?,?)''', (name, age, review))
      connection.commit()
      connection.close()
   except Exception as e:
      print(f'הזנת הפרטים שגויה {e}')
      return 'error'




app = Flask('myapp')


@app.route('/')
def get_input():
   return flask.render_template("index.html")



@app.route('/submit', methods=['POST'])
def submit():
      name = request.form['name']
      age = request.form['age']
      review = request.form['review']
      get_discord_webhook(f'my name is : {name} and age is : {age} and review is:  {review}')
      send_text_db(name, age, review)
      try:
         age_val = int(age)
         if age_val < 14:
            return 'error'
      except ValueError:
         return 'error'
      return flask.render_template("first.html")



@app.route('/recent_messages')
def get_recent():
   connection = sqlite3.connect('MY_DATABASE.db')
   cursor = connection.cursor()
   query = "SELECT * FROM MY_TABLE WHERE created_at >= datetime('now', '-30 minutes')"
   cursor.execute(query)
   rows = cursor.fetchall()

   messages_list = []
   for row in rows:
      # כאן אנחנו בונים אובייקט (מילון) לכל שורה לפי הסדר בטבלה
      messages_list.append({
         'id': row[0],
         'name': row[1],
         'age': row[2],
         'review': row[3],
         'time': row[4]
      })
   connection.close()
   # עכשיו jsonify יחזיר מערך של אובייקטים [{...}, {...}]
   return jsonify(messages_list)

if __name__ == '__main__':
   app.run(debug=True)

















