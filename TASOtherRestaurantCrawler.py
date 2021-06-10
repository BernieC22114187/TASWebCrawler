
def generically_filter(something, include): 
    results = list() 
    for each in something: 
        if each in include: 
            results.append(each)
         
    return results 


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


driver = webdriver.Chrome(r"C:\Users\22berniec\Desktop\chromedriver_win32\chromedriver")
driver.get("https://tas.nutrislice.com/menu/tas/serving-line/2021-05-04")

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
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[1]/div[1]/div/div/div/nav/ul/li/a" )))

# button = button.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[1]/div/div/div/nav/ul/li/a")
# button.click()

# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[11]" )))
# time.sleep(4) 

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[3]/div[1]/h3/a/i" )))

button = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[3]/div[1]/h3/a/i")

# print("11111111111")
# button = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]/div")
# button = button.find_elements(By.TAG_NAME, "div")
# button = button[3]
# print("2222222222222222222222222")
# listContainer = button.find_element(By.TAG_NAME, "div")
# button = listContainer.find_element(By.TAG_NAME, "h3")
# button = button.find_element_by_css_selector("a.toggle.icon-link")
# button = button.find_element(By.CLASS_NAME, "ns-icon-down-chevron")
button.click()
time.sleep(2) 
listContainer = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[3]/div[1]")
button = listContainer.find_element(By.CLASS_NAME, "food-list")
foods = button.find_elements(By.CLASS_NAME, "food")
'''daily carbs'''
for food in foods:
    foodName = food.find_element(By.CLASS_NAME, "food-name")
    print(foodName.text, end = ": [")
    food.click()
    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/div/div/div[2]")))
    
    modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
    modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
    modalActive = modalList.find_element_by_css_selector("li.modal.active")
    temp = modalActive.find_element(By.CLASS_NAME, "item-container")
    info = temp.find_element(By.CLASS_NAME, "info")
   
    info = info.find_element(By.TAG_NAME, "div")
    tabActive = info.find_element_by_css_selector("div.tab.active")
    
    # tabActive = info.find_element(By.XPATH, "div[1]/div[1]")
    infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

    calories = infocontainer.find_element(By.CLASS_NAME, "calories")
    text = ''.join(generically_filter(calories.text, '0123456789.')) 
    print(text, end = " ")
    infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
    fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
    
    totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
    text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
    print("Total Fat: ", text, end = " ")
    
    carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
    cholesterol = carbs[2]
    text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
    print("Cholesterol: ", text, end = " ")
    protein = carbs[6]
    text = ''.join(generically_filter(protein.text, '0123456789.')) 
    print("Protein: ", text, end = " ")
    sodium = carbs[3]
    text = ''.join(generically_filter(sodium.text, '0123456789.')) 
    print("Sodium: ", text, end = " ")
    carbs = carbs[4]
    text = ''.join(generically_filter(carbs.text, '0123456789.')) 
    print("Total Carbs: ", text, end = " ]")
    
    modal = modalList.find_element_by_css_selector("li.modal.active")
    close = modal.find_element_by_css_selector("a.modal-carousel.close")
    close.click()
'''vegan and gluten-free'''
# section = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]") # type-container
# section = section.find_element(By.CLASS_NAME, "content")

# section = section.find_elements(By.TAG_NAME, "div")
# section = section[6]
# # section = section.find_element(By.TAG_NAME, "div")
# listContainer = section.find_element(By.CLASS_NAME, "list-container")
# section = listContainer.find_element(By.TAG_NAME, "h3")
# section = section.find_element(By.TAG_NAME, "a")
# section.click()
# time.sleep(1)
# foodList = listContainer.find_element(By.CLASS_NAME, "food-list")
# foods = foodList.find_elements(By.CLASS_NAME, "food")
# for food in foods:
#     foodName = food.find_element(By.CLASS_NAME, "food-name")
#     print(foodName.text, end = ": [")
#     food.click()
#     wait = WebDriverWait(driver, 5)
#     wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/div/div/div[2]")))
    
#     modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
#     modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
#     modalActive = modalList.find_element_by_css_selector("li.modal.active")
#     temp = modalActive.find_element(By.CLASS_NAME, "item-container")
#     info = temp.find_element(By.CLASS_NAME, "info")
#     tabActive = info.find_element_by_css_selector("div.tab.active")
#     # tabActive = info.find_element(By.XPATH, "div[1]/div[1]")
#     infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

#     calories = infocontainer.find_element(By.CLASS_NAME, "calories")
#     text = ''.join(generically_filter(calories.text, '0123456789.')) 
#     print(text, end = " ")
#     infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
#     fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
    
#     totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
#     text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
#     print("Total Fat: ", text, end = " ")
    
