import os
import base64
from email.message import EmailMessage
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set the required Gmail API scope
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# Path to credentials from environment
creds_path = os.environ.get("GMAIL_CREDENTIALS_PATH")

def get_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def create_message(sender: str, to: str, subject: str, body_text: str) -> dict:
    message = EmailMessage()
    message.set_content(body_text)
    message["To"] = to
    message["From"] = sender
    message["Subject"] = subject
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": encoded_message}

def send_email(sender: str, to: str, subject: str, body_text: str):
    try:
        service = get_service()
        message = create_message(sender, to, subject, body_text)
        result = service.users().messages().send(userId="me", body=message).execute()
        print(f"Message sent. ID: {result['id']}")
    except HttpError as error:
      print(f"An error occurred: {error}")
      try:
          print(json.loads(error.content.decode()))
      except Exception:
          pass



if __name__ == "__main__":
    send_email(
        sender="", #enter a valid gmail email address, make sure it's added as a valid test user to the Google Cloud project.
        to="", #enter who you want to send an email to
        subject="Test Email from Gmail API",
        body_text="This is a test email sent via Gmail API."
    )
