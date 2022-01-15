# import necessary packages
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to read the contacts from a given contact file and return a
# list of names and email addresses
class sendMail():
    def get_contacts(filename):
        names = []
        emails = []
        with open(filename, mode='r', encoding='utf-8') as contacts_file:
            for a_contact in contacts_file:
                names.append(a_contact.split()[0])
                emails.append(a_contact.split()[1])
        return names, emails

    # to read message template
    def read_template(filename):
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    # set up the SMTP server
    serverSMTP = smtplib.SMTP(host='smtp.gmail.com', port=587)
    serverSMTP.starttls()
    serverSMTP.login('2018.aman.singh@ves.ac.in', 'wnptzbactskrdnwl')   
    #password = 'wnptzbactskrdnwl' is google application/app password found on this link https://myaccount.google.com/security



    names, emails = get_contacts('src\sendMail\mycontacts.txt')  # read contacts
    #message_template = read_template('message.txt') # read template

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        #message = message_template.substitute(PERSON_NAME=name.title())
        message = "http://192.168.0.103:5000"

        # setup the parameters of the message
        msg['From']="2018.aman.singh@ves.ac.in"
        msg['To']=email
        msg['Subject']="This is TEST"

        # add in the message body
        msg.attach(MIMEText(message))

        # send the message via the server set up earlier.
        serverSMTP.send_message(msg)
        
        del msg