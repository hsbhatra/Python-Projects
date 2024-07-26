# autoEmail Function

## Description
The `autoEmail` function is a Python script that sends an email from a specified sender to a specified recipient using the Gmail SMTP server. It uses the `email.message.EmailMessage` class to construct the email and `smtplib.SMTP_SSL` to send the email securely.

## Requirements
- Python 3.x
- `email` module (comes with Python standard library)
- `ssl` module (comes with Python standard library)
- `smtplib` module (comes with Python standard library)

## Function Definition
```python
def autoEmail(senderEmail, senderEmailPass, recieverEmail, topicOfEmail, bodyOfEmail):
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
```

## Parameters
- `senderEmail` (str): The email address of the sender.
- `senderEmailPass` (str): The password (or app-specific password) of the sender's email account.
- `recieverEmail` (str): The email address of the recipient.
- `topicOfEmail` (str): The subject line of the email.
- `bodyOfEmail` (str): The main content of the email.

## Usage
1. **Enable Less Secure App Access or Generate an App Password**:
    - If you are using Gmail, you may need to enable "Less secure app access" or generate an app-specific password if you have 2-factor authentication enabled.
    - Instructions can be found [here](https://support.google.com/accounts/answer/185833?hl=en).

2. **Install Required Libraries**:
    - The required libraries (`email`, `ssl`, `smtplib`) are part of the Python standard library, so no additional installation is necessary.

3. **Example**:
    ```python
    sender = "your-email@gmail.com"
    sender_pass = "your-email-password"
    recipient = "recipient-email@gmail.com"
    subject = "Test Email"
    body = "This is a test email sent from a Python script."

    autoEmail(sender, sender_pass, recipient, subject, body)
    ```

4. **Run the Script**:
    - Save the `autoEmail` function in a Python file (e.g., `auto_email.py`).
    - Import and call the function with the appropriate arguments in your script.

## Security Considerations
- Avoid hardcoding your email password directly in the script.
- Use environment variables or a configuration file to store sensitive information.
- Consider using an app-specific password instead of your main email password if your email provider supports it.

## Troubleshooting
- Ensure that the sender's email and password are correct.
- Verify that the recipient's email address is valid.
- Check if your email provider requires additional settings for SMTP access (e.g., enabling less secure apps in Gmail).
- If using Gmail, ensure you have allowed "Less secure app access" or used an app password.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


This `ReadMe.md` file provides a comprehensive guide on how to use the `autoEmail` function, including the requirements, usage, and important security considerations.