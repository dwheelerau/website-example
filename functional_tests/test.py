from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase): #1

    def setUp(self): #2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self): #3
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self): #4
        #fred has heard about a cool list site on the web
        #he decides to go out and check it out
        self.browser.get(self.live_server_url)

        #he notice the page title and header mention a to-do list
        self.assertIn('To-Do',self.browser.title) #5
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #he is invited to enter a to-do item straigt away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
            'Enter a to-do item')


        #he types "buy peacock feathers" into a text box (for fly fishing
        #lours)
        inputbox.send_keys('Buy peacock feathers')

        #when he hits enter the page updates and now the pages lists
        # "1: buy peacock feathers" as a todo list item
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #there is still a text box inviting him to add another item.
        #he enters "use feathers to make fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #the page updates again, now both her list items are there
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        time.sleep(5)
        self.fail('Finish the test!')

        #fred wonders what will become of his list, he notes that the 
        #url has been created that is unique to this page, and that
        #there is some explanation that says something to that effect

        #he ivsit that url - her to do list is still there

        #satisfied he turns of the computer and gets a life

