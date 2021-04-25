from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Error
from time import sleep as s
import bdd

test = bdd.BDD('Welling83488832','Wellington24','tonmedeiros','firefox',test=True)
driver = test.driver_get()
browser = 'chrome'
try:
    test.login()
    s(5)
    test.user_finder()
    s(5)
    driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/div').click()  # Botão três pontos
    print('[teste-mode] clicando na opção de denunciar')
    driver.find_element_by_css_selector('div.r-1loqt21:nth-child(8)').click()  # Botão de denunciar
    s(1)
    print('[teste-mode] entrando no iframe')
    driver.switch_to.frame(0)  # Entrando no iFrame
    wait(driver, 5).until(
                    lambda driver: driver.find_element_by_css_selector('#compromised-btn#compromised-btn'))
    print('[teste-mode] clicando para denuciar')
    driver.find_element_by_css_selector(
                    '#compromised-btn#compromised-btn').click()  # Botão de Denúncia por hack

except(KeyboardInterrupt):
    test.abort_bot()
finally:
    test.abort_bot()