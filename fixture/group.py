class groupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        # Open group page
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[3]/a").click()

    def create(self, group):
        # Create group
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        self.submit_group_create()
        self.return_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

        # wd.find_element_by_name("group_header").click()
        # wd.find_element_by_name("group_header").clear()
        # wd.find_element_by_name("group_header").send_keys(group.header)
        # wd.find_element_by_name("group_footer").click()
        # wd.find_element_by_name("group_footer").clear()
        # wd.find_element_by_name("group_footer").send_keys(group.footer)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def submit_group_create(self):
        # submit group creation
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open modif group
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modify
        wd.find_element_by_name("Update").click()

        self.return_group_page()


        # wd.find_element_by_xpath("/html/body/div/div[4]/form/input[3]").click()
        # wd.find_element_by_xpath("/html/body/div/div[4]/form/input[2]").clear()
        # wd.find_element_by_xpath("/html/body/div/div[4]/form/input[2]").send_keys(group.name)
        # wd.find_element_by_xpath("/html/body/div/div[4]/form/input[3]").click()
        # wd.find_element_by_xpath("/html/body/div/div[4]/div/i/a").click()


    def return_group_page(self):
        # return group page
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[3]/a").click()
