import configparser
CONF_FILE = "../config.ini"


class Configurations:
    def __init__(self):
        self.loc_tokens = {}

    def read_config(self):
        config = configparser.ConfigParser()
        config.read(CONF_FILE)
        return self.loc_tokens


"""
config.add_section('new_section')
config.set('new_section','key','value')

with open(file, "w") as conf:
    config.write(conf)
"""
