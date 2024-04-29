import argparse
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender, password, receiver, content_file, subject, attachment_file=None):
    # Check if content file path is valid
    if not os.path.isfile(content_file):
        print('Error: Invalid content file path.')
        return

    # Read HTML content from file
    with open(content_file, 'r') as file:
        html_content = file.read()

    # Set up SMTP server details for Outlook
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587

    # Create message container (MIMEMultipart)
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    # Attach HTML body to the message
    msg.attach(MIMEText(html_content, 'html'))

    # Attach file as attachment if provided
    if attachment_file:
        # Check if attachment file path is valid
        if not os.path.isfile(attachment_file):
            print('Error: Invalid attachment file path.')
            return

        # Open and read the attachment file
        with open(attachment_file, 'rb') as attachment:
            # Create MIMEBase object
            attachment_part = MIMEBase('application', 'octet-stream')
            attachment_part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(attachment_part)

        # Add header as key/value pair to attachment part
        attachment_part.add_header(
            'Content-Disposition',
            f'attachment; filename= {os.path.basename(attachment_file)}'
        )

        # Add attachment to message
        msg.attach(attachment_part)

    # Create SMTP session for sending the mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS for security
        server.login(sender, password)  # Login to SMTP server
        text = msg.as_string()
        server.sendmail(sender, receiver, text)  # Send the email
        print('Email sent successfully!')
    except Exception as e:
        print('Error: Unable to send email.')
        print(e)
    finally:
        server.quit()  # Terminate the SMTP session

if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description='Send an email from Outlook to Gmail.')
    parser.add_argument('-s', '--sender', required=True, help='Sender\'s email address (Outlook)')
    parser.add_argument('-p', '--password', required=True, help='Sender\'s email password (Outlook)')
    parser.add_argument('-r', '--receiver', required=True, help='Recipient\'s email address (Gmail)')
    parser.add_argument('-c', '--content', required=True, help='Path to HTML content file')
    parser.add_argument('-subj', '--subject', required=True, help='Email subject')
    parser.add_argument('-a', '--attachment', help='Path to attachment file')
    args = parser.parse_args()

    # Send the email
    send_email(args.sender, args.password, args.receiver, args.content, args.subject, args.attachment)
