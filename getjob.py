# https://www.104.com.tw/jobs/search/?keyword=Front%20end%20engineer&order=1&jobsource=2018indexpoc&ro=0
from selenium import webdriver
import re
# 請安裝相對應瀏覽器的 Driver
# https://sites.google.com/a/chromium.org/chromedriver/
driver = webdriver.Chrome('/Applications/Google Chrome.app/Contents/MacOS/chromedriver')

driver.implicitly_wait(10)

url = 'https://www.104.com.tw/jobs/search/?keyword=Front%20end%20engineer&order=1&jobsource=2018indexpoc&ro=0'

driver.get(url)

print(driver.title)

num = driver.find_element_by_css_selector('html body#job-jobList.job-list-body main div#main-content.l-content--2col.b-clearfix div.l-content--2col--main.l-container.jobs-content div#js-job-header.job-tab.b-clearfix div.b-float-left ul#js-job-tab.b-nav-tabs.job-type li.b-nav-tabs__active span.js-txt')

result = re.sub(r'[\(\)]','', num.text)

print('104 前端職缺目前全部有 => ', result , '個職缺')

driver.quit()