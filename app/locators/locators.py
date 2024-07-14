from selenium.webdriver.common.by import By

PRODUCT_TITLE = (By.CSS_SELECTOR, 'a.product-card__title')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.v-pb__cur > span.sum')

PAGINATION_LAST_PAGE = (By.CSS_SELECTOR, 'ul.pagination__list > li:last-child')
PAGINATION_NEXT_PAGE = (By.CSS_SELECTOR, 'div.pagination__next > a')
