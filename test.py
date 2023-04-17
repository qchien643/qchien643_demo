import requests

url = 'https://qchien643.github.io/qchien643_demo/'
myObj = {'somekey':'somevalue'}

x = requests.post(url , json=myObj)

print(x.text)