import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

month_to_select = "November"
year_to_select = "2023"

location_number = 3
'''
1. Carson City 
2. Decatur 
3. Flamingo 
4. Henderson
5. Sahara
6. South Reno
'''

action_number = 2
'''
1. ADA - Disabilities Center
2. Drivers License - Renewal 
3. Drivers License - New 
4. Knowledge/ Written Testing
5. License Plate Pickup\ Drop off
6. Multiple Transactions (DL & Registration)
7. Registration - New
8. Registration - Renewal
9. Suspensions (Reinstatements) - Driver License/Revenue Recovery
10. Suspensions (Reinstatements) - Registration/Revenue Recovery
'''

# Set up chrome the driver 
def driver_define():
    print(f"Chrome Browser Opening")

    driver_path = ChromeDriverManager().install()
    options = Options()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service(driver_path)
    
    driver = webdriver.Chrome(service=s, options =options)
    driver.maximize_window()
    return driver

# Go through the website 
def Open_website(driver):
    driver.get("https://qwebbooking.dmv.nv.gov/qmaticwebbooking/index.html#/")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='process-step-name']")))

    # Location Selection 
    area_button = driver.find_element(By.XPATH , f"//div[@class='v-radio branch theme--light radio-group'][{location_number}]")
    area_button.click()

    sleep(1)

    service_area = driver.find_element(By.CSS_SELECTOR, "[class^='v-input radio-container d-flex hide-border v-input--hide-details theme--light v-input--selection-controls v-input--radio-group v-input--radio-group--column']")

    # Action Selection
    service_button = service_area.find_element(By.XPATH, f"//div[@class='radio-row service-options'][{action_number}]")
    service_button.find_element(By.CSS_SELECTOR, "[class^='v-radio service-name ma-2 pa-0 me-1 theme--light']").click()

    sleep(3)

    month_select = driver.find_element(By.CSS_SELECTOR, '[class^="dateName"]').text


    sleep(1)

    return month_select


def Main():
    driver = driver_define()
    
    select_format = "{month} {year}"

    select_format = select_format.format(month = month_to_select , year = year_to_select)
    counter = 40
    
    for i in range(counter):
        
        Month = Open_website(driver)
        if Month == select_format:
            sleep(120)
            break
        driver.refresh()
        sleep(1)

    
    driver.quit()


if __name__ == "__main__":
    Main()