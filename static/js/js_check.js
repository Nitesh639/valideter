function js_check(){
    document.getElementById("click").innerHTML="Checking";
    var username=document.getElementById('username').value;
    var email=document.getElementById('email').value;
    var number=document.getElementById('number').value;
    var password=document.getElementById('password').value;
    var again_password=document.getElementById('again_password').value;
    var unamergx = /^[a-z A-Z 0-9]+$/;
    var emailrgx = /^([a-z A-Z 0-9 \. _ -]+)@([a-z A-Z 0-9 -]+).([a-z]+)(.[a-z]+)?$/;
    var numberrgx = /^[0-9]{10}$/;


if (password == username) {
    document.getElementById("pproblem").innerHTML="*username and password is same";
    document.getElementById("click").innerHTML="Password problem";
    document.getElementById("click").style.backgroundColor="red";
    return false;
}
else if (password == email) {
    document.getElementById("pproblem").innerHTML="*email and password is same";
    document.getElementById("click").innerHTML="Password problem";
    document.getElementById("click").style.backgroundColor="red";
    return false;
}
else if (password == number) {
    document.getElementById("pproblem").innerHTML="*number and password is same";
    document.getElementById("click").innerHTML="Password problem";
    document.getElementById("click").style.backgroundColor="red";
    return false;
}
else if (password.length < 6) {
    document.getElementById("pproblem").innerHTML="*password is too short";
    document.getElementById("click").innerHTML="Password problem";
    document.getElementById("click").style.backgroundColor="red";
    return false;
}
else if (password != again_password){
    document.getElementById("pproblem").innerHTML="*both passwords are not matching";
    document.getElementById("click").innerHTML="Password problem";
    document.getElementById("click").style.backgroundColor="red";
    return false
}
else {
    if(unamergx.test(username) == false)
    {
        document.getElementById("pproblem").innerHTML="*only alphabet and digits";
        document.getElementById("click").innerHTML="Wrong username"
        document.getElementById("click").style.backgroundColor="red";
        return false
    }
    else if (emailrgx.test(email) == false) {
        document.getElementById("pproblem").innerHTML="*email is not correct format";
        document.getElementById("click").innerHTML="Wrong email"
        document.getElementById("click").style.backgroundColor="red";
        return false
    }
    else if (numberrgx.test(number) == false) {
        document.getElementById("pproblem").innerHTML="*number should be 10 digits";
        document.getElementById("click").innerHTML="Wrong number"
        document.getElementById("click").style.backgroundColor="red";
        return false
    }
    else
    {
       return true
    }
}
}