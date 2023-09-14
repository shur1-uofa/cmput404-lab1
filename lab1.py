import requests


# print( requests.__version__ )

#resp = requests.get( "http://www.google.com" )
resp = requests.get( "https://raw.githubusercontent.com/shur1-uofa/cmput404-lab1/master/lab1.py" )
print(resp.text)
