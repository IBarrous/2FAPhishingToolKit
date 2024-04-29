import argparse

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Urgent: Review of Attached Document Required</title>
<style>
    body {{
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }}
    .container {{
        max-width: 600px;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        background-color: #f9f9f9;
    }}
    h1 {{
        color: #333;
    }}
    p {{
        color: #666;
    }}
</style>
</head>
<body>
<div class="container">
    <h1>Urgent: Review of Attached Document Required</h1>
    <p>Dear {target},</p>
    <p>We're excited to have you on board!</p>
    <p>Your insights are valuable to us, which is why we're reaching out to ask for your review of the attached document titled "<strong>{document_title}</strong>". Your input will help us move forward with confidence.</p>
    <p>We understand you're just getting started, but your contribution matters. Please take a moment to review the document at your earliest convenience.</p>
    <p>Thank you for your attention to this matter. We look forward to your feedback!</p>
    <p>Best regards,</p>
    <p>{your_name}<br>{your_position}<br>{your_contact}</p>
</div>
</body>
</html>
"""


def fill_template(target, document_title, your_name, your_position, your_contact):
    return html_template.format(target=target,
                                document_title=document_title,
                                your_name=your_name,
                                your_position=your_position,
                                your_contact=your_contact)

def write_html_to_file(html_content, file_name):
    with open(file_name, 'w') as file:
        file.write(html_content)
    print(f'HTML file "{file_name}" has been generated successfully.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate HTML email template with placeholders replaced by provided values.')
    parser.add_argument('-t','--target', required=True, help='Target\'s name')
    parser.add_argument('-d','--document-title', required=True, help='Title of the attached document')
    parser.add_argument('-n','--your-name', required=True, help='Your name')
    parser.add_argument('-p','--your-position', required=True, help='Your position')
    parser.add_argument('-c', '--your-contact', required=True, help='Your contact information')
    parser.add_argument('-o', '--output-file', default='review_email.html', help='Output file name (default: review_email.html)')
    args = parser.parse_args()

    html_content = fill_template(args.target, args.document_title, args.your_name, args.your_position, args.your_contact)
    write_html_to_file(html_content, args.output_file)
