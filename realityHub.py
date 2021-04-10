import helper


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

REALITY_HUB_TIMEOUT = 10

def addEvent(eventObj, credentials):    
    eventURL = None
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://realityhub.climaterealityproject.org/home")
    # Page Load
    loginButtonID = "headerLogLink"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, loginButtonID):
        print("Page has not loaded in time")
        return eventURL
    driver.find_element_by_id(loginButtonID).send_keys(Keys.ENTER)
    # Login
    emailFieldID = "email"
    passwordFieldID = "password"
    loginButtonID = "main_login_button"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, emailFieldID):
        print("Page has not loaded in time")
        return eventURL
    driver.find_element_by_id(emailFieldID).send_keys(credentials["username"])
    driver.find_element_by_id(passwordFieldID).send_keys(credentials["password"])
    driver.find_element_by_id(loginButtonID).send_keys(Keys.ENTER)
    # Go to Events
    actBarID = "navbarDropdown_1"
    attendEventText = "Record an"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, actBarID):
        print("Page has not loaded in time")
        return eventURL
    action = ActionChains(driver)
    actBar = driver.find_element_by_id(actBarID)
    action.click(on_element = actBar)
    action.perform()
    # Need to see it on the screen before you click
    helper.PauseForEffect(1)
    
    # Need to create a new chain every time
    action = ActionChains(driver)    
    attendEventLink = driver.find_element_by_partial_link_text(attendEventText)
    action.click(on_element = attendEventLink)
    action.perform()
    
    
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    organizeEventLink = "Organize"
    action = ActionChains(driver)    
    attendEventLink = driver.find_element_by_partial_link_text(organizeEventLink)
    action.click(on_element = attendEventLink)
    action.perform()
    
    
    