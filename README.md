# 2FAPhishingToolKit
The Outlook 2FA Activation Phishing Toolkit is a collection of scripts and resources designed for conducting phishing attacks aimed at tricking users into providing their credentials for activating two-factor authentication (2FA) on their Outlook accounts. The toolkit includes features for hosting a fake Outlook login page, sending phishing emails, and managing email templates for various stages of the attack.

### Features
- **Fake Outlook Login Page:** Hosts a fake Outlook login page with Flask that prompts users to login to enable 2FA authentication (<b><i>HostWebsite.py</i></b>).
  ![first](https://github.com/IBarrous/2FAPhishingToolKit/assets/126162952/d9debd87-5c2c-4cfd-8663-e7a0c6bc37d3)
- **Phishing Email Sender:** A Python script for sending phishing emails to targets, including customizable email subjects, content and attachments (<b><i>sendmail.py</i></b>).
- **Email Templates:** Includes templates for two types of phishing emails:
  - Notification email: Notifies the target about the deadline to activate 2FA (<b><i>2FAMailGenerator.py</i></b>).
    ![second](https://github.com/IBarrous/2FAPhishingToolKit/assets/126162952/d5368f49-7a0c-4c6d-8e95-9c9db42e87d4)
  - Impersonation email: Impersonates the target and instructs another target to download a backdoor/payload/NTLMTheft ... (<b><i>ImpersonationMailGenerator.py</i></b>).

    ![third](https://github.com/IBarrous/2FAPhishingToolKit/assets/126162952/511eb65f-9525-4864-b976-e85669385509)

### Usage

### Disclaimer
This toolkit is for educational and testing purposes only. Unauthorized use of this toolkit for phishing or other malicious activities is strictly prohibited. Use at your own risk.