#     carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#     cholesterol = carbs[2]
#     text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
#     print("Cholesterol: ", text, end = " ")
#     protein = carbs[6]
#     text = ''.join(generically_filter(protein.text, '0123456789.')) 
#     print("Protein: ", text, end = " ")
#     sodium = carbs[3]
#     text = ''.join(generically_filter(sodium.text, '0123456789.')) 
#     print("Sodium: ", text, end = " ")
#     carbs = carbs[4]
#     text = ''.join(generically_filter(carbs.text, '0123456789.')) 
#     print("Total Carbs: ", text, end = " ]")
    
#     modal = modalList.find_element_by_css_selector("li.modal.active")
#     close = modal.find_element_by_css_selector("a.modal-carousel.close")
#     close.click()

# '''snack bar breakfast and drinks'''
# section = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]") # type-container
# section = section.find_element(By.CLASS_NAME, "content")

# section = section.find_elements(By.TAG_NAME, "div")
# section = section[8]
# # section = section.find_element(By.TAG_NAME, "div")
# listContainer = section.find_element(By.CLASS_NAME, "list-container")
# section = listContainer.find_element(By.TAG_NAME, "h3")
# section = section.find_element(By.TAG_NAME, "a")
# section.click()
# time.sleep(1)   
# foodList = listContainer.find_element(By.CLASS_NAME, "food-list")
# foods = foodList.find_elements(By.CLASS_NAME, "food")
# for food in foods:
#     foodName = food.find_element(By.CLASS_NAME, "food-name")
#     print(foodName.text, end = ": [")
#     food.click()
#     wait = WebDriverWait(driver, 5)
#     wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/div/div/div[2]")))
    
#     modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
#     modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
#     modalActive = modalList.find_element_by_css_selector("li.modal.active")
#     temp = modalActive.find_element(By.CLASS_NAME, "item-container")
#     info = temp.find_element(By.CLASS_NAME, "info")
#     tabActive = info.find_element_by_css_selector("div.tab.active")
#     # tabActive = info.find_element(By.XPATH, "div[1]/div[1]")
#     infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

#     calories = infocontainer.find_element(By.CLASS_NAME, "calories")
#     text = ''.join(generically_filter(calories.text, '0123456789.')) 
#     print(text, end = " ")
#     infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
#     fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
    
#     totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
#     text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
#     print("Total Fat: ", text, end = " ")
    
#     carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#     cholesterol = carbs[2]
#     text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
#     print("Cholesterol: ", text, end = " ")
#     protein = carbs[6]
#     text = ''.join(generically_filter(protein.text, '0123456789.')) 
#     print("Protein: ", text, end = " ")
#     sodium = carbs[3]
#     text = ''.join(generically_filter(sodium.text, '0123456789.')) 
#     print("Sodium: ", text, end = " ")
#     carbs = carbs[4]
#     text = ''.join(generically_filter(carbs.text, '0123456789.')) 
#     print("Total Carbs: ", text, end = " ]")
    
#     modal = modalList.find_element_by_css_selector("li.modal.active")
#     close = modal.find_element_by_css_selector("a.modal-carousel.close")
#     close.click()

# '''snackbar baked goods and yogurts'''
# section = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]") # type-container
# section = section.find_element(By.CLASS_NAME, "content")

# section = section.find_elements(By.TAG_NAME, "div")
# section = section[9]
# # section = section.find_element(By.TAG_NAME, "div")
# listContainer = section.find_element(By.CLASS_NAME, "list-container")
# section = listContainer.find_element(By.TAG_NAME, "h3")
# section = section.find_element(By.TAG_NAME, "a")
# section.click()
# time.sleep(1)   
# foodList = listContainer.find_element(By.CLASS_NAME, "food-list")
# foods = foodList.find_elements(By.CLASS_NAME, "food")
# for food in foods:
#     foodName = food.find_element(By.CLASS_NAME, "food-name")
#     print(foodName.text, end = ": [")
#     food.click()
#     wait = WebDriverWait(driver, 5)
#     wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/div/div/div[2]")))
    
#     modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
#     modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
#     modalActive = modalList.find_element_by_css_selector("li.modal.active")
#     temp = modalActive.find_element(By.CLASS_NAME, "item-container")
#     info = temp.find_element(By.CLASS_NAME, "info")
#     tabActive = info.find_element_by_css_selector("div.tab.active")
#     # tabActive = info.find_element(By.XPATH, "div[1]/div[1]")
#     infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

#     calories = infocontainer.find_element(By.CLASS_NAME, "calories")
#     text = ''.join(generically_filter(calories.text, '0123456789.')) 
#     print(text, end = " ")
#     infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
#     fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
    
#     totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
#     text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
#     print("Total Fat: ", text, end = " ")
    
#     carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#     cholesterol = carbs[2]
#     text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
#     print("Cholesterol: ", text, end = " ")
#     protein = carbs[6]
#     text = ''.join(generically_filter(protein.text, '0123456789.')) 
#     print("Protein: ", text, end = " ")
#     sodium = carbs[3]
#     text = ''.join(generically_filter(sodium.text, '0123456789.')) 
#     print("Sodium: ", text, end = " ")
#     carbs = carbs[4]
#     text = ''.join(generically_filter(carbs.text, '0123456789.')) 
#     print("Total Carbs: ", text, end = " ]")
    
