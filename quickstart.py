from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from mmap import mmap,ACCESS_READ
from xlrd import open_workbook,cellname,XL_CELL_TEXT
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

#ListFolder('root')

myfile = drive.CreateFile({
    "id": "0B4p_kPMS8cz7SGhrZExmVDlqTUE"
})

myfile.GetContentFile('abc.csv')


book = open_workbook('abc.csv')
print book.nsheets
sheet = book.sheet_by_index(0)
print sheet.name
print sheet.nrows
print sheet.ncols

# Introspecting a Sheet 

#for row_index in range(sheet.nrows):
# for col_index in range(sheet.ncols):
#  print cellname(row_index,col_index),'-',
#  print sheet.cell(row_index,col_index).value

# Getting a particular Cell

cell = sheet.cell(0,0)
print cell
print cell.value
print cell.ctype==XL_CELL_TEXT

for i in range(sheet.ncols):
 print sheet.cell_type(1,i),sheet.cell_value(1,i)

#Iterating over the contents of a Sheet
#print sheet.row(0)
#print sheet.col(0)



#print open_workbook('pr06.csv')


# commands to manipulate the file

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


