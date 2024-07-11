import os
import configparser

file_name_settings = os.getcwd() + "/appsettings.ini"

class Config:
    @staticmethod
    def extract(param: str) -> list:
        list_split = param.split(":")
        return list_split
    
    @staticmethod
    def parse(param: str) -> str:  
        """
        Format: TAG:PARAM -> Settings:name
        Ex: 
        [Settings]
        name="Test"
        """
        try:
            parse = configparser.ConfigParser()
            parse.read(file_name_settings)
            return parse[Config.extract(param)[0]][Config.extract(param)[1]]
        except:
            raise Exception("Variable not found")