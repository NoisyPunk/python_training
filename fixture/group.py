from model.group import Group

class groupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        # Open group page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click() # проверка чтобы не было лишних переходов на страницу

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
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
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

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open modif group
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modify
        wd.find_element_by_name("update").click()
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


    def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups