from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): #1

    def setUp(self): #2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self): #3
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self): #4
        #fred has heard about a cool list site on the web
        #he decides to go out and check it out
        self.browser.get('http://localhost:8000')

        #he notice the page title and header mention a to-do list
        self.assertIn('To-Do',self.browser.title) #5
        self.fail('Finish the test')#6

        #he is invited to enter a to-do item straigt away

        #he types "buy peacock feathers" into a text box (for fly fishing
        #lours)

        #when he hits enter the page updates and now the pages lists
        # "1: buy peacock feathers" as a todo list item

        #there is still a text box inviting him to add another item.
        #he enters "use feathers to make fly"

        #the page updates again, now both her list items are there

        #fred wonders what will become of his list, he notes that the 
        #url has been created that is unique to this page, and that
        #there is some explanation that says something to that effect

        #he ivsit that url - her to do list is still there

        #satisfied he turns of the computer and gets a life

if __name__ == '__main__': #7
    unittest.main(warnings='ignore') #8
