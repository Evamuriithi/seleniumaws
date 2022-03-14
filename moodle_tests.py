import unittest
import moodle_locators as locators
import moodle_methods as methods

class MoodleAppPostiveTestCases(unittest.TestCase):

    @staticmethod # signal to unittest that this is a function inside class (vs @classmethod)
    def test_create_new_user(): # test_in the name is mandotory
        methods.setUp()
        methods.log_in(locators.admin_username, locators.admin_password)
        methods.create_new_user()
        methods.search_user()
        methods.log_out()
        methods.log_in(locators.new_username,locators.new_password)
        methods.check_new_user_can_login()
        methods.log_out()
        methods.log_in(locators.admin_username, locators.admin_password)
        methods.delete_user()
        methods.log_out()
        methods.tearDown()
# setUp()
# log_in(locators.admin_username, locators.admin_password)
# create_new_user()
# search_user()
# log_out()
# log_in(locators.new_username, locators.new_password)
# check_new_user_can_login()
# log_out()
# log_in(locators.admin_username, locators.admin_password)
# delete_user()
# log_out()
# tearDown()
