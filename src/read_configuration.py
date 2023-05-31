import configparser
CONF_FILE = "config.ini"


class Configurations:
    def __init__(self):
        self.loc_tokens = {}

    @staticmethod
    def read_config():
        config = configparser.ConfigParser()
        config.read(CONF_FILE)
        return dict(config['DEFAULT'])


# testing
#print(Configurations().read_config()['start_token'])

"""
config.add_section('new_section')
config.set('new_section','key','value')

with open(file, "w") as conf:
    config.write(conf)
"""
