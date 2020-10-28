# pip install requests
# pip freeze > requirements
# pip install -r requirements.txt
# pap lib

import json
import requests


#
# url = 'https://yandex.ru/'
#
# response = requests.get(url)
# file = open('yandex.html', 'wb')
# try:
#     file.write(response.content)
# except IOError:
#     pass
# finally:
#     file.close()
# print(1)

# with open('text.txt', 'r', encoding='UTF-8')as file:
#     # for line in file:
#     #     print(line)
#     lines = file.readline()
#     print(lines)

data ={
    'name':'Sergei',
    'surname': 'Romanov',
    'age':33,
    'post':[1,2,3,4,5,6],
    'writer': True,
    'tags':(1,2,3,4,5),
    # 'sets':{1,2,3,4}
}
with open('test.json', 'w', encoding='UTF-8')as file:
    file.write(json.dumps(data))    #loads - десюриалезовать
