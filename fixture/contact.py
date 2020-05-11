from selenium.webdriver.support.ui import Select

from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text

                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")

        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)


    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)



# class userHelper:
#
#     def __init__(self, app):
#         self.app = app
#
#     def open_create_user_page(self):
#         wd = self.app.wd
#         wd.find_element_by_link_text("add new").click()
#
#     def open_user_page(self):
#         wd = self.app.wd
#         wd.find_element_by_link_text("home").click()
#
#
#     def create(self, user):
#         self.open_create_user_page()
#         self.paste_firstname(user)
#         self.paste_middlename(user)
#         self.paste_lasname(user)
#         self.paste_nickname(user)
#         self.paste_photo()
#         self.paste_title(user)
#         self.paste_company(user)
#         self.paste_address(user)
#         self.paste_homephone(user)
#         self.paste_mobilephone(user)
#         self.paste_workphone(user)
#         self.paste_fax(user)
#         self.paste_email()
#         self.paste_email2()
#         self.paste_email3()
#         self.paste_homepage()
#         self.paste_bday()
#         self.paste_ayear()
#         self.paste_address2(user)
#         self.paste_phonealt(user)
#         self.paste_notes(user)
#         self.submit_user_create()
#
#     def delete_first_user(self):
#         wd = self.app.wd
#         self.open_user_page()
#         wd.find_element_by_name("selected[]").click()
#         wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
#         wd.switch_to_alert().accept()
#         wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()
#
#
#     def submit_user_create(self):
#         wd = self.app.wd
#         wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
#
#     def paste_notes(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("notes").click()
#         wd.find_element_by_name("notes").clear()
#         wd.find_element_by_name("notes").send_keys(user.value)
#
#     def paste_phonealt(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("phone2").click()
#         wd.find_element_by_name("phone2").clear()
#         wd.find_element_by_name("phone2").send_keys(user.value)
#
#     def paste_address2(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("address2").click()
#         wd.find_element_by_name("address2").clear()
#         wd.find_element_by_name("address2").send_keys(user.value)
#
#     def paste_ayear(self):
#         wd = self.app.wd
#         wd.find_element_by_name("aday").click()
#         wd = self.app.wd
#         Select(wd.find_element_by_name("aday")).select_by_visible_text("16")
#         wd.find_element_by_xpath("(//option[@value='16'])[2]").click()
#         wd.find_element_by_name("amonth").click()
#         Select(wd.find_element_by_name("amonth")).select_by_visible_text("October")
#         wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
#         wd.find_element_by_name("ayear").click()
#         wd.find_element_by_name("ayear").clear()
#         wd.find_element_by_name("ayear").send_keys("2000")
#
#     def paste_bday(self):
#         wd = self.app.wd
#         wd.find_element_by_name("bday").click()
#         Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
#         wd.find_element_by_xpath("//option[@value='15']").click()
#         wd.find_element_by_name("bmonth").click()
#         Select(wd.find_element_by_name("bmonth")).select_by_visible_text("November")
#         wd.find_element_by_xpath("//option[@value='November']").click()
#         wd.find_element_by_name("byear").click()
#         wd.find_element_by_name("byear").clear()
#         wd.find_element_by_name("byear").send_keys("1235")
#
#     def paste_homepage(self):
#         wd = self.app.wd
#         wd.find_element_by_name("homepage").click()
#         wd.find_element_by_name("homepage").clear()
#         wd.find_element_by_name("homepage").send_keys("1234567.tu")
#
#     def paste_email3(self):
#         wd = self.app.wd
#         wd.find_element_by_name("email3").click()
#         wd.find_element_by_name("email3").clear()
#         wd.find_element_by_name("email3").send_keys("135@.ru")
#
#     def paste_email2(self):
#         wd = self.app.wd
#         wd.find_element_by_name("email2").click()
#         wd.find_element_by_name("email2").clear()
#         wd.find_element_by_name("email2").send_keys("12345@123.ru")
#
#     def paste_email(self):
#         wd = self.app.wd
#         wd.find_element_by_name("email").click()
#         wd.find_element_by_name("email").clear()
#         wd.find_element_by_name("email").send_keys("54321@123.ru")
#
#     def paste_fax(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("fax").click()
#         wd.find_element_by_name("fax").clear()
#         wd.find_element_by_name("fax").send_keys(user.value)
#
#     def paste_workphone(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("work").click()
#         wd.find_element_by_name("work").clear()
#         wd.find_element_by_name("work").send_keys(user.value)
#
#     def paste_mobilephone(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("mobile").click()
#         wd.find_element_by_name("mobile").clear()
#         wd.find_element_by_name("mobile").send_keys(user.value)
#
#     def paste_homephone(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("home").click()
#         wd.find_element_by_name("home").clear()
#         wd.find_element_by_name("home").send_keys(user.value)
#
#     def paste_address(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("address").click()
#         wd.find_element_by_name("address").clear()
#         wd.find_element_by_name("address").send_keys(user.value)
#
#     def paste_company(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("company").click()
#         wd.find_element_by_name("company").clear()
#         wd.find_element_by_name("company").send_keys(user.value)
#
#     def paste_title(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("title").click()
#         wd.find_element_by_name("title").clear()
#         wd.find_element_by_name("title").send_keys(user.value)
#
#     def paste_photo(self):
#         wd = self.app.wd
#         photo = wd.find_element_by_xpath("//input[@type='file']")  # возможный вариант, проверить
#         photo.send_keys("C:\\sm.JPG")
#
#     def paste_nickname(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("nickname").click()
#         wd.find_element_by_name("nickname").clear()
#         wd.find_element_by_name("nickname").send_keys(user.value)
#
#     def paste_lasname(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("lastname").click()
#         wd.find_element_by_name("lastname").clear()
#         wd.find_element_by_name("lastname").send_keys(user.value)
#
#     def paste_middlename(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("middlename").click()
#         wd.find_element_by_name("middlename").clear()
#         wd.find_element_by_name("middlename").send_keys(user.value)
#
#     def paste_firstname(self, user):
#         wd = self.app.wd
#         wd.find_element_by_name("firstname").click()
#         wd.find_element_by_name("firstname").clear()
#         wd.find_element_by_name("firstname").send_keys(user.value)

