import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def caesar_encrypt(password):
    """
    Purpose: Encrypt the password given to the
    parameter using the caesar method. After encryption
    write the encryption to the file

    Return: Nothing
    """
    pass


def caesar_decrypt(password, shift):
    """
    Purpose: Decrypt the encrypted caesar password.
    This will read from the 

    Return:
    """
    pass


def main():

    # Variables
    address = "test.accout1.python@gmail.com"
    email_subject = "Test Run"

    # Read the message to be sent over email.
    with open("message.txt", "r") as f:
        body_text = f.read()


    # Get the password from a txt file and save it
    # to a password variable.
    with open("password.txt", "r") as g:
        password = g.read()

    # This section will be used to get the header part of the email.
    # This includes:
        # From
        # To
        # Subject
        # Body

    msg = MIMEMultipart()
    msg['From'] = address
    msg['To'] = address
    msg['Subject'] = email_subject

    # attatchs it to msg object
    msg.attach(MIMEText(body_text, "plain"))

    # Port number (587) with SSL port numbers (587) with TSL
    # Server parameters --> Host            Port
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Start process
    server.starttls()

    # Set msg to a string
    text = msg.as_string()

    # Log into the account. Need email and password
    try:
        server.login(address, password)
        print("Logged In")
        
        # Send mail
        server.sendmail(address, address, text)
        print("Email was sent!")

    except smtplib.SMTPAuthenticationError:
        print("Unable to sign in")

    server.quit()


if __name__ == "__main__":
    main()
