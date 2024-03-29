from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_to_microsoft(gmail, pswd):
    """
    This function automates the login process for Microsoft Student Learn using Selenium.

    It prompts the user to enter their email and password, and then navigates to the login page.
    After successfully logging in, it navigates to the Microsoft Learn training page and retrieves the links to the available modules.
    It then iterates through each module, clicks on the module link, retrieves the links to the tasks within the module,
    and finally clicks on each task link.

    Note: This code requires the Selenium library to be installed.

    Returns:
        None
    """
    try:
        email = gmail
        password = pswd

        driver = webdriver.Chrome()
        driver.get(r"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=18fbca16-2224-45f6-85b0-f7bf2b39b3f3&scope=openid%20profile%20email%20offline_access&redirect_uri=https%3A%2F%2Flearn.microsoft.com%2F_themes%2Fdocs.theme%2Fmaster%2Fen-us%2F_themes%2Fglobal%2Fidentity-redirect.html&client-request-id=15c565ee-5f88-4907-b187-59da2a3afc8b&response_mode=fragment&response_type=code&x-client-SKU=msal.js.browser&x-client-VER=2.32.2&client_info=1&code_challenge=c3GAsXvs9oyrl_afMSkI5kjEXJGS8RK4eZUrUoOpm0I&code_challenge_method=S256&prompt=select_account&nonce=e38c3039-cf25-40c1-b16f-fabfa60e3367&state=eyJpZCI6IjdkZTNkOGQ3LWU1NTgtNDhhNS05ZGFjLTEyOWJkZmY5YjNkMSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D%7Chttps%253A%252F%252Flearn.microsoft.com%252Fen-us%252Ftraining%252F%253Fsource%253Dlearn")
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(email)
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(5)
        try:
            driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(password)
            driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        except Exception as e:
            (driver.find_element(By.XPATH, '//*[@id="pageContent"]/div/form/div[3]/div/div/div')).find_element(By.TAG_NAME, 'span').click()
            time.sleep(4)
            driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(password)
            driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(4)
        try :
            remember = driver.find_element(By.XPATH, '//*[@id="lightbox"]/div[3]/div/div[2]/div/div[3]/div[1]/div')
            remember.find_element(By.TAG_NAME, 'span').click()
            driver.find_element(By.XPATH, '//*[@id="lightbox"]/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]').click()
        except Exception as e:
            print("Error", e)
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="checkboxField"]').click()
            (driver.find_element(By.XPATH, '//*[@id="pageContent"]/div/div/form/div[3]/div[2]/div/div[2]')).find_element(By.TAG_NAME, 'button').click()
        time.sleep(6)
        driver.get(r"https://learn.microsoft.com/en-us/training/?source=learn")
        try:
            driver.find_element(By.XPATH, '//*[@id="ms--site-header"]/div[1]/a[3]').click()
            time.sleep(6)
            driver.find_element(By.XPATH, '//*[@id="tilesHolder"]/div[1]').click()
            time.sleep(6)
        except Exception as e:
            driver.find_element(By.XPATH, '//*[@id="lightboxTemplateContainer"]/div[2]/div[1]/div/div/div/div/div[3]/div[2]').click()
            time.sleep(8)
        driver.get(r'https://learn.microsoft.com/en-us/users/me/')
        time.sleep(6)
        driver.find_element(By.XPATH, '//*[@id="profile-nav"]/nav[1]/ul/li[3]/a').click()
        time.sleep(8)
        print("Challenge\n")
        challenges = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/section/div[1]/div/div/ol')
        links = challenges.find_elements(By.TAG_NAME, 'a')
        links = [link.get_attribute('href') for link in links]
        print("Modules are stored\n", links)
        for link in links:
            driver.get(link)
            time.sleep(6)

            section = driver.find_element(By.XPATH, '//*[@id="challenge-container"]/div/div/div/div[1]')
            section.find_element(By.TAG_NAME, 'a').click()
            print("Module is started\n")
            time.sleep(6)

            modules = driver.find_element(By.XPATH, '//*[@id="items-list"]')
            modules_links = modules.find_elements(By.TAG_NAME, 'a')
            modules_links = [module.get_attribute('href') for module in modules_links]
            print("All units links are stored\n", modules_links)

            for unit_link in modules_links:
                driver.get(unit_link)
                print("Clicked on the Module link ")
                time.sleep(6)

                tasks = driver.find_element(By.XPATH, '//*[@id="unit-list"]')
                tasks_links = tasks.find_elements(By.TAG_NAME, 'a')
                tasks_links = [task.get_attribute('href') for task in tasks_links]
                print("All tasks links are stored\n", tasks_links)

                for unit_particular_link in tasks_links:
                    driver.get(unit_particular_link)
                    time.sleep(6)
                    print("Entered " + driver.find_element(By.XPATH, '//*[@id="unit-inner-section"]/h1').text)
                    try:
                        if(driver.find_element(By.XPATH, '//*[@id="unit-inner-section"]/h1').text == 'Knowledge check'):
                            input_container = driver.find_element(By.XPATH, '//*[@id="unit-inner-section"]/form/fieldset/div')
                            inputs = input_container.find_elements(By.TAG_NAME, 'input')
                            time.sleep(10)
                            for inp in inputs:
                                inp.click()
                            driver.find_element(By.XPATH, '//*[@id="unit-inner-section"]/form/fieldset/button').click()
                            time.sleep(10)
                        footer = driver.find_element(By.XPATH, '//*[@id="next-section"]')
                        footer.find_element(By.TAG_NAME, 'a').click()
                    except Exception as e:
                        print("Error", e)
    except Exception as e:
        print("Error", e)
    finally:
        driver.quit()
        return "Task Completed"
