from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        binary = FirefoxBinary(r'c:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        self.wd = WebDriver(firefox_binary=binary)
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8070/addressbook/")




    def destroy(self):
        wd = self.wd
        wd.quit()

