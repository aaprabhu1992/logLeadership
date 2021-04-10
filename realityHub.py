import helper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

REALITY_HUB_TIMEOUT = 10


def addAllLeadership(eventObj, credentials):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://realityhub.climaterealityproject.org/home")
    # Page Load
    loginButtonID = "headerLogLink"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, loginButtonID):
        print("Page has not loaded in time")
        return
    driver.find_element_by_id(loginButtonID).send_keys(Keys.ENTER)
    # Login
    emailFieldID = "email"
    passwordFieldID = "password"
    loginButtonID = "main_login_button"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, emailFieldID):
        print("Page has not loaded in time")
        return
        
    driver.find_element_by_id(emailFieldID).send_keys(credentials["username"])
    driver.find_element_by_id(passwordFieldID).send_keys(credentials["password"])
    driver.find_element_by_id(loginButtonID).send_keys(Keys.ENTER)
    # Go to Events
    actBarID = "navbarDropdown_1"
    recordLeadershipText = "Record an"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, actBarID):
        print("Page has not loaded in time")
        return
    action = ActionChains(driver)
    actBar = driver.find_element_by_id(actBarID)
    action.click(on_element = actBar)
    action.perform()
    # Need to see it on the screen before you click
    helper.PauseForEffect(1)

    # Need to create a new chain every time
    action = ActionChains(driver)    
    attendEventLink = driver.find_element_by_partial_link_text(recordLeadershipText)
    action.click(on_element = attendEventLink)
    action.perform()    
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)


    if "organize" in eventObj:
        allOrganizations = eventObj["organize"]
        for organizeObj in allOrganizations:
            driver.switch_to.window(driver.window_handles[-1])
            addOrganize(driver, organizeObj)


    if "assist" in eventObj:
        allAssists = eventObj["assist"]
        for assistObj in allAssists:
            driver.switch_to.window(driver.window_handles[-1])
            addAssist(driver, assistObj)

    if "participate" in eventObj:
        allParticipates = eventObj["participate"]
        for participateObj in allParticipates:
            driver.switch_to.window(driver.window_handles[-1])
            addParticipate(driver, participateObj)

    if "blog" in eventObj:
        allBlogs = eventObj["blog"]
        for blogObj in allBlogs:
            driver.switch_to.window(driver.window_handles[-1])
            addBlog(driver, blogObj)

    # All Acts have been added
    # Now Close the window
    driver.quit()


def addPhotoOrganize(driver, photoObj):
    photoNameID = "file_419_File Name"
    photoDescID = "file_419_File Description"
    addPhotoButtonID = "file_419"
    driver.find_element_by_id(photoNameID).send_keys(photoObj["name"])
    driver.find_element_by_id(photoDescID).send_keys(photoObj["description"])
    driver.find_element_by_id(addPhotoButtonID).send_keys(photoObj["path"])


def addPhotoAssist(driver, photoObj):
    photoNameID = "file_342_File Name"
    photoDescID = "file_342_File Description"
    addPhotoButtonID = "file_342"
    driver.find_element_by_id(photoNameID).send_keys(photoObj["name"])
    driver.find_element_by_id(photoDescID).send_keys(photoObj["description"])
    driver.find_element_by_id(addPhotoButtonID).send_keys(photoObj["path"])

def addPhotoParticipate(driver, photoObj):
    photoNameID = "file_428_File Name"
    photoDescID = "file_428_File Description"
    addPhotoButtonID = "file_428"
    driver.find_element_by_id(photoNameID).send_keys(photoObj["name"])
    driver.find_element_by_id(photoDescID).send_keys(photoObj["description"])
    driver.find_element_by_id(addPhotoButtonID).send_keys(photoObj["path"])


