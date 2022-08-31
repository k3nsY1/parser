from selenium.webdriver import Chrome, ChromeOptions

import custom_utils.proxy as rproxy
import custom_utils.user_agent as ragent

rproxy.GetProxies()

def create_driver():
    chrome_options = ChromeOptions()  
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--remote-debugging-port=9222")
    #chrome_options.add_argument("--nogpu")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280,1280")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-logging') 
    chrome_options.add_argument("--enable-javascript")
    #chrome_options.add_argument("--disable-crash-reporter");
    #chrome_options.add_argument("--disable-in-process-stack-traces");
    chrome_options.add_argument("--disable-dev-shm-usage");
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('user-agent={0}'.format(ragent.GetRandom()))
    #chrome_options.add_argument('--proxy-server={0}'.format(rproxy.GetProxy()))
    driver = Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    
    return driver
