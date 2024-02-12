import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

# a new selenium browser
def open_browser() -> webdriver:
    my_options = webdriver.ChromeOptions()
    # Use custom profile
    my_options.add_argument(f'user-data-dir=Scraper')
    my_options.add_argument('--enable-javascript')
    # Prevent Selenium driven WebDriver getting detected
    # Add the argument --disable-blink-features=AutomationControlled
    my_options.add_argument('--disable-blink-features=AutomationControlled')
    # Exclude the collection of enable-automation switches
    my_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Turn-off useAutomationExtension
    my_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(service=Service("/Users/manaadvice/Documents/Python/chromedriver"), options=my_options) 

    # Change the property value of the navigator for webdriver to undefined
    # The webdriver read-only property of the navigator interface indicates whether the user agent is controlled by automation.
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})")
    
    # Rotating the user-agent through execute_cdp_cmd() command
    # Setting up Chrome/83.0.4103.53 as useragent
    # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

    return driver


# login to Seeking Alpha for premium only content
def sign_in(driver: webdriver) -> None:
    try:
        driver.find_element(By.XPATH, value='//span[text()="Sign In"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, value='//input[@name="email"]').send_keys("***"['username'])
        driver.find_element(By.XPATH, value='//input[@name="password"]').send_keys("***"['password'])
        time.sleep(3)
        driver.find_element(By.XPATH, value='//button[@data-test-id="sign-in-button"]').click()
    except NoSuchElementException:
        pass


# get all the transcripts from webpage
def get_transcripts(driver: webdriver) -> list[WebElement]:

    articles_before_scroll: list = driver.find_elements(By.TAG_NAME, value='article')
    articles_after_scroll: list = []

    while len(articles_after_scroll) != len(articles_before_scroll):
        articles_before_scroll: list = driver.find_elements(By.TAG_NAME, value='article')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        articles_after_scroll: list = driver.find_elements(By.TAG_NAME, value='article')

    return articles_after_scroll
