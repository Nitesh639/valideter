from django.shortcuts import render
# this come from check.py file, in api python directory
from .api.check import email_check, phone_check
from .models import user, email_details, phone_details


# first page or index page
def index(request):
    return render(request, 'index.html')


# user registration page open by this function
def registration(request):
    return render(request, 'registration.html')


# user login page
def login(request):
    return render(request, 'login.html')


# show the data after login by the user
def user_status(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    datas = user.objects.filter(email=email)
    if (len(datas) != 0):
        for data in datas:
            if (data.email == email):
                if (data.password == password):

                    return render(request, 'user_status.html',
                                  {'about_email': data.email_detail, 'about_phone': data.phone_detail})
                else:
                    return render(request, 'login.html', {'e': "user or password is not match"})
            else:
                return render(request, 'login.html', {'e': "user or password is not match"})
    else:
        return render(request, 'login.html', {'e': "user or password is not match"})


# this function for the storing the data if every thing going fine
def status(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    number = request.POST.get('number')
    password = request.POST.get('password')
    again_password = request.POST.get('again_password')
    CR_email = user.objects.filter(email=email)
    CR_number = user.objects.filter(number=number)
    if (len(CR_email) != 0):
        return render(request, 'registration.html',
                      {'msg': 'email already exist', 'username': username, 'email': email, 'number': number,
                       'password': password, 'again_password': again_password})
    elif (len(CR_number) != 0):
        return render(request, 'registration.html',
                      {'msg': 'number already exist', 'username': username, 'email': email, 'number': number,
                       'password': password, 'again_password': again_password})
    else:
        email_val = email_check(email)
        email_status = email_val[0]
        about_email = email_val[1]
        phone_val = phone_check(number)
        phone_status = phone_val[0]
        about_phone = phone_val[1]
        if (email_status == True and phone_status == True):
            data_email = email_details(email_address=about_email['email_address'], domain=about_email['domain'],
                                       valid_syntax=about_email['valid_syntax'],
                                       disposable=about_email['disposable'], webmail=about_email['webmail'],
                                       deliverable=about_email['deliverable'],
                                       gibberish=about_email['gibberish'], spam=about_email['spam'])
            data_number = phone_details(status=about_phone['status'], phone=about_phone['phone'],
                                        phone_valid=about_phone['phone_valid'],
                                        phone_type=about_phone['phone_type'], phone_region=about_phone['phone_region'],
                                        country=about_phone['country'], country_code=about_phone['country_code'],
                                        country_prefix=about_phone['country_prefix'],
                                        international_number=about_phone['international_number'],
                                        local_number=about_phone['local_number'],
                                        e164=about_phone['e164'], carrier=about_phone['carrier'])

            data_user = user(username=username, password=password, number=number, email=email, email_detail=data_email,
                             phone_detail=data_number)
            data_number.save()
            data_email.save()
            data_user.save()
            return render(request, 'validator_result.html',
                          {'email_status': email_status, 'about_email': about_email, 'phone_status': phone_status,
                           'about_phone': about_phone, 'result': 'Completed', })
        else:
            return render(request, 'validator_result.html',
                          {'email_status': email_status, 'about_email': about_email, 'phone_status': phone_status,
                           'about_phone': about_phone, 'result': 'Not Completed'})
