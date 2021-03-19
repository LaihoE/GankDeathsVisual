import csv
from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

def opggloop(username):
    url = f"https://euw.op.gg/summoner/userName={username}"
    path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
    DRIVER_PATH = path
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(url)

    driver.find_element_by_id('right_gametype_soloranked').click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='TimeStamp']"))).get_attribute("data-datetime")
    box=driver.find_element_by_class_name("GameItemList")

    with open(os.path.join(os.path.dirname(__file__),"data","CSV","recentgames.csv"), "w", newline='\n')as f:
        thewriter = csv.writer(f)
        thewriter.writerow(["id"])

    for x in range(20):
        try:
            game = box.find_elements_by_class_name('GameItemWrap')[x]
            ids=game.find_element(By.CSS_SELECTOR, "div[data-game-result]").get_attribute("data-game-id")
            with open(os.path.join(os.path.dirname(__file__),"data","CSV","recentgames.csv"), "a", newline='\n')as f:
                thewriter = csv.writer(f)
                thewriter.writerow([ids])
        except:
            print("Failed")
            pass



