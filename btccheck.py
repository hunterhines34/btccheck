import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass


def send_email():
    # Create email instance
    message = MIMEMultipart()
    password = user_password

    # Define the email parameters
    message['From'] = email
    message['To'] = send_email_to
    message['Subject'] = "Bitcoin price alert"

    # Create the email message content
    email_msg = "Dear Hunter, \n\nThe current Bitcoin price is $" + str(bitcoin_rate)

    # Adds the message from above
    message.attach(MIMEText(message, 'plain'))

    # Create the Gmail server connection
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    # Login to the email instance
    server.login(message['From'], password)

    # Send the message
    server.sendmail(message['From'], message['To'], email_msg)

    # Close the Gmail server instance
    server.quit()

    # Print output to the end-user
    print('Successfully sent email to %s:' % (message['To']))
    print('Current price of Bitcoin was: ' + str(bitcoin_rate))


# Get user inputs
name = input('Enter your name: ')
email = input('Enter your email (Gmail only): ')
user_password = getpass.getpass()
send_email_to = input('Enter the email you want to send to: ')
alert_amount = input('Send email if Bitcoin price falls below: ')

# Gather data from API
while True:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url, headers={"Accept: " "applications/json"}, )
    data = response.json()
    bpi = data['bpi']
    USD = bpi['USD']
    bitcoin_rate = int(USD['rate_float'])

    if bitcoin_rate < int(alert_amount):
        send_email()
        print('This program will check for prices again in 3 minutes. Ctrl + C to quit.')
        time.sleep(180)
    else:
        time.sleep(300)
        print('The current price is: ' + str(
            bitcoin_rate) + '.\nThis program will check for prices again in 5 minutes. Ctrl + C to quit.')
