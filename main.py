import requests
from bs4 import BeautifulSoup
import pyperclip

from datetime import date
import time

print('Поиск ключа активации...')

today = str(date.today())
year = today[0:4]


url = f"https://gitee.com/superbeyone/J2_B5_A5_C4/blob/master/licenses/{year}/{today}.md"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

textAreaList = [textAreaElement.get_text() for textAreaElement in soup.find_all("textarea")]
code = textAreaList[1][1::]
pyperclip.copy(code)
print('Код активации скопирван в буфер обмена!\n')
print('Поддержать разработчика:\nBTC: 1JdA7pxnhjCisvXmUVArGP1vtiuCXrkeap\nUSDT TRC20: TYVhUdq6UemAGcPNaQkDn8A7UMTqV8jvHP\nTON: UQCb1uo-8iJ-2mlIpVj8nV-7JpafJPSwAk7qeQWgbut2wfx9\n')
exit = input('Нажмите Enter, чтобы выйти')

