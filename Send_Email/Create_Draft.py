import os
import base64
from email.message import EmailMessage
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define scope for writing email drafts
SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

# Load credentials from environment variable
creds_path = os.environ.get("GMAIL_CREDENTIALS_PATH")
if not creds_path:
    raise RuntimeError("GMAIL_CREDENTIALS_PATH environment variable is not set")

# Run OAuth flow and get Gmail API client
flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
creds = flow.run_local_server(port=0)
service = build("gmail", "v1", credentials=creds)

# Create the email message
msg = EmailMessage()
msg.set_content("This is a test draft from Python")
msg["To"] = "someone@example.com"
msg["From"] = "me"
msg["Subject"] = "Python Gmail Draft"

# Encode and send as draft
encoded_msg = base64.urlsafe_b64encode(msg.as_bytes()).decode()
draft_body = {"message": {"raw": encoded_msg}}
draft = service.users().drafts().create(userId="me", body=draft_body).execute()

print("✅ Draft created. ID:", draft["id"])
