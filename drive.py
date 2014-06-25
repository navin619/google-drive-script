#!/usr/bin/python


import httplib2
import pprint


from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
#from oauth2client.client import flow_from_clientsecrets

#path_to_json="client_secrets.json"    # download from https://code.google.com/apis/console/
#AUTH_SCOPE ='https://www.googleapis.com/auth/drive'
#redirect_uri also provided in api console.The other URI mentioned there is for web applications.

#flow = flow_from_clientsecrets(Path_to_JSON,AUTH_SCOPE,redirect_uri="urn:ietf:wg:oauth:2.0:oob")

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Copy your credentials from the APIs Console
CLIENT_ID = '936897596528-cshqh20k97ls3jrou5u5aacb5bbnrh3d.apps.googleusercontent.com'
CLIENT_SECRET = 'oqRs8J_Sr6dEdZPBOza64I5I'


# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'



# Path to the file to upload
FILENAME = 'document.txt'


# Run through the OAuth flow and retrieve credentials
#flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE)
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print 'Go to the following link in your browser: ' + authorize_url
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)


# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)


drive_service = build('drive', 'v2', http=http)


# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
 'title': 'My document',
 'description': 'A test document',
 'mimeType': 'text/plain'
}


file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)
