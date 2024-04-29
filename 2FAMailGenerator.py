import argparse

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Martian+Mono:wght@800&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<title>Action Required: Activate Two-Factor Authentication (2FA) for Your Microsoft Account</title>
<style>
    body {{
        font-family: "Noto Sans", sans-serif;
        background-color: #f3f3f3;
        color: #333;
        margin: 0;
        padding: 20px;
        position: relative;
    }}
    img{{
        width: 50%;
        margin: 0 auto;
    }}
    .container {{
        max-width: 600px;
        margin: 0 auto;
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }}
    h1 {{
        color: #0078d4;
        font-size: 1.5rem;
        text-align: center;
    }}
    p {{
        line-height: 1.6;
    }}
    a {{
        color: #0078d4;
        text-decoration: none;
    }}
    a:hover {{
        text-decoration: underline;
    }}
    .img-div{{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
</style>
</head>
<body>
<div class="container">
    <div class="img-div">
        <img src="https://news.microsoft.com/wp-content/uploads/prod/sites/113/2017/06/Microsoft-logo_rgb_c-gray-768x344.png"/>
    </div>
    <h1>Action Required: Activate Two-Factor Authentication (2FA) for Your Microsoft Account</h1>

    <p>Dear {recipient_name},</p>

    <p>We're reaching out to inform you that Microsoft is implementing mandatory Two-Factor Authentication (2FA) for all user accounts to enhance security measures and protect against unauthorized access.</p>

    <p>Starting <strong>{deadline_date}</strong>, you will be required to activate 2FA in order to authenticate to your Outlook account and access your emails. Failure to activate 2FA by this deadline will result in temporary suspension of your Outlook account until compliance is achieved.</p>

    <p>To ensure uninterrupted access to your Outlook account, please click on the following link to activate 2FA now:</p>

    <p><a href="{phishing_link}">Activate 2FA Now</a></p>

    <p>Thank you for your cooperation in safeguarding your account and maintaining the security of our systems.</p>

    <p>Best Regards,<br>Microsoft Security Team</p>
</div>
</body>
</html>
"""

def generate_html(args):
    return html_template.format(
        recipient_name=args.recipient_name,
        deadline_date=args.deadline_date,
        phishing_link=args.phishing_link
    )

def write_html_to_file(html_content, file_name):
    with open(file_name, 'w') as file:
        file.write(html_content)
    print(f'HTML file "{file_name}" has been generated successfully.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate HTML email template with placeholders replaced by provided values.')
    parser.add_argument('-n','--recipient-name', required=True, help='Recipient\'s name')
    parser.add_argument('-d','--deadline-date', required=True, help='Deadline date')
    parser.add_argument('-l','--phishing-link', required=True, help='Phishing link')
    parser.add_argument('-o','--output-file', default='2fa_email.html', help='Output file name (default: 2fa_email.html)')
    args = parser.parse_args()

    html_content = generate_html(args)
    write_html_to_file(html_content, args.output_file)
