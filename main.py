import smtplib
from email.mime.text import MIMEText
import os
import argparse
import logging

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_imap_email(title: str, content: str, send_email: str=os.environ['EMAIL']):
    smtp = smtplib.SMTP(os.environ['SMTP_EMAIL'], int(os.environ['SMTP_PORT']))

    logging.info("SMTP Connection established")

    smtp.ehlo()
    smtp.starttls()

    logging.info("SMTP Connection secured")
    smtp.login(os.environ['EMAIL'], os.environ['SMTP_EMAIL_PASSWORD'])

    logging.info(f"SMTP {os.environ['EMAIL']} Login successful")
    msg = MIMEText(content)
    msg['Subject'] = title

    #이메일을 보내기 위한 설정(Cc도 가능)
    smtp.sendmail(os.environ['EMAIL'], send_email, msg.as_string())

    logging.info(f"Email send to {send_email}")

    #객체 닫기
    smtp.quit()
    logging.info("SMTP Connection closed")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send email using SMTP')
    parser.add_argument('--title', type=str, help='Title of the email')
    parser.add_argument('--content', type=str, help='Content of the email')
    parser.add_argument('--send_email', type=str, default= os.environ["EMAIL"] ,help='Email address to send the email to')
    args = parser.parse_args()

    send_imap_email(args.title, args.content, args.send_email)
