from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Scraper():
    def __init__(self) -> None:

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

        self.driver = webdriver.Chrome(service=Service("/Users/manaadvice/Documents/Python/chromedriver"), options=my_options) 

        # Change the property value of the navigator for webdriver to undefined
        # The webdriver read-only property of the navigator interface indicates whether the user agent is controlled by automation.
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})")
        
        # Rotating the user-agent through execute_cdp_cmd() command
        # Setting up Chrome/83.0.4103.53 as useragent
        # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

        