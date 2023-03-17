from requests import get

print(get('http://localhost:8080/api/v2/news').json())
print(get('http://localhost:8080/api/v2/new/2').json())