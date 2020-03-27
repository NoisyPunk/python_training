# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


class TestAddGroup(unittest.TestCase):


    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        # open homepage
        self.app = Application()
        # wd = self.wd
        # wd.get("http://localhost/addressbook/group.php")

    # def login(self, username, password):
    #     # login
    #     wd = self.wd
    #     self.open_home_page(wd)
    #     wd.find_element_by_name("user").click()
    #     wd.find_element_by_name("user").clear()
    #     wd.find_element_by_name("user").send_keys(username)
    #     wd.find_element_by_id("LoginForm").click()
    #     wd.find_element_by_name("pass").click()
    #     wd.find_element_by_name("pass").clear()
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_xpath("//input[@value='Login']").click()
    #
    # def open_group_page(self):
    #     # Open group page
    #     wd = self.wd
    #     wd.find_element_by_link_text("groups").click()
    #
    # def create_group(self, group):
    #     # Create group
    #     wd = self.wd
    #     self.open_group_page()
    #     wd.find_element_by_name("new").click()
    #     wd.find_element_by_name("group_name").click()
    #     wd.find_element_by_name("group_name").clear()
    #     wd.find_element_by_name("group_name").send_keys(group.name)
    #     wd.find_element_by_name("group_header").click()
    #     wd.find_element_by_name("group_header").clear()
    #     wd.find_element_by_name("group_header").send_keys(group.header)
    #     wd.find_element_by_name("group_footer").click()
    #     wd.find_element_by_name("group_footer").clear()
    #     wd.find_element_by_name("group_footer").send_keys(group.footer)
    #     self.submit_group_create()
    #     self.return_group_page()
    #
    # def submit_group_create(self):
    #     # submit group creation
    #     wd = self.wd
    #     wd.find_element_by_name("submit").click()
    #
    # def return_group_page(self):
    #     # return group page
    #     wd = self.wd
    #     wd.find_element_by_link_text("group page").click()
    #
    # def logout(self):
    #     # logout
    #     wd = self.wd
    #     wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="dfre", header="dfre", footer='123'))
        self.app.logout()


    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=''))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
