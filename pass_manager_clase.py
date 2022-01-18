import os
import rsa

class PassManager:
    def __init__(self, file, app='', password=''):
        self.file = file
        self.app = app
        self.password = password
        if os.path.exists(self.file) == False:
            with open(self.file, 'w') as f:
                pass

    @staticmethod
    def menu():
        option = ''
        while option != '1' and option != '2' and option != '3':
            option = input(
                '1.Salveaza o parola\n'
                '2.Alege aplicatia pentru care sa vezi parola\n'
                '3.Vezi toate parolele\n'
                'Alege o optiune:'
                            )
        return option

    def input_app(self):
        self.app = input('Introduceti aplicatia: ')

    def input_password(self):
        self.password = input('Introduceti parola: ')

    def write_to_file(self, mode, content):
        with open(self.file, mode) as f:
            f.write(content)

    def read_from_file(self, mode, whole=False):
        if whole == False:
            with open(self.file, mode) as fr:
                file_content = fr.readlines()
                return file_content
        with open(self.file, mode) as fr:
            file_content = fr.read()
            return file_content


    def save_data_to_file(self):
        file_content = self.read_from_file('r', whole=True)
        if self.app in file_content:
            print('Aplicatia exista in fisier')
        else:
            self.write_to_file('a', f'{self.app}: {self.password}\n')

    def encrypt_file(self):
        pubkey, privkey = rsa.newkeys(1024)
        with open(f'keys/public.pem','wb') as fw:
            fw.write(pubkey.save_pkcs1('PEM'))
        with open(f'keys/private.pem','wb') as fw:
            fw.write(privkey.save_pkcs1('PEM'))

        content = self.read_from_file('r', whole=True)
        enc_content = rsa.encrypt(content.encode('utf-8'),pubkey)

        self.write_to_file('wb', enc_content)

    def decrypt_file(self):
        if os.path.exists(self.file) and os.path.getsize(self.file) > 0:
            with open(f'keys/private.pem', 'rb') as fr:
                priv_key = rsa.PrivateKey.load_pkcs1(fr.read())

            content = self.read_from_file('rb', whole=True)
            decrypted_content = rsa.decrypt(content, priv_key)

            self.write_to_file('w', decrypted_content.decode('utf-8'))

pm = PassManager('password_manager_file.txt')
pm.decrypt_file()
option = ''
while option.upper() != 'Y':
    option = pm.menu()
    if option == '1':
        pm.input_app()
        pm.input_password()
        pm.save_data_to_file()
    elif option == '2':
        pm.input_app()
        file_content = pm.read_from_file('r', whole=False)
        print('*' * 33)
        for line in file_content:
            if pm.app in line:
                print(line.strip())
        print('*' * 33)
    elif option == '3':
        print('*' * 33)
        file_content = pm.read_from_file('r', whole=True)
        print(file_content.strip())
        print('*' * 33)

    option = input('Vrei sa iesi? [Y/N]')
    if option.upper() == 'Y':
        pm.encrypt_file()