import os
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import propmanager

config = propmanager.PropManager(os.getenv('MS_KEY'))
print(config)
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = uc.Chrome(options=options)
driver.implicitly_wait(10)

unilist = ['ubs','sbu','ga','osu']

def open_new_tab(url):
    scr = "window.open('"+ url +"', '_blank');"
    driver.execute_script(scr)

def openunipage(uni,i):
    if(uni == 'ncsu'):
        try:
            if(driver.find_element(By.ID,'_pc_1')):
                driver.find_element(By.ID,'_pc_1').click()
        except NoSuchElementException:
            print('skipping consent')

        try:
            if(driver.find_element(By.ID,'email')):
                email = driver.find_element(By.ID,'email')
                password = driver.find_element(By.ID,'password')
                email.send_keys(config.prop('ncsu.username'))
                password.send_keys(config.prop('ncsu.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')

        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Master's and Doctoral Programs"))
            )

        try:
            if(driver.find_element(By.LINK_TEXT, "Master's and Doctoral Programs")):
                element = driver.find_element(By.LINK_TEXT, "Master's and Doctoral Programs")
                element.click()
        except NoSuchElementException:
            print('Application not found')

        try:
            if(driver.find_element(By.CSS_SELECTOR,'div.action > button.default')):
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('Could not open application')
    elif(uni == 'cu'):
        try:
            if(driver.find_element(By.ID,'email')):
                email = driver.find_element(By.ID,'email')
                password = driver.find_element(By.ID,'password')
                email.send_keys(config.prop('cu.username'))
                password.send_keys(config.prop('cu.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')

        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "2022 Graduate Application"))
            )

        try:
            if(driver.find_element(By.LINK_TEXT, "2022 Graduate Application")):
                element = driver.find_element(By.LINK_TEXT, "2022 Graduate Application")
                element.click()
        except NoSuchElementException:
            print('Application not found')

        try:
            if(driver.find_element(By.CSS_SELECTOR,'div.action > button.default')):
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('Could not open application')
    elif(uni=='wisc'):
        try:
            if(driver.find_element(By.ID,'UserName')):
                email = driver.find_element(By.ID,'UserName')
                password = driver.find_element(By.ID,'Password')
                email.send_keys(config.prop('wisc.username'))
                password.send_keys(config.prop('wisc.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'button.btn')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')

        try:
            if(driver.find_element(By.CSS_SELECTOR, "td.all > a.btn")):
                element = driver.find_element(By.CSS_SELECTOR, "td.all > a.btn")
                element.click()
        except NoSuchElementException:
            print('Application not found')
    elif(uni=='msu'):
        try:
            if(driver.find_element(By.ID,'email')):
                email = driver.find_element(By.ID,'email')
                password = driver.find_element(By.ID,'password')
                email.send_keys(config.prop('msu.username'))
                password.send_keys(config.prop('msu.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')

        try:
            if(driver.find_element(By.LINK_TEXT, "Graduate")):
                element = driver.find_element(By.LINK_TEXT, "Graduate")
                element.click()
        except NoSuchElementException:
            print('Application not found')

        try:
            if(driver.find_element(By.CSS_SELECTOR,'div.action > button.default')):
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('Could not open application')
    elif(uni=='tamu'):
        try:
            if(driver.find_element(By.ID,'cas-login-field-username')):
                email = driver.find_element(By.ID,'cas-login-field-username')
                password = driver.find_element(By.ID,'cas-login-field-password')
                email.send_keys(config.prop('tamu.username'))
                password.send_keys(config.prop('tamu.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'button.cas-login-sign-in-button')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')

        try:
            if(driver.find_element(By.CSS_SELECTOR, "a.cas-notification-csu-cas")):
                element = driver.find_element(By.CSS_SELECTOR, "a.cas-notification-csu-cas")
                element.click()
        except NoSuchElementException:
            print('Application not found')
    elif(uni=='ubs'):
        try:
            if(driver.find_element(By.ID,'email')):
                email = driver.find_element(By.ID,'email')
                password = driver.find_element(By.ID,'password')
                email.send_keys(config.prop('ubs.username'))
                password.send_keys(config.prop('ubs.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')

        try:
            if(driver.find_element(By.LINK_TEXT, "2022 School of Engineering and Applied Sciences Graduate Application")):
                element = driver.find_element(By.LINK_TEXT, "2022 School of Engineering and Applied Sciences Graduate Application")
                element.click()
        except NoSuchElementException:
            print('Application not found')

        try:
            if(driver.find_element(By.CSS_SELECTOR,'div.action > button.default')):
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('Could not open application')
    elif(uni=='sbu'):
        try:
            if(driver.find_element(By.ID,'email')):
                email = driver.find_element(By.ID,'email')
                password = driver.find_element(By.ID,'password')
                email.send_keys(config.prop('sbu.username'))
                password.send_keys(config.prop('sbu.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')

        try:
            if(driver.find_element(By.LINK_TEXT, "2022 Graduate Application")):
                element = driver.find_elements(By.LINK_TEXT, "2022 Graduate Application")
                element[1].click()
        except NoSuchElementException:
            print('Application not found')

        try:
            if(driver.find_element(By.CSS_SELECTOR,'div.action > button.default')):
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('Could not open application')
    elif(uni=='ga'):
        try:
            if(driver.find_element(By.ID,'email')):
                email = driver.find_element(By.ID,'email')
                password = driver.find_element(By.ID,'password')
                email.send_keys(config.prop('ga.username'))
                password.send_keys(config.prop('ga.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')

        try:
            if(driver.find_element(By.LINK_TEXT, "2023 Graduate Application")):
                element = driver.find_element(By.LINK_TEXT, "2023 Graduate Application")
                element.click()
        except NoSuchElementException:
            print('Application not found')

        try:
            if(driver.find_element(By.CSS_SELECTOR,'div.action > button.default')):
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('Could not open application')
    elif(uni=='ufl'):
        try:
            if(driver.find_element(By.ID,'email')):
                email = driver.find_element(By.ID,'email')
                password = driver.find_element(By.ID,'password')
                email.send_keys(config.prop('ufl.username'))
                password.send_keys(config.prop('ufl.password'))
                btn = driver.find_element(By.CSS_SELECTOR,'div.action > button.default')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')
    elif(uni=='osu'):
        try:
            if(driver.find_element(By.ID,'username')):
                email = driver.find_element(By.ID,'username')
                password = driver.find_element(By.ID,'password')
                email.send_keys(config.prop('osu.username'))
                password.send_keys(config.prop('osu.password'))
                btn = driver.find_element(By.ID,'submit')
                btn.click()
        except NoSuchElementException:
            print('could not login, exiting')


def runMain():
    i=0
    for uni in unilist:
        url = config.prop(uni + '.url')
        if(i==0):
            driver.get(url)
        else:
            open_new_tab(url)
            driver.switch_to.window(driver.window_handles[i])
        openunipage(uni,i)
        i+=1

runMain()