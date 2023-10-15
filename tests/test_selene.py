import allure
from allure_commons.types import Severity
from selene import be, by
from selene.support.shared import browser

allure.dynamic.tag('web')
allure.dynamic.severity(Severity.CRITICAL)
allure.dynamic.label('owner', 'mrantip')
allure.dynamic.feature('Issues tab')
allure.dynamic.story('Поиск Issues')
allure.dynamic.link('https://github.com/', name='Testing')


def test_find_issue():
    '''
    Тест Чистый Selene (без шагов)
    '''
    browser.open('https://github.com')

    browser.element(".header-search-button").click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example')
    browser.element('#query-builder-test').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text("#76")).should(be.visible)
    browser.quit()
