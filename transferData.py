import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def uploadFile(self, source, dest):
        dbx = dropbox.Dropbox(self.access_token)

        with open(source, 'rb') as f:
            dbx.files_upload(f.read(), dest)
    

def main():
    access_token = 'sl.Ax4mhrdIFi83lawbda4Xxjz20GH9vpq5VhfyS2cMHaYlyC1vfZIjvuX68N70EvhxD4nS85NckWEL_kjoF8Az4g3YrrivmpfeNt60paI8vdN_InIgOgazKNLDOvk3RPai2stHqoFoTQg'
    backup = TransferData(access_token)

    source = input('Enter the source file : ')
    dest = input('Enter the destination file: ')

    backup.uploadFile(source,dest)
    print('The file is uploaded.')

main()

