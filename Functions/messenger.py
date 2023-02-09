from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib, ssl, os




class Messenger:

    def __init__(self, message: str, service: str):
        self.message = message
        self.service = service 

    def send_mail(self):
        load_dotenv()
        
        EMAIL = os.environ.get("EMAIL")
        PASSWORD = os.environ.get("PASSWORD")

        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP("smtp.office365.com", 587)
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)

            message = self.message

            msg = MIMEMultipart()
            msg['From'] = EMAIL
            msg['To'] = EMAIL
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = f"Error in service {self.service}"

            msg.attach(MIMEText(message, "plain"))

            server.sendmail(EMAIL, EMAIL, msg.as_string() )
            server.quit()
            return True
        except:
            return "Connection refused by the host."
