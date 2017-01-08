"""from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class ApplicationUnittest:

    def __init__(self):
        binary = FirefoxBinary(r'c:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        self.wd = WebDriver(firefox_binary=binary)
        self.wd.implicitly_wait(20)

    def create_group(self, group):
        wd = self.wd
        wd.get_screenshot_as_file("screenshot.png")
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
        wd.find_element_by_name("submit").click()

    def log_out(self):
        wd = self.wd
        wd.find_element_by_link_text("Выйти").click()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Группы").click()

    def login(self, name, password):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8070/addressbook/")

    def kill(self):
        wd = self.wd
        wd.quit()

