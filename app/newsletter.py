from emaildb import users
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.environ.get("NEWS_API_KEY")


email_sender = "hoolynews@gmail.com"
password = os.environ.get("MAILER_PASSWORD")


def send_newsletter(email, content):

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email
    msg['Subject'] = 'Your Hooly Newsletter is Here'

    msg.attach(MIMEText(content, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, password)
    server.sendmail(email_sender, email, msg.as_string())
    server.quit()

    return


def generate_newsletter():
    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={apiKey}"

    r = requests.get(url=url)
    r = r.json()

    articles = r['articles']

    email_content = None

    if not articles:
        print("Couldn't fetch articles.")
    else:
        email_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                /* Add your CSS styles here */
                .container {
                    font-family: Arial, sans-serif;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f7f7f7;
                }

                h1 {
                    color: #0070c0;
                    font-size: 32px;
                    margin-bottom: 20px;
                    text-align: center;
                }

                p {
                    font-size: 16px;
                }

                ul {
                    list-style: none;
                    padding: 0;
                }

                li {
                    margin-bottom: 20px;
                    padding: 10px;
                    background-color: #fff;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }

                h4 {
                    color: #333;
                    font-size: 20px;
                    margin: 0;
                }

                p.article-content {
                    font-size: 16px;
                    margin: 10px 0;
                }

                img {
                    max-width: 100%;
                    height: auto;
                }

                a {
                    color: #0070c0;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>hooli news</h1>
                <p>Welcome to our newsletter! Here are the latest news headlines:</p>
                <ul>
        """

        for article in articles:
            email_content += '<li>'
            email_content += f'<h4>{article["title"]}</h4>'
            email_content += f'<p class="article-content">{article["content"]}</p>'
            
            if article["urlToImage"]:
                email_content += f'<img src="{article["urlToImage"]}" alt="Article Image">'
            
            email_content += f'<a href="{article["url"]}">Read more</a>'
            email_content += '</li>'

        email_content += """
                </ul>
            </div>
        </body>
        </html>
        """

    return email_content

def do_the_job():
    subscribers = list(users.find())

    content = generate_newsletter()

    # content = """ <h1> Garbage arrived !</h1>"""

    for subscriber in subscribers:
        subscriber_email = subscriber["email"]
        send_newsletter(subscriber_email, content)


# schedule.every(1).minutes.do(do_the_job)

# num = 3

# while num:
#     print("Mailing Started!")
#     num -= 1
#     schedule.run_pending()
#     time.sleep(1)

do_the_job()

print("All mails sent!")
