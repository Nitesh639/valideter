import requests
def email_check(email):
    url = "https://api.eva.pingutil.com/email?email="+email
    response = requests.get(url)
    data = response.json()
    valid = data['data']
    if (valid['valid_syntax'] == True and valid['webmail'] == True and valid['deliverable'] == True and valid['gibberish'] == False and valid['spam'] == False and valid['disposable'] == False):
        return [True,valid]
    else:
        return [False, valid]

def phone_check(number):
    url = "https://veriphone.p.rapidapi.com/verify"

    querystring = {"phone": number}

    headers = {
        'x-rapidapi-host': "veriphone.p.rapidapi.com",
        'x-rapidapi-key': "34262c539amsh117b337c7ab904fp198546jsn3cb7619c8fb4"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    values = response.json()
    if(values['status'] == "success" and values['phone_valid']==True and values['phone_type'] != "unknown" and values['carrier'] != ""):
        return [True,values]

    else:
        return [False,values]