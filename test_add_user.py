# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from user import User


class UntitledTestCase(unittest.TestCase):


    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.open_home_page()
        self.login(wd, username='admin', password='secret')
        self.add_group(wd)
        self.paste_firstname(wd, User(value='54321'))
        self.paste_middlename(wd, User(value='54321'))
        self.paste_lasname(wd, User(value='54321'))
        self.paste_nickname(wd, User(value='54321'))
        self.paste_photo(wd)
        self.paste_title(wd, User(value='54321'))
        self.paste_company(wd, User(value='54321'))
        self.paste_address(wd, User(value='54321'))
        self.paste_homephone(wd, User(value='54321'))
        self.paste_mobilephone(wd, User(value='54321'))
        self.paste_workphone(wd, User(value='54321'))
        self.paste_fax(wd, User(value='54321'))
        self.paste_email(wd)
        self.paste_email2(wd)
        self.paste_email3(wd)
        self.paste_homepage(wd)
        self.paste_bday(wd)
        self.paste_ayear(wd)
        self.paste_address2(wd, User(value='54321'))
        self.paste_phonealt(wd, User(value='54321'))
        self.paste_notes(wd, User(value='54321'))
        self.submit(wd)
        self.goHomepage(wd)

    def goHomepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def submit(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def paste_notes(self, wd, user):
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(user.value)

    def paste_phonealt(self, wd, user):
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(user.value)

    def paste_address2(self, wd, user):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(user.value)

    def paste_ayear(self, wd):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("16")
        wd.find_element_by_xpath("(//option[@value='16'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("October")
        wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")

    def paste_bday(self, wd):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
        wd.find_element_by_xpath("//option[@value='15']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("November")
        wd.find_element_by_xpath("//option[@value='November']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1235")

    def paste_homepage(self, wd):
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("1234567.tu")

    def paste_email3(self, wd):
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("135@.ru")

    def paste_email2(self, wd):
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("12345@123.ru")

    def paste_email(self, wd):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("54321@123.ru")

    def paste_fax(self, wd, user):
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(user.value)

    def paste_workphone(self, wd, user):
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(user.value)

    def paste_mobilephone(self, wd, user):
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.value)

    def paste_homephone(self, wd, user):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.value)

    def paste_address(self, wd, user):
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.value)

    def paste_company(self, wd, user):
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(user.value)

    def paste_title(self, wd, user):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(user.value)

    def paste_photo(self, wd):
        photo = wd.find_element_by_xpath("//input[@type='file']")  # возможный вариант, проверить
        photo.send_keys("C:\\sm.JPG")

    def paste_nickname(self, wd, user):
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(user.value)

    def paste_lasname(self, wd, user):
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.value)

    def paste_middlename(self, wd, user):
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.value)

    def paste_firstname(self, wd, user):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.value)

    def add_group(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        return wd

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
