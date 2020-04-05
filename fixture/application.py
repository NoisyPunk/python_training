from selenium import webdriver
from fixture.session import sessionHelper
from fixture.group import groupHelper
from fixture.user import userHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)
        self.user = userHelper(self)

    def is_valid(self):
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
