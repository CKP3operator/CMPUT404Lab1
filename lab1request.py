import requests

#print(requests.__version__)
r = requests.get('https://raw.githubusercontent.com/CKP3operator/CMPUT404Lab1/main/lab1request.py')
print(r.text)