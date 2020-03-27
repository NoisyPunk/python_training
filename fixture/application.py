from selenium import webdriver
from fixture.session import sessionHelper
from fixture.group import groupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)

    def open_home_page(self):
        # open homepage
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()