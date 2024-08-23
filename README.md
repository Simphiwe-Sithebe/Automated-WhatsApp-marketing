# Automated-WhatsApp-marketing
This application allows for the management of client details, including the storage of personal information and automated birthday greetings via WhatsApp. The system is built using Flask for the web interface, PostgreSQL for data storage, and the WhatsApp Business API for sending messages.

Features
Client Data Collection: Users can submit client details through an HTML form.
Data Storage: Client details are securely stored in a PostgreSQL database.
Automated Birthday Greetings: The system checks daily at 7 AM for clients' birthdays and sends a personalized WhatsApp message.
WhatsApp Integration: Messages are sent directly from your registered WhatsApp Business number.
Prerequisites
Before running this application, ensure you have the following installed:

Python 3.x
PostgreSQL
Flask
Required Python packages (requirements.txt provided)
API and Credentials
WhatsApp Business API: You must have access to the WhatsApp Business API.
Twilio/Alternative BSP: If using a BSP like Twilio, you will need an account and API credentials.
Installation
Clone the Repository:

Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file in the project root and add the following:

makefile
Copy code
DB_NAME=Customers
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
WHATSAPP_API_URL=https://api.whatsapp.com/v1/messages
WHATSAPP_API_TOKEN=your_api_token
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
Set Up the Database:

Create the PostgreSQL database:
bash
Copy code
psql -U your_db_username -c "CREATE DATABASE Customers;"
Run the SQL script to create the client_details table and populate it with sample data.
Run the Flask Application:

bash
Copy code
python app.py
Access the Web Form:
Open your browser and go to http://localhost:5000/client_form.html to submit client details.

Daily Birthday Check
The application includes a scheduled task that runs daily at 7 AM (local time). This task checks if any client has a birthday today and sends them a personalized WhatsApp message.

Scheduling with APScheduler
The APScheduler library is used to schedule the birthday check. The schedule is configured in the app.py file, and it triggers the check_birthdays function daily.

Sending WhatsApp Messages
Messages are sent using the WhatsApp Business API. If you are using Twilio or another BSP, ensure that your API credentials are correctly set up in the .env file.

Deployment
To deploy this application on a server:

Choose a Hosting Platform: AWS, Heroku, or any VPS that supports Python and PostgreSQL.
Configure Environment Variables: Ensure all required environment variables are set on your server.
Run the Flask Application in Production Mode: Consider using gunicorn or another WSGI server.
Ensure Scheduled Tasks Run: The server must stay active to execute the scheduled tasks. Consider using a process manager like supervisord or a dedicated service like AWS Lambda for the scheduled tasks.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to open issues or submit pull requests if you find any bugs or have feature suggestions.

Acknowledgments
Flask: For providing the web framework.
PostgreSQL: For database management.
APScheduler: For scheduling tasks.
WhatsApp Business API: For enabling communication.
This README provides an overview of the application, setup instructions, and key details for deployment and usage. Feel free to adjust the content to match your project's specifics.
