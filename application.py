
class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        # open homepage
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def login(self, username, password):
        # login
        wd = self.wd
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_group_page(self):
        # Open group page
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        # Create group
        wd = self.wd
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
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def return_group_page(self):
        # return group page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()