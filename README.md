# Project: Form Validator

User data validation system, built on a django framework using JavaScript and REST APIs, which detects fake data entered by the user

# ⌛ Project Demo

https://user-images.githubusercontent.com/66905080/147885041-d89d6091-889a-478b-b891-d260f23f3299.mp4

## 👇 Install
###### This project requires Django and the following Python libraries installed:

* [Django](https://pypi.org/project/Django/)
* [Requests](https://pypi.org/project/requests/)
* [Jinja](https://pypi.org/project/Jinja2/)


If you do not have Python installed yet, it is highly recommended that you install the python.
### OR 
All required libraries are included in the file ```requirements.txt```


# 🚀  Installation
Clone the repo
```
git clone https://github.com/Nitesh639/valideter.git

```
Change your directory to the cloned repo
```
cd valideter
```
Now, run the following command in your Terminal/Command Prompt to install the libraries required
```
pip3 install -r requirements.txt
```

# 💡 Working
To run the website on the local server type the following command.
``` 
python manage.py runserver
```

# Project Description
* User goes to registration and enters their data.
* The data entered is checked first for format by Javascript and then The rest API checks if the data is fake/real
* If the data is real then it is stored in the database.
* The user can now login using his credentials is registeration is sucessfull.

# Utility
When such a system is implemented in a website, it prevents  fake user data and prevent creation of multiple accounts using forged data.

### [Feel free to report issues and suggest any changes.](https://github.com/Nitesh639/valideter/issues)
