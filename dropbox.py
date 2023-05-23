import dropbox


class TransferPhoto:
    def __init__(self, acess_token):
        self.token = acess_token

    def upload_data(self, path_from, path_to):
        dropbox__ = dropbox.Dropbox()
        with open(path_from, "r") as file:
            dropbox__.files_upload(file.read(), path_to)

def main():
    acess_token = ""
    TransferPhoto(acess_token).upload_data(
        "./Image.png", "https://www.dropbox.com/scl/fo/u0ai73y5ovij27wdktl02/h?dl=0&rlkey=hqtz6z87xbpqtk9u6hehzaa72")