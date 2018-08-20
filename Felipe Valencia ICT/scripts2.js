function response() {
    let name = document.getElementById("name").value;
    let lastname = document.getElementById("lastname").value;
    let email = document.getElementById("email").value;
    
    document.getElementById("out").innerHTML = "Thank you " + name +" " + lastname +" we have recieved your message and \nwill shortly be contacting you in the email address " + email;
}