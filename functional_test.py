from selenium import webdriver

browser = webdriver.Firefox()

#fred has heard about a cool list site on the web
#he decides to go out and check it out
browser.get('http://localhost:8000')

#he notice the page title and header mention a to-do list
assert 'To-Do' in browser.title

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
