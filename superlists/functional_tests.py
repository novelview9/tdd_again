from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')

        header_text = self.browser.find_element_by_css_selector("h1").text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_css_selector("#id_new_item")
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                "input To-Do item"
        )
        
        input.send_keys(Keys.Enter)
        
        table = self.browser.find_element_by_css_selector('#id_list_table')
        rows = table.find_elements_by_css_selector('tr')
        self.assertTrue(
                any(row.text == '1: Buy the toy' for row in rows),
        )
        
        self.fail('Finish the test!!')



if __name__ == '__main__':
    unittest.main(warnings='ignore')
