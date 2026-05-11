import os
import requests
import rq
import jinja2

from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)

def send_simple_message(to, subject, body, html):
    api_key = os.getenv("MAILGUN_API_KEY")
    response = requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages",
        auth=("api", api_key),
        data={"from": f"Olivier Q-B <postmaster@{DOMAIN}>",
            "to": [to],
            "subject": subject,
            "text": body,
            "html": html,
            })
    response.raise_for_status()
    return response


def send_user_registration_email(email, username):
    return send_simple_message(
        email, 
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
        render_template("email/action.html", username=username)
    )
