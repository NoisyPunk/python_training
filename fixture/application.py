from selenium import webdriver
from fixture.session import sessionHelper
from fixture.group import groupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser="firefox"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd = webdriver.Firefox()
        # self.wd.implicitly_wait(5)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        wd = self.wd
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        # open homepage
        wd = self.wd
        # wd.get("http://172.26.66.34/addressbook")
        wd.get("http://127.0.0.1/addressbook")


    def destroy(self):
        self.wd.quit()
