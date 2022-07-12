import configparser

def main():
    ACCESS_KEY_ID = ''
    ACCESS_SECRET_KEY = ''

    config = configparser.RawConfigParser()

    print (config.read('~/.aws/credentials')) ## []
    print (config.sections())                 ## []
    ACCESS_KEY_ID = config.get('default', 'aws_access_key_id') ##configparser.NoSectionError: No section: 'default'
    print(ACCESS_KEY_ID)

if __name__ == '__main__':
    main()