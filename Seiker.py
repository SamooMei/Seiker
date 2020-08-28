from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from copy import deepcopy
import requests
import smtplib
import json
import time
import os


class Seiker:
    def __init__(self, USER, PASS):
        if not isinstance(USER, str) and not isinstance(PASS, str):
            print("Credentials are invalid")
            return
        self.USER = USER
        self.PASS = PASS
        self.current, self.recent = [], []
        self.landing = "https://elwiki.net/babel/"
        # Mailing Addresses
        addresses = open("addresses.json")
        self.addresses = json.load(addresses)

    def getSoup(self, link):
        # Fetches the html source and returns it as a BeautifulSoup object
        page_source = requests.get(link).text
        return BeautifulSoup(page_source, "html.parser")

    def sendMail(self, subject, message):
        # Compiles the message into a MIMEText and sends it through smtp
        try:
            mail = MIMEText(message, "html")
            mail["From"] = self.USER
            mail["To"] = ", ".join(self.addresses)
            mail["Subject"] = subject

            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            server.starttls()
            server.login(self.USER, self.PASS)
            server.sendmail(self.USER, self.addresses.get(
                "goons"), mail.as_string())
            server.quit()
            print("Success")
        except:
            print("Failure")
            return

    def compare(self):
        # Uses the sidebar to retrieve the 5 latest posts on Babel
        soup = self.getSoup(self.landing)
        articles = soup.find(id="sidebar").find_all("a")
        for article in articles:
            self.current.append((article.get_text(), article.get("href")))
        if not self.recent:
            self.recent = deepcopy(self.current)
        # Compares the newest articles of Babel to the last known ones
        if self.current != self.recent:
            # Gets the main info of the newest article
            message = self.getSoup(self.current[0][1]).find(class_="entry")
            self.sendMail(self.current[0][0], str(message))
            self.recent = deepcopy(self.current)
        self.current.clear()


def run():
    # Checks Babel every 5 minutes
    print("Ready Perfectly")
    while True:
        SeikerPy.compare()
        time.sleep(300)


if __name__ == "__main__":
    SeikerPy = Seiker(os.environ['USER'], os.environ['PASS'])
    run()
