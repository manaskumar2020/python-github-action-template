import logging
import logging.handlers
import os
import subprocess
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")
    r = requests.get('https://cat-fact.herokuapp.com/facts/')
    # Email configuration
    recipient = "manas.kumar@capgemini.com"
    subject = "Hello from Python #CGO#"
    message = "This is a test email sent from Python using mailx."

    # Construct the email body
    email_body = f"Subject: {subject}\n\n{message}"

    # Use the `subprocess` module to send the email
    try:
        p = subprocess.Popen(["mailx", "-s", subject, recipient], stdin=subprocess.PIPE)
        p.communicate(input=email_body.encode())
        p.wait()
        print("Email sent successfully")
    except Exception as e:
        print("An error occurred:", str(e))

    
    if r.status_code == 200:
        data = r.json()
        logger.info(data)
        # print(data)
        # temperature = data["forecast"]["temp"]
        logger.info(f'Weather in Berlin:')