#     modal = modalList.find_element_by_css_selector("li.modal.active")
#     close = modal.find_element_by_css_selector("a.modal-carousel.close")
#     close.click()

# '''snack bar lunch'''
# section = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]") # type-container
# section = section.find_element(By.CLASS_NAME, "content")

# section = section.find_elements(By.TAG_NAME, "div")
# section = section[10]
# # section = section.find_element(By.TAG_NAME, "div")
# listContainer = section.find_element(By.CLASS_NAME, "list-container")
# section = listContainer.find_element(By.TAG_NAME, "h3")
# section = section.find_element(By.TAG_NAME, "a")
# section.click()
# time.sleep(1)   
# foodList = listContainer.find_element(By.CLASS_NAME, "food-list")
# foods = foodList.find_elements(By.CLASS_NAME, "food")
# for food in foods:
#     foodName = food.find_element(By.CLASS_NAME, "food-name")
#     print(foodName.text, end = ": [")
#     food.click()
#     wait = WebDriverWait(driver, 5)
#     wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/div/div/div[2]")))
    
#     modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
#     modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
#     modalActive = modalList.find_element_by_css_selector("li.modal.active")
#     temp = modalActive.find_element(By.CLASS_NAME, "item-container")
#     info = temp.find_element(By.CLASS_NAME, "info")
#     tabActive = info.find_element_by_css_selector("div.tab.active")
#     # tabActive = info.find_element(By.XPATH, "div[1]/div[1]")
#     infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

#     calories = infocontainer.find_element(By.CLASS_NAME, "calories")
#     text = ''.join(generically_filter(calories.text, '0123456789.')) 
#     print(text, end = " ")
#     infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
#     fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
    
#     totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
#     text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
#     print("Total Fat: ", text, end = " ")
    
#     carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#     cholesterol = carbs[2]
#     text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
#     print("Cholesterol: ", text, end = " ")
#     protein = carbs[6]
#     text = ''.join(generically_filter(protein.text, '0123456789.')) 
#     print("Protein: ", text, end = " ")
#     sodium = carbs[3]
#     text = ''.join(generically_filter(sodium.text, '0123456789.')) 
#     print("Sodium: ", text, end = " ")
#     carbs = carbs[4]
#     text = ''.join(generically_filter(carbs.text, '0123456789.')) 
#     print("Total Carbs: ", text, end = " ]")
    
#     modal = modalList.find_element_by_css_selector("li.modal.active")
#     close = modal.find_element_by_css_selector("a.modal-carousel.close")
#     close.click()

# '''snackbar fruits and veggies'''
# section = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]") # type-container
# section = section.find_element(By.CLASS_NAME, "content")

# section = section.find_elements(By.TAG_NAME, "div")
# section = section[11]
# # section = section.find_element(By.TAG_NAME, "div")
# listContainer = section.find_element(By.CLASS_NAME, "list-container")
# section = listContainer.find_element(By.TAG_NAME, "h3")
# section = section.find_element(By.TAG_NAME, "a")
# section.click()
# time.sleep(1)   
# foodList = listContainer.find_element(By.CLASS_NAME, "food-list")
# foods = foodList.find_elements(By.CLASS_NAME, "food")
# for food in foods:
#     foodName = food.find_element(By.CLASS_NAME, "food-name")
#     print(foodName.text, end = ": [")
#     food.click()
#     wait = WebDriverWait(driver, 5)
#     wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/div/div/div[2]")))
    
#     modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
#     modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
#     modalActive = modalList.find_element_by_css_selector("li.modal.active")
#     temp = modalActive.find_element(By.CLASS_NAME, "item-container")
#     info = temp.find_element(By.CLASS_NAME, "info")
#     tabActive = info.find_element_by_css_selector("div.tab.active")
#     # tabActive = info.find_element(By.XPATH, "div[1]/div[1]")
#     infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

#     calories = infocontainer.find_element(By.CLASS_NAME, "calories")
#     text = ''.join(generically_filter(calories.text, '0123456789.')) 
#     print(text, end = " ")
#     infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
#     fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
    
#     totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
#     text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
#     print("Total Fat: ", text, end = " ")
    
#     carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#     cholesterol = carbs[2]
#     text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
#     print("Cholesterol: ", text, end = " ")
#     protein = carbs[6]
#     text = ''.join(generically_filter(protein.text, '0123456789.')) 
#     print("Protein: ", text, end = " ")
#     sodium = carbs[3]
#     text = ''.join(generically_filter(sodium.text, '0123456789.')) 
#     print("Sodium: ", text, end = " ")
#     carbs = carbs[4]
#     text = ''.join(generically_filter(carbs.text, '0123456789.')) 
#     print("Total Carbs: ", text, end = " ]")
    
#     modal = modalList.find_element_by_css_selector("li.modal.active")
#     close = modal.find_element_by_css_selector("a.modal-carousel.close")
#     close.click()


