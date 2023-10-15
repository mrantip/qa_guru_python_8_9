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


def test_decorator_steps():
    '''
    Шаги с декоратором @allure.step
    '''
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com')


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example')
    browser.element('#query-builder-test').submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text('eroshenkoam/allure-example')).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text("#76")).should(be.visible)
