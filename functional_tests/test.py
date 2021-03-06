from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
from django.contrib.staticfiles.testing import StaticLiveServerCase

class NewVisitorTest(StaticLiveServerCase): #1

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()
    
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
        self.browser.get(self.server_url)

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
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #there is still a text box inviting him to add another item.
        #he enters "use feathers to make fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #the page updates again, now both her list items are there
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        #time.sleep(5)
        #self.fail('Finish the test!')
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        #ted visits the website, there is no sign of freds list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #ted starts a new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #ted gets his own unique url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        #again there is no trace of ediths list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('Buy milk',page_text)

        #satisfied they go back to sleep
        
        #fred wonders what will become of his list, he notes that the 
        #url has been created that is unique to this page, and that
        #there is some explanation that says something to that effect

        #he ivsit that url - her to do list is still there

        #satisfied he turns of the computer and gets a life

    def test_layout_and_styling(self):
        #edit goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        #She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=5)

        #She notices the input box is nicely centered
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=5)


