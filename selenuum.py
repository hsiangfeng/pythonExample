from selenium import webdriver

# 請安裝相對應瀏覽器的 Driver
# https://sites.google.com/a/chromium.org/chromedriver/
driver = webdriver.Chrome('/Applications/Google Chrome.app/Contents/MacOS/chromedriver')

driver.implicitly_wait(10)

driver.get('https://hsiangfeng.github.io/')

print(driver.title)
fp = open('selenium/index.html', 'w')
fp.write(driver.page_source)
fp.close()
print('取得完成')

driver.quit()