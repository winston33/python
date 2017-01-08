# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.group import GroupHelper
import unittest




def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add(unittest.TestCase):
    def setUp(self):

        binary = FirefoxBinary(r'c:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        self.wd = WebDriver(firefox_binary=binary)
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def test_add(self):
        success = True
        wd = self.wd
        wd.get("http://localhost:8070/addressbook/group.php")
        wd.find_element_by_xpath("//div[@id='content']//form[normalize-space(.)='study']").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("ww")
        wd.find_element_by_xpath("//div[@id='content']/form").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("w")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
