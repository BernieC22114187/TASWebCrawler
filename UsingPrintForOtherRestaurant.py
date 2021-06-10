def generically_filter(something, include): 
    results = list() 
    for each in something: 
        if each in include: 
            results.append(each)
         
    return results 


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# driver = webdriver.Chrome(chrome_options = options, executable_path = "/Users/christianlin/Desktop/Coding/chromedriver")
driver = webdriver.Chrome("/Users/22berniec/Desktop/chromedriver_win32/chromedriver")
driver.get("https://tas.nutrislice.com/menu/tas/serving-line/print-menu/month/2021-04-16")   

wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/ng-view/div/print-sidebar/div/div[1]/div[3]/div[1]/ul/li[1]/a")))

button = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/print-sidebar/div/div[1]/div[3]/div[1]/ul/li[1]/a")
button.click()

wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/div/ng-view/div/print-sidebar/div/div[1]/div[3]/div[1]/ul/li[1]/a")))

body = driver.find_element(By.XPATH, "/html/body") 
weekBlock = body.find_elements_by_xpath('//*[@class="menu-day-contents font-normal height11"]')
print("weekBlock count: ", len(weekBlock))
# /html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[1]/label/span
button = body.find_element(By.TAG_NAME, "div")
button = button.find_element(By.TAG_NAME, "ng-view")
landscape = button.find_element(By.TAG_NAME, "div")
printSidebar = landscape.find_element(By.TAG_NAME, "print-sidebar")
button = printSidebar.find_element(By.CLASS_NAME, "rb")
button = button.find_element(By.CLASS_NAME, "lists")
button = button.find_element(By.TAG_NAME, "div")
buttonList = button.find_element(By.TAG_NAME, "div")
button = buttonList.find_element(By.TAG_NAME, "div")
button = button.find_element(By.TAG_NAME, "label")
button = button.find_element(By.TAG_NAME, "span")
button.click()
'''carbohydrates button'''
#/html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[2]/label/span 
button = buttonList.find_elements(By.TAG_NAME, "div")[1]
button = button.find_element(By.TAG_NAME, "label")
button = button.find_element(By.TAG_NAME, "span")
button.click()
'''Protein button'''
#/html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[4]/label/span
button = buttonList.find_elements(By.TAG_NAME, "div")[3]
button = button.find_element(By.TAG_NAME, "label")
button = button.find_element(By.TAG_NAME, "span")
button.click()


'''Salad Bar'''
saladBar = landscape.find_element(By.ID, "print-area")
saladBar = saladBar.find_element(By.ID, "page-1")
saladBar = saladBar.find_element(By.ID, "page-body")
saladBar = saladBar.find_element(By.ID, "print-footer")

saladBar = saladBar.find_elements(By.TAG_NAME, "div")[5]
saladBar = saladBar.find_element(By.CLASS_NAME, "footer-foodlists")
saladBarList = [] # Ex. [ ["Lettuce", calorie, carbo, protein, totalFat, cholesterol, sodium], ....  ]
foodItems = saladBar.find_elements(By.CLASS_NAME, "footer-foodlist-item")
for food in foodItems:
    tmp1 = food.find_element(By.TAG_NAME, "div")
    foodList = []
    foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
    foodList.append(foodInfo[0].text) # name
    statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
    statStringList = statString.split(",", 3)
    for x in range(3):
        foodList.append(statStringList[x])
        
    saladBarList.append(foodList)

# for element in weekBlock:

#     divs = element.find_elements(By.TAG_NAME, "div")

#     day = divs[0]
#     print("April : ", day.text)

#     information = divs[1]
#     block = information.find_element(By.TAG_NAME, "div")
#     lines = block.find_elements(By.TAG_NAME, "div") 

#     for line in lines:
#         print(line.text)




#### print lower part
# others = body.find_element_by_xpath('//*[@id="print-footer"]')
# divs = others.find_elements(By.TAG_NAME, "div")
# count = 0

# for div in divs:
#     count += 1

#     if count <= 2:
#         continue
#     else:
#         block = div.find_element(By.TAG_NAME, "div")
#         title = block.find_elements(By.TAG_NAME, "span")
#         items = div.find_elements(By.CLASS_NAME, "footer-foodlist-item")

#         print("store title: {}".format(title.text))

#         for item in items:
#             name = item.find_elements(By.TAG_NAME, "div")
#             print(name.text)
    