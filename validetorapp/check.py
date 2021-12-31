import requests
email = input("Enter the email:")
url = "https://api.eva.pingutil.com/email?email="+email

response = requests.get(url)
data = response.json()
valid = data['data']
print(data['data'])
if (valid['valid_syntax'] == False):
    print("Not the valid syntax")

elif (valid['webmail'] == False):
    print("Enter the valid email")
elif (valid['deliverable'] == False):
    print("Enter the valid email")
else:
    print("succes")