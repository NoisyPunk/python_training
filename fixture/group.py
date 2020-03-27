class groupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        # Open group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        # Create group
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group_create()
        self.return_group_page()

    def submit_group_create(self):
        # submit group creation
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_group_page(self):
        # return group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
