# Approach:-
    # Go to gmail account and setup 2 factor Authentication.
    # Ganerate app password.
    # Create a function to send the mail.


def autoEmail(senderEmail, senderEmailPass, recieverEmail, topicOfEmail, bodyOfEmail ):
    from email.message import EmailMessage
    import ssl
    import smtplib

    # Create an instance of 'EmailMessage()' which will be used to construct the email.
    em = EmailMessage()
    em['From'] = senderEmail  # Set the 'From' field of the email
    em['To'] = recieverEmail  # Set the 'To' field of the email
    em['subject'] = topicOfEmail    # Set the 'subject' field of the email
    em.set_content(bodyOfEmail)       # Set the main content of the email

    # Create a default SSL context to establish a secure connection
    context = ssl.create_default_context()

    # Open a connection to the Gmail SMTP server using SMTP_SSL
    # 'smtp.gmail.com' is the server address, 465 is the port for SSL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(senderEmail, senderEmailPass)    # Log in to the server using the sender's email and app password
        smtp.sendmail(senderEmail, recieverEmail, em.as_string())   # Send the email.
















###########################################################################################################################################

# # Import the EmailMessage class from the email.message module
# # This class is used to create an email message object
# from email.message import EmailMessage

# # Import the ssl module to handle secure connections
# import ssl

# # # Import the smtplib module to handle the actual sending of email.
# import smtplib


# email_sender = 'Email address of sender'

# # Define the app password generated for the sender's email (used for authentication)
# email_password = '2-Factor-Authentication Password'

# email_receiver = input("Enter email address here: ")         # Enter email address here.

# subject = "# Topic of the email."
# body = """
# # Content of the email.
# """

# # Create an instance of 'EmailMessage()' which will be used to construct the email.
# em = EmailMessage()
# em['From'] = email_sender  # Set the 'From' field of the email
# em['To'] = email_receiver  # Set the 'To' field of the email
# em['subject'] = subject    # Set the 'subject' field of the email
# em.set_content(body)       # Set the main content of the email

# # Create a default SSL context to establish a secure connection
# context = ssl.create_default_context()

# # Open a connection to the Gmail SMTP server using SMTP_SSL
# # 'smtp.gmail.com' is the server address, 465 is the port for SSL
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)    # Log in to the server using the sender's email and app password
#     smtp.sendmail(email_sender, email_receiver, em.as_string())   # Send the email.