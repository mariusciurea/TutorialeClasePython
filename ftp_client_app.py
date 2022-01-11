from ftplib import FTP

# ftp = FTP()
# ftp.connect('192.168.0.105', 21)
# ftp.login('testuser', 'test123')
# # ftp.dir()
# ftp.cwd('/test')
# # ftp.dir()
# ftp.retrlines('LIST')
# remote_file = 'test.txt'
# local_file = 'local_test_file.txt'
#
# with open(local_file, 'w') as f:
#     ftp.retrlines(f'RETR {remote_file}', f.write)

class Client:
    ftp = FTP()
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def connet_to_server(self):
        Client.ftp.connect(self.hostname, self.port)
        Client.ftp.login(self.username, self.password)

    @staticmethod
    def download_file(local_file, remote_file):
        with open(local_file, 'w') as f:
            Client.ftp.retrlines(f'RETR {remote_file}', f.write)

# c1 = Client('192.168.0.105', 21, 'testuser', 'test123')
# c1.connet_to_server()
# remote_file = 'test.txt'
# local_file = 'local_test_file_2.txt'
# Client.ftp.cwd('/test')
# c1.download_file(local_file, remote_file)

c2 = Client('192.168.0.105', 21, 'testuser2', 'test123')
c2.connet_to_server()
remote_file = 'tutorial.txt'
local_file = 'local_tutorial.txt'
Client.ftp.cwd('/test/test_2')
c2.download_file(local_file, remote_file)