def addOrganize(driver, eventObj):    
    organizeEventLink = "Organize"
    action = ActionChains(driver)    
    attendEventLink = driver.find_element_by_partial_link_text(organizeEventLink)
    action.click(on_element = attendEventLink)
    action.perform()
    
    driver.switch_to.window(driver.window_handles[-1])
    addLeadershipButtonID = "reviews_item_form_button"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, addLeadershipButtonID):
        print("Page has not loaded in time")
        return
    eventDateID = "date_412"
    eventNameID = "textField_413"
    eventAttendanceID = "textField_415"
    textAreaID = "textarea_418"
    driver.find_element_by_id(eventDateID).send_keys(eventObj["date"])
    driver.find_element_by_id(eventNameID).send_keys(eventObj["name"])
    driver.find_element_by_id(eventAttendanceID).send_keys(eventObj["attendance"])
    driver.find_element_by_id(textAreaID).send_keys(eventObj["description"])
    
    # Radio Button
    elements = driver.find_elements_by_tag_name("label")
    for elem in elements:
        if elem.text == eventObj["type"]:
            elem.click()
    if "photo" in eventObj:
        addPhotoOrganize(driver, eventObj["photo"])
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    driver.find_element_by_id(addLeadershipButtonID).click()    
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    
    # Only Close the TAB
    driver.close()

def addParticipate(driver, eventObj):    
    participateEventLink = "Participate"
    action = ActionChains(driver)    
    attendEventLink = driver.find_element_by_partial_link_text(participateEventLink)
    action.click(on_element = attendEventLink)
    action.perform()
    
    driver.switch_to.window(driver.window_handles[-1])
    addLeadershipButtonID = "reviews_item_form_button"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, addLeadershipButtonID):
        print("Page has not loaded in time")
        return
    eventDateID = "date_421"
    eventNameID = "textField_422"
    eventHostID = "textField_423"
    textAreaID = "textarea_427"
    driver.find_element_by_id(eventDateID).send_keys(eventObj["date"])
    driver.find_element_by_id(eventNameID).send_keys(eventObj["name"])
    driver.find_element_by_id(eventHostID).send_keys(eventObj["host"])
    driver.find_element_by_id(textAreaID).send_keys(eventObj["description"])
    
    # Radio Button
    elements = driver.find_elements_by_tag_name("label")
    for elem in elements:
        if elem.text == eventObj["type"]:
            elem.click()
    if "photo" in eventObj:
        addPhotoParticipate(driver, eventObj["photo"])
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    driver.find_element_by_id(addLeadershipButtonID).click()    
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    
    # Only Close the TAB
    driver.close()



def addBlog(driver, eventObj):    
    blogEventLink = "Blog"
    action = ActionChains(driver)    
    attendEventLink = driver.find_element_by_partial_link_text(blogEventLink)
    action.click(on_element = attendEventLink)
    action.perform()
    
    driver.switch_to.window(driver.window_handles[-1])
    addLeadershipButtonID = "reviews_item_form_button"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, addLeadershipButtonID):
        print("Page has not loaded in time")
        return
    blogDateID = "date_381"
    blogNameID = "textField_382"
    blogTitleID = "textField_383"
    linkID = "link_385"
    textAreaID = "textarea_386"
    driver.find_element_by_id(blogDateID).send_keys(eventObj["date"])
    driver.find_element_by_id(blogNameID).send_keys(eventObj["name"])
    driver.find_element_by_id(blogTitleID).send_keys(eventObj["title"])
    driver.find_element_by_id(linkID).send_keys(eventObj["link"])
    driver.find_element_by_id(textAreaID).send_keys(eventObj["description"])
    
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    driver.find_element_by_id(addLeadershipButtonID).click()    
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    
    # Only Close the TAB
    driver.close()
    
def addAssist(driver, eventObj):
    assistEventLink = "Assist"
    action = ActionChains(driver)    
    attendEventLink = driver.find_element_by_partial_link_text(assistEventLink)
    action.click(on_element = attendEventLink)
    action.perform()
    
    driver.switch_to.window(driver.window_handles[-1])
    addLeadershipButtonID = "reviews_item_form_button"
    if not helper.HasPageLoadedIDCheck(driver, REALITY_HUB_TIMEOUT, addLeadershipButtonID):
        print("Page has not loaded in time")
        return
    eventDateID = "date_191"
    eventAttendanceID = "number_224"
    textAreaID = "textarea_195"
    driver.find_element_by_id(eventDateID).send_keys(eventObj["date"])
    driver.find_element_by_id(eventAttendanceID).send_keys(eventObj["attendance"])
    driver.find_element_by_id(textAreaID).send_keys(eventObj["description"])
    
    if "photo" in eventObj:
        addPhotoAssist(driver, eventObj["photo"])
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    driver.find_element_by_id(addLeadershipButtonID).click()    
    helper.PauseForEffect(REALITY_HUB_TIMEOUT)
    
    # Only Close the TAB
    driver.close()
    
    
    