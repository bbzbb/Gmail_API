# Gmail_API
Learning to work with the Gmail API - will include further automation if necessary

1. Utilizing steps found here: https://mailtrap.io/blog/send-emails-with-gmail-api/ .
    1.1 Also found this: https://developers.google.com/identity/protocols/oauth2/#basicsteps
2. Create a project at the Google developers console: https://console.developers.google.com/
3. Enable the Gmail API.
4. Create OAuth Client ID for desktop app and received client_secret.json
5. send garbage and test mail to: https://maildrop.cc/inbox/
6. Run the following:

```

- python -m venv GMAIL_API
    -activate it with: GMAIL_API\Scripts\activate
- pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

```

7. Point the .py file towards the credentials.json you got from step #4.  I stored mine in an environment variable and called it for security purposes.
8. Walk through this to allow a test user so you don't have to publish you google project: https://stackoverflow.com/questions/75454425/access-blocked-project-has-not-completed-the-google-verification-process.
9. 