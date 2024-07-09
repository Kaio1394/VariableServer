import os
from datetime import datetime

FILE_NAME = "ApiVariable-"

global data
global date_now

class Log:
    def __init__(self, path_system, path_error):
        if os.path.isdir(path_system) and os.path.isdir(path_error):
            self.path_system = path_system
            self.path_error = path_error
        else:
            raise Exception("Diretório não existe!")
    
    def info(self, text: str):
        tag = ""
        hour = datetime.now().strftime('%H')
        date_now = datetime.now().strftime('%Y%m%d-%H:%M:%S')
        name_file = FILE_NAME + hour
        full_path = self.path_system + f'/{name_file}'
        if os.path.exists(full_path):
            tag = 'a'
        else:
            tag = 'w'

        with open(full_path, tag) as file:
            if tag == 'a': file.write(f'\r\n{date_now} [INFO] ' + text)
            else: file.write(f'{date_now} [INFO] ' + text)

    def error(self, text: str):
        tag = ""
        hour = datetime.now().strftime('%H')
        date_now = datetime.now().strftime('%Y%m%d-%H:%M:%S')
        name_file = FILE_NAME + hour
        full_path = self.path_error + f'/{name_file}'
        if os.path.exists(full_path):
            tag = 'a'
        else:
            tag = 'w'

        with open(full_path, tag) as file:
            if tag == 'a': file.write(f'{date_now} [ERROR] ' + text)
            else: file.write(f'{date_now} [ERROR] ' + text)