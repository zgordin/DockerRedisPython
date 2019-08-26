from selenium import webdriver

WEB_SITE ="http://192.168.99.100:5000"



if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="C:\\Users\\zgordin\\Documents\\chromedriver.exe")
    driver.implicitly_wait(20)  # give up to 20 sec to find on all find_elemets or find_elements
    driver.get(WEB_SITE)
    originalstr = str(driver.page_source.encode("utf-8"))
    newres = originalstr.replace("World", "")
    print(newres)
