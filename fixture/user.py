from selenium.webdriver.support.ui import Select


class userHelper:

    def __init__(self, app):
        self.app = app

    def open_user_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, user):
        wd = self.app.wd
        self.open_user_page()
        self.paste_firstname(user)
        self.paste_middlename(user)
        self.paste_lasname(user)
        self.paste_nickname(user)
        self.paste_photo()
        self.paste_title(user)
        self.paste_company(user)
        self.paste_address(user)
        self.paste_homephone(user)
        self.paste_mobilephone(user)
        self.paste_workphone(user)
        self.paste_fax(user)
        self.paste_email()
        self.paste_email2()
        self.paste_email3()
        self.paste_homepage()
        self.paste_bday()
        self.paste_ayear()
        self.paste_address2(user)
        self.paste_phonealt(user)
        self.paste_notes(user)

        # wd.find_element_by_name("firstname").click()
        # wd.find_element_by_name("firstname").clear()
        # wd.find_element_by_name("firstname").send_keys(user.value)
        # wd.find_element_by_name("firstname").click()
        # wd.find_element_by_name("firstname").clear()
        # wd.find_element_by_name("firstname").send_keys(user.value)
        # wd.find_element_by_name("middlename").click()
        # wd.find_element_by_name("middlename").clear()
        # wd.find_element_by_name("middlename").send_keys(user.value)
        # wd.find_element_by_name("lastname").click()
        # wd.find_element_by_name("lastname").clear()
        # wd.find_element_by_name("lastname").send_keys(user.value)
        # wd.find_element_by_name("nickname").click()
        # wd.find_element_by_name("nickname").clear()
        # wd.find_element_by_name("nickname").send_keys(user.value)
        # photo = wd.find_element_by_xpath("//input[@type='file']")  # возможный вариант, проверить
        # photo.send_keys("C:\\sm.JPG")
        # wd.find_element_by_name("title").click()
        # wd.find_element_by_name("title").clear()
        # wd.find_element_by_name("title").send_keys(user.value)
        # wd.find_element_by_name("company").click()
        # wd.find_element_by_name("company").clear()
        # wd.find_element_by_name("company").send_keys(user.value)
        # wd.find_element_by_name("address").click()
        # wd.find_element_by_name("address").clear()
        # wd.find_element_by_name("address").send_keys(user.value)
        # wd.find_element_by_name("home").click()
        # wd.find_element_by_name("home").clear()
        # wd.find_element_by_name("home").send_keys(user.value)
        # wd.find_element_by_name("mobile").click()
        # wd.find_element_by_name("mobile").clear()
        # wd.find_element_by_name("mobile").send_keys(user.value)
        # wd.find_element_by_name("work").click()
        # wd.find_element_by_name("work").clear()
        # wd.find_element_by_name("work").send_keys(user.value)
        # wd.find_element_by_name("fax").click()
        # wd.find_element_by_name("fax").clear()
        # wd.find_element_by_name("fax").send_keys(user.value)
        # wd.find_element_by_name("email").click()
        # wd.find_element_by_name("email").clear()
        # wd.find_element_by_name("email").send_keys("54321@123.ru")
        # wd.find_element_by_name("email2").click()
        # wd.find_element_by_name("email2").clear()
        # wd.find_element_by_name("email2").send_keys("12345@123.ru")
        # wd.find_element_by_name("email3").click()
        # wd.find_element_by_name("email3").clear()
        # wd.find_element_by_name("email3").send_keys("135@.ru")
        # wd.find_element_by_name("homepage").click()
        # wd.find_element_by_name("homepage").clear()
        # wd.find_element_by_name("homepage").send_keys("1234567.tu")
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
        # wd.find_element_by_xpath("//option[@value='15']").click()
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text("November")
        # wd.find_element_by_xpath("//option[@value='November']").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys("1235")
        # wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text("16")
        # wd.find_element_by_xpath("(//option[@value='16'])[2]").click()
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text("October")
        # wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys("2000")
        # wd.find_element_by_name("address2").click()
        # wd.find_element_by_name("address2").clear()
        # wd.find_element_by_name("address2").send_keys(user.value)
        # wd.find_element_by_name("phone2").click()
        # wd.find_element_by_name("phone2").clear()
        # wd.find_element_by_name("phone2").send_keys(user.value)
        # wd.find_element_by_name("notes").click()
        # wd.find_element_by_name("notes").clear()
        # wd.find_element_by_name("notes").send_keys(user.value)
        self.submit_user_create()

    def submit_user_create(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def paste_notes(self, user):
        wd = self.app.wd
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(user.value)

    def paste_phonealt(self, user):
        wd = self.app.wd
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(user.value)

    def paste_address2(self, user):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(user.value)

    def paste_ayear(self):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        wd = self.app.wd
        Select(wd.find_element_by_name("aday")).select_by_visible_text("16")
        wd.find_element_by_xpath("(//option[@value='16'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("October")
        wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")

    def paste_bday(self):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
        wd.find_element_by_xpath("//option[@value='15']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("November")
        wd.find_element_by_xpath("//option[@value='November']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1235")

    def paste_homepage(self):
        wd = self.app.wd
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("1234567.tu")

    def paste_email3(self):
        wd = self.app.wd
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("135@.ru")

    def paste_email2(self):
        wd = self.app.wd
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("12345@123.ru")

    def paste_email(self):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("54321@123.ru")

    def paste_fax(self, user):
        wd = self.app.wd
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(user.value)

    def paste_workphone(self, user):
        wd = self.app.wd
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(user.value)

    def paste_mobilephone(self, user):
        wd = self.app.wd
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.value)

    def paste_homephone(self, user):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.value)

    def paste_address(self, user):
        wd = self.app.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.value)

    def paste_company(self, user):
        wd = self.app.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(user.value)

    def paste_title(self, user):
        wd = self.app.wd
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(user.value)

    def paste_photo(self):
        wd = self.app.wd
        photo = wd.find_element_by_xpath("//input[@type='file']")  # возможный вариант, проверить
        photo.send_keys("C:\\sm.JPG")

    def paste_nickname(self, user):
        wd = self.app.wd
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(user.value)

    def paste_lasname(self, user):
        wd = self.app.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.value)

    def paste_middlename(self, user):
        wd = self.app.wd
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.value)

    def paste_firstname(self, user):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.value)

    # def open_user_page(self, wd):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("add new").click()


    # def login(self, wd, username, password):
    #     wd.find_element_by_name("user").click()
    #     wd.find_element_by_name("user").send_keys(username)
    #     wd.find_element_by_id("LoginForm").click()
    #     wd.find_element_by_name("pass").click()
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_xpath("//input[@value='Login']").click()
    #
    # def open_home_page(self):
    #     wd = self.wd
    #     wd.get("http://localhost/addressbook/")
    #     return wd
