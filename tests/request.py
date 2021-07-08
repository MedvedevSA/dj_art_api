import requests
# подготовка параметров для POST-запроса
param = {'title': 'value1', 'description': 'value2'}
# обратите внимание, что для метода POST, аргумент для 
# передачи параметров в запрос отличается от метода GET  
resp = requests.post("http://localhost:8000/api/tutorials", data=param)
print(resp.text)