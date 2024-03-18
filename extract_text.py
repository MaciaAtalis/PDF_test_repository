import requests

url = "https://api.pdfrest.com/extracted-text"

payload = {
	
}

files = [
	('file', ('document_example.pdf', open('document_example.pdf', 'rb'), 'application/octet-stream'))
]

headers = {
    'Api-Key': '88a9c4df-fc2a-4e5b-9c7d-89ac642bd433'  
}

response = requests.request(
    "POST", url, headers=headers, data=payload, files=files)

print(response.text)