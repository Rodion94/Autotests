import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

"""Input Values"""
squareFootage = 1000
black_price_per_bag = 25
light_green_price_per_bag = 60
buffing_price_per_bag = 25
"""Open Domen"""
driver = webdriver.Chrome()
driver.get('https://dev5.dev2.playgrounds.com')
driver.maximize_window()
act = ActionChains(driver)
"""Fill In Login"""
user_name = driver.find_element(by=By.ID, value="email")
user_name.send_keys("rodiontest@mail.com")

"""Fill In Password"""
password = driver.find_element(by=By.ID, value="password")
password.send_keys("qwe123ZXC!")

"""Login"""
button_login = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div/form/div[4]/div/button")
button_login.click()

"""Open AAA PIP Calculator Grid"""
aaa_pip_calculator = driver.find_element(by=By.XPATH, value="//*[@id='sidebar']/div/div/div/ul/li[6]/a/span")
aaa_pip_calculator.click()
time.sleep(3)

"""Start New Quote"""
start_new_quote_btn = driver.find_element(by=By.XPATH, value="//*[@id='aaa-rubber-mulch-calculator.index']/div[2]/div/main/div[2]/div/div/div[1]/div[1]/div/a")
start_new_quote_btn.click()
print("Open a new quote")
time.sleep(2)


"""Fill In Required Fields"""
project_name = driver.find_element(by=By.ID, value="project_name")
project_name.send_keys("Test AAA PIP Calculator")
print("Project Name")

click_installation_state = driver.find_element(by=By.XPATH, value="//span[@id='select2-installation_state-container']")
click_installation_state.click()
time.sleep(3)
click_alaska = driver.find_element(by=By.XPATH, value="(//li[@class='select2-results__option'])[1]")
click_alaska.click()
print("Click Alaska")
time.sleep(3)
top_color_1 = driver.find_element(by=By.XPATH, value="//*[@id='aaa-rubber-mulch-calculator.create']/div[2]/div/main/div[2]/div/div/form/div[1]/div/div[6]/span/span[1]/span")
top_color_1.click()
print("Open Dropdown 1st Top Color")
time.sleep(3)
click_black = driver.find_element(by=By.XPATH, value="(//li[@class='select2-results__option select2-results__option--highlighted'])[1]")
click_black.click()
print("1st Top Color - Black")
time.sleep(3)

top_color_2 = driver.find_element(by=By.XPATH, value="//*[@id='aaa-rubber-mulch-calculator.create']/div[2]/div/main/div[2]/div/div/form/div[1]/div/div[7]/span/span[1]/span")
top_color_2.click()
time.sleep(3)
click_light_green = driver.find_element(by=By.XPATH, value="(//li[@class='select2-results__option'])[2]")
click_light_green.click()
print("2nd Top Color - Light Green")
time.sleep(3)

driver.execute_script("window.scrollTo(0, 300)")
time.sleep(3)
square_footage = driver.find_element(by=By.XPATH, value="//input[@id='square_footage']")
square_footage.send_keys(Keys.CONTROL+"a")
time.sleep(3)
square_footage.send_keys('1000')
print("Square Footage = 1000")
time.sleep(3)

driver.execute_script("window.scrollTo(0, 300)")
freight = driver.find_element(by=By.XPATH, value="//input[@id='freight']")
freight.send_keys('500')
print("Freight = 500")
time.sleep(3)

labor_cost = driver.find_element(by=By.XPATH, value="//input[@id='labor_cost_per_sf']")
labor_cost.send_keys('4')
print("Labor Cost = 4")
time.sleep(3)

sub_base = driver.find_element(by=By.XPATH, value="//*[@id='aaa-rubber-mulch-calculator.create']/div[2]/div/main/div[2]/div/div/form/div[1]/div/div[15]/span/span[1]/span")
sub_base.click()


driver.execute_script("window.scrollTo(0, 800)")
time.sleep(4)


"""Get Pad Thickness"""
fall_height = driver.find_element(by=By.XPATH, value="//span[@id='select2-fall-height-container']")
correct_fall_height = int(fall_height.text.replace("'", ""))

