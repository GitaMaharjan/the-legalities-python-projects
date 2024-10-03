# 34.  Basic Command-line Email Client   
#     *Description*: Develop a simple email client that can send and receive emails from the command line.  
#     *Skills*: Networking, SMTP, email handling.

import smtplib  # For sending emails using SMTP
import imaplib  # For receiving emails using IMAP
import email  # To handle the structure of emails
from email.mime.text import MIMEText  # To create the text for email
from email.mime.multipart import MIMEMultipart  # To create email with multiple parts
from email.header import decode_header  # To decode email headers
import re  # For validating email format

def is_valid_email(email_address):

    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email_address) is not None

def send_email(sender_email, sender_password, recipient_email, subject, body):

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email  # Set sender email
    msg['To'] = recipient_email  # Set recipient email
    msg['Subject'] = subject  # Set email subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server on port 587 for TLS encryption
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption for secure connection
        server.login(sender_email, sender_password)  # Log into your email account

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Failed to send email: Invalid username or password.")
    except Exception as e:
        print(f"Failed to send email: {e}")  
    
    finally:
        # Close the server connection
        server.quit()

def read_email(email_user, email_password):

    # Connect to the IMAP server (Gmail IMAP server)
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_user, email_password)  # Log into your email account
    except imaplib.IMAP4.error:
        print("Failed to login: Invalid email or password.")
        return

    # Select the mailbox (inbox) to fetch emails from
    mail.select("inbox")

    # Search for all emails in the inbox
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()  # Get list of email IDs

    if not email_ids:
        print("No emails found in the inbox.")
        mail.logout()
        return

    # Fetch the latest email
    latest_email_id = email_ids[-1]  # Get the most recent email ID
    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")  # Fetch the email data
    
    # Parse the email content
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            # Get the email object from the raw data
            msg = email.message_from_bytes(response_part[1])

            # Decode the email subject (in case it's encoded)
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")

            print(f"Subject: {subject}")  # Print the email subject

            # Check if the email is multipart (contains attachments or multiple parts)
            if msg.is_multipart():
                for part in msg.walk():
                    # Get the email content that is plain text
                    if part.get_content_type() == "text/plain":
                        print(part.get_payload(decode=True).decode("utf-8"))
            else:
                # If it's not multipart, just print the plain text content
                print(msg.get_payload(decode=True).decode("utf-8"))

    # Logout and close the connection
    mail.logout()

def main():
    while True:
        # Display menu options
        print("1. Send an Email")
        print("2. Read Latest Email")
        print("3. Exit")
        choice = input("Choose an option: ")  # Get user input for selection

        if choice == '1':
            # Sending an email
            sender = input("Enter your email: ")
            if not is_valid_email(sender):
                print("Invalid email format.")
                continue
            
            password = input("Enter your password: ")
            recipient = input("Enter recipient email: ")
            if not is_valid_email(recipient):
                print("Invalid recipient email format.")
                continue
            
            subject = input("Enter subject: ")
            body = input("Enter message: ")
            send_email(sender, password, recipient, subject, body)

        elif choice == '2':
            # Reading the latest email
            email_user = input("Enter your email: ")
            if not is_valid_email(email_user):
                print("Invalid email format.")
                continue
            
            email_password = input("Enter your password: ")
            read_email(email_user, email_password)

        elif choice == '3':
            # Exit the program
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()  # Call the main function to start the program
