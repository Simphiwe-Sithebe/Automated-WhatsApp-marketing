import datetime
from flask import Flask, request, render_template_string, redirect
import psycopg2
from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler import APScheduler
from clientDetails import ClientDetails
import pytz


app = Flask(__name__)

# Database connection details
DB_NAME = "Customers"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_to_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

@app.route('/submit_client', methods=['POST'])
def submit_client():
    name = request.form['name']
    surname = request.form['surname']
    number = request.form['number']
    email = request.form['email']
    birthday = request.form['birthday']
    last_check_up = request.form['last_check_up']

    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO client_details (name, surname, number, email, birthday, last_check_up)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (name, surname, number, email, birthday, last_check_up))
    
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/success')

@app.route('/success')
def success():
    return "Client details submitted successfully!"

# if __name__ == '__main__':
#     app.run(debug=True)

from twilio.rest import Client

# Twilio credentials (replace with your own)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio Sandbox Number

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number, message):
    client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=message,
        to=f'whatsapp:{to_number}'
    )

scheduler = APScheduler()

def check_birthdays():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM client_details")
    clients = cursor.fetchall()

    today = datetime.now().date()

    for client in clients:
        client_obj = ClientDetails(*client)
        if client_obj.birthday == today:
            message = f"Happy Birthday {client_obj.name}, your dentist cares!"
            send_whatsapp_message(client_obj.number, message)

    cursor.close()
    conn.close()

if __name__ == '__main__':
 # Schedule the birthday check task to run daily at 7 AM
    scheduler.add_job(
        func=check_birthdays,
        trigger="cron",
        hour=7,
        timezone=pytz.timezone("Africa/Johannesburg"),
        id='birthday_check'  # Adding a unique id for the job
    )
scheduler.start()

    # Start the Flask application
app.run(debug=True)