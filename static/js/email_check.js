function email_check(){
    document.getElementById("click").innerHTML="Processing"
    var email=document.getElementById('email').value;
    var emailrgx = /^([a-z A-Z 0-9 \. _ -]+)@([a-z A-Z 0-9 -]+).([a-z]+)(.[a-z]+)?$/;



    if (emailrgx.test(email) == false) {
        document.getElementById("demail").innerHTML="*email is not correct formet"
        document.getElementById("click").innerHTML="Wrong email"
        document.getElementById("click").style.backgroundColor="red";
        return false
    }
    else
    {
       document.getElementById("click").innerHTML="JS Check Completed"
       return true
    }
}