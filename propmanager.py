import configparser
from cryptography.fernet import Fernet

class PropManager:
    cipher_suite = ''
    config = ''

    def __init__(self, key):
        self.config = configparser.ConfigParser(interpolation=None)
        self.config.read('config.ini')
        self.cipher_suite = Fernet(key.encode('utf-8'))
    
    def prop(self, propkey):
        prop = self.config.get('universities', propkey)
        decoded_prop = self.config.get('universities', propkey)
        try:
            decoded_prop = self.cipher_suite.decrypt(prop.encode('utf-8')).decode('utf-8')
        except:
            print('could not decode prop', propkey, 'defaulting to unencrypted mode')
        return decoded_prop
    
    def encrypt(self, data):
        encoded_prop = self.cipher_suite.encrypt(data)
        print(encoded_prop)