from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import re
import time
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
# options.add_argument('--headless')

# driver = webdriver.Chrome(chrome_options = options, executable_path = "/Users/christianlin/Downloads/chromedriver")
# options = webdriver.ChromeOptions()


driver = webdriver.Chrome(r"c:\Users\22berniec\Desktop\chromedriver")
driver.get("https://tas.nutrislice.com/menu/tas/serving-line")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[4]/p" )))
# time.sleep(2)

driver.maximize_window()
# button = driver.find_element(By.CLASS_NAME, "wf-roboto-n4
# -active wf-roboto-i7-active wf-roboto-n7-active wf-roboto-i4-active wf-montserrat-n6-active wf-montserrat-n4-active wf-montserrat-i4-active wf-montserrat-n2-active wf-montserrat-n7-active wf-montserrat-i6-active wf-active")

button = driver.find_element(By.XPATH, "/html/body")

button = button.find_element(By.CLASS_NAME, "splash-container")

button = button.find_element(By.CLASS_NAME, "primary")

button.click()

time.sleep(4) 

week = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[2]/div/div[1]/ul")
days = week.find_elements(By.CLASS_NAME, "day")
for day in days:
    date = day.find_element(By.CLASS_NAME, "day-label")
    print(date.text)
    item = day.find_element(By.CLASS_NAME, "items")
    print("Entrees: ", end = "")
    dishes = item.find_element(By.TAG_NAME, "ul")
    dishes = dishes.find_elements(By.CLASS_NAME, "food-card")
    for dish in dishes:
        dishName = dish.find_element(By.CLASS_NAME, "food-name")
        print(dishName.text, end = ": [")
        dish.click()
        # time.sleep(2)
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/ul/li[1]/div/div/div[2]/div[2]/fieldset/ul")))
        modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
        modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
        modalActive = modalList.find_element_by_css_selector("li.modal.active")
        temp = modalActive.find_element(By.CLASS_NAME, "item-container")

        info = temp.find_element(By.CLASS_NAME, "info")
        tabActive = info.find_element_by_css_selector("div.tab.active")
        infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

        calories = infocontainer.find_element(By.CLASS_NAME, "calories")
        print(calories.text, end = " ")
        infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
        fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
        totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
        print("Total Fat: ", totalFat.text, end = " ")
        carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
        carbs = carbs[4]
        print("Total Carbs: ", carbs.text, end = " ]")

        modal = modalList.find_element_by_css_selector("li.modal.active")
        close = modal.find_element_by_css_selector("a.modal-carousel.close")
        close.click()
        

    print("Sides: ", end = "")
    dishes = item.find_elements(By.TAG_NAME, "ul")
    dishes = dishes[1]
    dishes = dishes.find_elements(By.CLASS_NAME, "food-card")
    for dish in dishes:
        dishName = dish.find_element(By.CLASS_NAME, "food-name")
        print(dishName.text, end = ": [")
        dish.click()
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/ul")))
        modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
        modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
        modalActive = modalList.find_element_by_css_selector("li.modal.active")
        temp = modalActive.find_element(By.CLASS_NAME, "item-container")

        info = temp.find_element(By.CLASS_NAME, "info")
        tabActive = info.find_element_by_css_selector("div.tab.active")
        infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

        calories = infocontainer.find_element(By.CLASS_NAME, "calories")
        print(calories.text, end = " ")
        infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
        fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
        totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
        print("Total Fat: ", totalFat.text, end = " ")
        carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
        carbs = carbs[4]
        print("Total Carbs: ", carbs.text, end = " ]")

        modal = modalList.find_element_by_css_selector("li.modal.active")
        close = modal.find_element_by_css_selector("a.modal-carousel.close")
        close.click()
    print("Fruits & Desserts: ", end = "")
    dishes = item.find_elements(By.TAG_NAME, "ul")
    dishes = dishes[2]
    dishes = dishes.find_elements(By.CLASS_NAME, "food-card")
    for dish in dishes:
        dishName = dish.find_element(By.CLASS_NAME, "food-name")
        print(dishName.text, end = ": [")
        dish.click()
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/ul/li[1]/div/div/div[2]/div[2]/fieldset/ul")))
        modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
        modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
        modalActive = modalList.find_element_by_css_selector("li.modal.active")
        temp = modalActive.find_element(By.CLASS_NAME, "item-container")

        info = temp.find_element(By.CLASS_NAME, "info")
        tabActive = info.find_element_by_css_selector("div.tab.active")
        infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

        calories = infocontainer.find_element(By.CLASS_NAME, "calories")
        print(calories.text, end = " ")
        infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
        fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
        totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
        print("Total Fat: ", totalFat.text, end = " ")
        carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
        carbs = carbs[4]
        print("Total Carbs: ", carbs.text, end = " ]")

        modal = modalList.find_element_by_css_selector("li.modal.active")
        close = modal.find_element_by_css_selector("a.modal-carousel.close")
        close.click()
        
    print(); print();
