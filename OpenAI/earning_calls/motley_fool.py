from scraper import Scraper
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class MothleyFool(Scraper):
    URL = "https://www.fool.com/earnings-call-transcripts/"

    def __init__(self) -> None:
        super().__init__()
        

    def get_earnings_calls(self):
        self.driver.get(self.URL)
        print(self.driver.title)
        articles = self.driver.find_elements(By.CSS_SELECTOR, "#aggregator-article-container div.page a")
        for article in articles:
            href = article.get_attribute("href")
            
            print(href, article.text, 2*"/n")
        
        
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)

    def close(self):
        self.driver.close()

