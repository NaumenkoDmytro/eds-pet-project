import os
import pprint
from time import sleep
from settings import driver, ROOT_DIR
from utils.utils import write_result

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from locators import locators

from database.mongo_module import get_laptops, add_laptops


def main(driver_) -> list:
    pages_num = int(driver_.find_element(*locators.PAGINATION_LAST_PAGE).text)
    i = 1
    result_lst = []

    while i <= pages_num:
        sleep(6)
        product_titles = tuple([elem.get_attribute("title")
                                for elem in driver_.find_elements(*locators.PRODUCT_TITLE)])
        product_price = tuple([elem.text
                               for elem in driver_.find_elements(*locators.PRODUCT_PRICE)])
        print(product_titles)
        print(product_price)

        result_lst.append({'titles': product_titles,
                           'prices': product_price,
                           'page_num': i})

        try:
            next_page_btn = driver.find_element(*locators.PAGINATION_NEXT_PAGE)
            actions = ActionChains(driver_)
            actions.move_to_element(next_page_btn).perform()

            # Або для того щоб прокрутити сторінку до певного елементу в селеніум є виконання JS скриптів
            # driver_.execute_script("arguments[0].scrollIntoView();", next_page_btn)
            sleep(0.5)
            next_page_btn.click()
        except Exception as e:
            print('It was last page')
            break

        i += 1
    return result_lst


if __name__ == '__main__':
    print('Parsing was started...\n\n\n')

    driver.get("https://allo.ua/ru/products/notebooks/")
    res = main(driver)
    write_result(result=res,
                 path=os.path.join(ROOT_DIR, 'results', 'result.json'))
    driver.close()

    add_laptops(res)
    print('Data from MongoDB was successfully saved.')
    pprint.pprint(get_laptops())
