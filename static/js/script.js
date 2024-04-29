let usernamereturnvalue = true;
let passwordreturnvalue = true;
let usernamevalue="";
let options = document.getElementById('options');
let username = document.getElementById('username');
let usernamesec = document.getElementById('username-sec');
let passwordsec = document.getElementById('password-sec');
let QRSection = document.getElementById('QR-section');
let password = document.getElementById('password');
let backwardName = document.getElementById('backward-name');
let usernameErrorMessage = document.getElementById('username-error-message');
let passwordErrorMessage = document.getElementById('password-error-message');
function OnUserNameChange(input)
{
    if (!usernamereturnvalue && input.value.trim() !== '')
    {
        username.classList.remove("redinput");
        usernameErrorMessage.style = "display:none;";
    }
    if (!usernamereturnvalue && input.value.trim() === '')
    {
        username.classList.add("redinput");
        usernameErrorMessage.style = "display:block;"; // Clear any previous error message
    }
}
function validateName() {
    // Check if username and password fields are empty
    if (username.value.trim() === '') {
        usernameErrorMessage.style = "display:block;"
        username.classList.add("redinput");
        usernamereturnvalue=false;
    } else {
        usernameErrorMessage.style = "display:none;"; // Clear any previous error message
        username.classList.remove("redinput");
        usernamesec.classList.add("animate__fadeOutLeft");
        usernamevalue = username.value;
        backwardName.textContent = usernamevalue;
        setTimeout(()=>{
            options.style="display:none";
            usernamesec.style="display:none;";
            passwordsec.style="display:block;";
            passwordsec.classList.add("animate__fadeInRight");    
        }, 200);
        usernamereturnvalue=true;
    }
    return usernamereturnvalue;
}

function OnPasswordChange(input)
{
    if (!passwordreturnvalue && input.value.trim() !== '')
    {
        password.classList.remove("redinput");
        passwordErrorMessage.style = "display:none;";
    }
    if (!passwordreturnvalue && input.value.trim() === '')
    {
        password.classList.add("redinput");
        passwordErrorMessage.style = "display:block;"; // Clear any previous error message
    }
}

function validateForm(e) {
    e.preventDefault();
    if (password.value.trim() === '') {
        passwordErrorMessage.style = "display:block;"
        password.classList.add("redinput");
        passwordreturnvalue=false;
    } else {
        passwordErrorMessage.style = "display:none;"; // Clear any previous error message
        password.classList.remove("redinput");
        passwordsec.classList.add("animate__fadeOutLeft");
        setTimeout(()=>{
            passwordsec.style="display:none;";
            QRSection.style = "display:block;";
            QRSection.classList.add("animate__fadeInRight");    
        }, 200);
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: username.value, password: password.value })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            // Handle successful response from server
            console.log(data);
        })
        .catch(error => {
            // Handle error
            console.error('Error:', error);
        });
        passwordreturnvalue=true;
    }
    
    return passwordreturnvalue;
}

function GoBack()
{
    passwordErrorMessage.style = "display:none;"; // Clear any previous error message
    password.classList.remove("redinput");
    passwordsec.classList.add("animate__fadeOutLeft");
    setTimeout(()=>{
        options.style="display:flex;";
        passwordsec.classList.remove("animate__fadeInRight");
        passwordsec.classList.remove("animate__fadeOutLeft");
        passwordsec.style="display:none;";
        usernamesec.style="display:block;";
        usernamesec.classList.remove("animate__fadeOutLeft");    
    }, 200);
        passwordreturnvalue=true;
}