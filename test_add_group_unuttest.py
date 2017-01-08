# -*- coding: utf-8 -*-
from application_unittest import ApplicationUnittest
from group import Group
import unittest



def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = ApplicationUnittest()


    def test_test_add_group(self):
        self.app.open_home_page()
        self.app.login("admin", "secret")
        self.app.open_group_page()
        self.app.create_group(Group(name="study", header="good", footer="Not friends"))
        self.app.open_group_page()
        self.app.log_out()

    def tearDown(self):
        self.app.kill()

if __name__ == '__main__':
    unittest.main()
