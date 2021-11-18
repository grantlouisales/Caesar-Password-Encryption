import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def get_password_for_account():
    """
    Purpose: Read the account password from a 
    .txt file.

    Return: Password read from the .txt file.
    """
    with open("passwordfortestaccount.txt", "r") as f:
        password = f.read()

    return password


def caesar_encrypt(password, shift):
    """
    Purpose: Encrypt the password given to the
    parameter using the caesar method. After encryption
    write the encryption to the file. We do this encryption
    by using ASCII.

    Return: Nothing
    """
    encrypted_password = ""

    # Loop through the password by each character
    for character in password:
        value = ord(character) + shift
        encrypted_password += chr(value % 128)

    with open("password.txt", "w") as f:
        f.write(encrypted_password)


def caesar_decrypt(shift):
    """
    Purpose: Decrypt the encrypted caesar password.
    This will read from the 

    Return: decrypted password
    """
    with open("password.txt", "r") as f:
        password = f.read()

    decrypted_password = ""

    for character in password:
        value = ord(character) - shift
        decrypted_password += chr(value % 128)
    return decrypted_password


def get_body_text():
    """
    Purpose: Read the messages.txt file.

    Return: Returns the body text for the email.
    """
    with open("message.txt", "r") as f:
        body_text = f.read()
    
    return body_text


def main():

    # Variables
    address = "test.accout1.python@gmail.com"
    email_subject = "Test Run"
    body_text = get_body_text()
    shift = 8
    account_password = get_password_for_account()

    # Encrypt the password and put it in the txt file.
    caesar_encrypt(account_password, shift)

    # Decrypt the password from the txt file.
    password = caesar_decrypt(shift)

    # This section will be used to get the header part of the email.
    # This includes:
        # From
        # To
        # Subject
    msg = MIMEMultipart()
    msg['From'] = address
    msg['To'] = address
    msg['Subject'] = email_subject

    # attatchs it to msg object
    msg.attach(MIMEText(body_text, "plain"))

    # Port number (465) with SSL port numbers (587) with TSL
    # Since we are using TSL the port will be (587)
    # Server parameters --> Host            Port
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Start process
    server.starttls()

    # Set msg to a string
    text = msg.as_string()


    try:
        # Log in to the email 
        server.login(address, password)
        print("Logged In")
        
        # Send mail
        server.sendmail(address, address, text)
        print("Email was sent!")

    except smtplib.SMTPAuthenticationError:
        print("Unable to sign in")

    # End the server
    server.quit()


if __name__ == "__main__":
    main()