match correct_fall_height:
    case 3:
        pad_thickness = 1.5
    case 4:
        pad_thickness = 2
    case 5:
        pad_thickness = 2.5
    case 6:
        pad_thickness = 3
    case 7:
        pad_thickness = 4
    case 9:
        pad_thickness = 5
    case 11:
        pad_thickness = 6
"""Rubber Block"""
topColorBagsTotal = (squareFootage * 1.1 / 55 ) * 2
color1_number_of_bags = topColorBagsTotal / 2
color2_number_of_bags = topColorBagsTotal / 2
black_cost = color1_number_of_bags * black_price_per_bag
light_green_cost = color2_number_of_bags * light_green_price_per_bag
buffingBags = (squareFootage * ((pad_thickness - 0.5) * 2 * 1.4 / 50)).__ceil__()
buffing_cost = buffingBags * buffing_price_per_bag
rubber_total = float(black_cost + light_green_cost + buffing_cost)
time.sleep(4)
"""Compare Rubber Block"""
final_rubber = driver.find_element(by=By.XPATH, value="//*[@id='rubber']/tbody/tr[4]/td[4]")
correct_final_rubber = float(final_rubber.text.split("$")[1].replace(",", ""))
time.sleep(4)
assert rubber_total == correct_final_rubber
print("Rubber Total is Correct")

"""Binder Block"""
topLayerPails = (((color1_number_of_bags + color2_number_of_bags + 0) / 4 ) * (1 + 0.2))
baseLayerPails = float(((buffingBags / 6) * (1 + 0.2)).__ceil__())
topLayerPrice = 120
baseLayerPrice = 120
topLayerCost = topLayerPrice * topLayerPails
baseLayerCost = baseLayerPrice * baseLayerPails
binder_total = topLayerCost + baseLayerCost

"""Compare Binder Block"""
final_binder = driver.find_element(by=By.XPATH, value="//*[@id='binder']/tbody/tr[3]/td[4]/span")
correct_final_binder = float(final_binder.text.split("$")[1].replace(",", ""))
assert binder_total == correct_final_binder
print("Binder Total is Correct")
driver.execute_script("window.scrollTo(0, 1200)")

"""Compare Labor Total"""
labor_total_cost = squareFootage * 4
labor_total = driver.find_element(by=By.XPATH, value="//*[@id='calc-labor-total']")
correct_labor_total = float(labor_total.text.split("$")[1].replace(",", ""))
assert  labor_total_cost == correct_labor_total
print("Labor Total is Correct")

"""Compare Freight Total"""
freight_total = driver.find_element(by=By.XPATH, value="//*[@id='calc-freight-total']")
correct_freight_total = float(freight_total.text.split("$")[1].replace(",", ""))
assert  correct_freight_total == 500
print("Freight Total is Correct")

"""Compare Total Cost Of Job"""
total_cost_of_job = rubber_total + binder_total + correct_labor_total + correct_freight_total

final_cost_of_job = driver.find_element(by=By.XPATH, value="//*[@id='calc-total-cost']")
correct_final_cost_of_job = float(final_cost_of_job.text.split("$")[1].replace(",", ""))
assert correct_final_cost_of_job == total_cost_of_job
print("Total Cost Of Job is Correct")

"""Compare Dealer Cost"""
dealer_cost = (correct_final_rubber + correct_final_binder + correct_freight_total + correct_labor_total) * 1.3
final_dealer_cost = driver.find_element(by=By.XPATH, value="//*[@id='calc-cost-dealer']")
correct_final_dealer_cost = float(final_dealer_cost.text.split("$")[1].replace(",", ""))
assert correct_final_dealer_cost == dealer_cost
print("Dealer Cost is Correct")

"""Compare Selling Price"""
selling_price = correct_final_dealer_cost / 0.8
final_selling_price = driver.find_element(by=By.XPATH, value="//*[@id='calc-selling-price']")
correct_final_selling_price = float(final_selling_price.text.split("$")[1].replace(",", ""))
assert selling_price == correct_final_selling_price
print("Selling Price is Correct")