from linkedin_scraper import actions
from my_person import MyPerson
from selenium import webdriver

driver = webdriver.Firefox()

email = "alicand96@gmail.com"
password = "secret1234"
actions.login(driver, email, password)  # if email and password isnt given, it'll prompt in terminal
person = MyPerson("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver, get=False,
                  close_on_complete=False)
print(person)
