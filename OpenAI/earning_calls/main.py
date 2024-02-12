import requests
from bs4 import BeautifulSoup

from scraper import Scraper
from motley_fool import MothleyFool

# BASE_URL = "https://seekingalpha.com"
# URL = "https://seekingalpha.com/earnings/earnings-call-transcripts"
# LOGIN_URL = 'https://seekingalpha.com/api/v3/login_tokens'

# email = "******@*****"
# password = "******"


# client = requests.Session()
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find_all("article")

# for earning_call_article in results[:1]:
#     article = earning_call_article.find("h3").find("a", href=True)
#     print(article['href'], end="\n"*2)
#     article_url = BASE_URL + article['href']
#     article_page = requests.get(URL)
#     with open("response.txt", "w") as file:
#         file.write(article_page.text)

# driver = webdriver.Chrome(service=Service("/Users/manaadvice/Documents/Python/chromedriver"))
# scraper = Scraper() 
# scraper.driver.get("http://www.python.org")
# scraper.driver.implicitly_wait(5)

# # time.sleep(5) 

# print(scraper.driver.title)
# # elem = scraper.driver.find_element(By.NAME, "q")
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)

# scraper.driver.close()

mf = MothleyFool()
mf.get_earnings_calls()