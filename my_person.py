import time

from linkedin_scraper import Person
from pynput.keyboard import Key, Controller

keyboard = Controller()


class MyPerson(Person):
    def scrape(self, close_on_complete=True):
        if self.is_signed_in():
            self.get_connections(close_on_complete=close_on_complete)
        else:
            self.scrape_not_logged_in(close_on_complete=close_on_complete)

    def get_connections(self, close_on_complete=True):
        driver = self.driver

        # Go to connections
        driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')

        # Enter loop
        # while True:
        # Press Home

        keyboard.press(Key.home)
        keyboard.release(Key.home)

        driver.execute_script('console.log(window.scrollY)')

        # Wait 2 seconds
        time.sleep(2)

        # Press End
        keyboard.press(Key.end)
        keyboard.release(Key.end)

        driver.execute_script('console.log(window.scrollY)')

        # Wait 10 seconds
        time.sleep(10)

        print('hey')

        if close_on_complete:
            driver.quit()
