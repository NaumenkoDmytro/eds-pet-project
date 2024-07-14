from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


HEADLESS_MODE = False
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_user_agent() -> str:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    return user_agent


def chrome() -> webdriver.Chrome:
    driver_service = Service(ChromeDriverManager().install())

    if HEADLESS_MODE:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument(f'user-agent={get_user_agent()}')

        driver_ = webdriver.Chrome(
            service=driver_service,
            options=options
        )
    else:
        driver_ = webdriver.Chrome(
            service=driver_service
        )
        driver_.maximize_window()

    return driver_


driver = chrome()
