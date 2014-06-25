from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#from apiclient import errors
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

def ListFolder(parent):
  file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
  for f in file_list:
    print 'title: %s , id:%s ,mimeType: %s' % (f['title'],f['id'],f['mimeType'])
    if f['mimeType']=='application/vnd.google-apps.folder': # if folder
      ListFolder(f['id'])

ListFolder('root')

myfile = drive.CreateFile({
    "id": "0B4p_kPMS8cz7SGhrZExmVDlqTUE"
})

myfile.GetContentFile('pr06.csv')
# Auto-iterate through all files that matches this query
#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#for file1 in file_list:
#  print 'title: %s, id: %s' % (file1['title'], file1['id'])

#file2 = drive.CreateFile({'id': '0B4p_kPMS8cz7SVNIWExBeEZUdlk'}) # Create GoogleDriveFile instance with file id of file1
#print 'title: %s, mimeType: %s' % (file2['title'], file2['mimeType']) # title: HelloWorld.txt, mimeType: text/plain
#file2.FetchContent()
#ListFolder('Qualtrics-NDAR Conversion Docs')
#file2.GetContentString()
#file3 = drive.CreateFile({'Qualtrics-NDAR Conversion Docs': '0B4p_kPMS8cz7SVNIWExBeEZUdlk'})
#print file3.ListFiles


