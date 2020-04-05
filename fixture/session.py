import time

class sessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # login
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def logout(self):
        # logout
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("Logout").click()
        # wd.find_element_by_xpath("/html/body/div/div[1]/form/a").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_loged_in():
            time.sleep(5)
            if self.is_loged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_loged_in():
            self.logout()

    def is_loged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_loged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("/html/body/div/div[1]/form/b").text == '('+username+')'
        # t = wd.find_element_by_xpath("/html/body/div/div[1]/form/b").text
        # print(t)



