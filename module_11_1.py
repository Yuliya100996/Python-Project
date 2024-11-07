import requests
import pandas


# библиотека requests
response = requests.get('https://github.com/Yuliya100996/Python-Project/blob/main/module_10_5.py')
r = response.headers

print(response)
print(dir(response))
print(r)

print() # это для отступа
print()

# библиотека pandas
p = pandas.read_csv('test.txt')
print(p)
print(p.info())
print(p.tail())
