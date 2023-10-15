import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene import be, by

allure.dynamic.tag('web')
allure.dynamic.severity(Severity.CRITICAL)
allure.dynamic.label('owner', 'mrantip')
allure.dynamic.feature('Issues tab')
allure.dynamic.story('Поиск Issues')
allure.dynamic.link('https://github.com/', name='Testing')


def test_dynamic_steps():
    '''
    Лямбда шаги через with allure.step
    '''
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com')

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-button").click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example')
        browser.element('#query-builder-test').submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем таб Issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)

    browser.quit()
