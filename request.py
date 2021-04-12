import requests

url = 'https://hsiangfeng.github.io/'
response = requests.get(url)

if response.status_code == 200:
  fp = open('blog/index.html', 'w')
  fp.write(response.text)
  fp.close()
else:
  print('請求出現錯誤')


