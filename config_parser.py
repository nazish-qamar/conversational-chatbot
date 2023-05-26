from configparser import ConfigParser

file="config.ini"
config=ConfigParser()
config.read(file)

print(config.sections())

print(config['token'])

"""
config.add_section('new_section')
config.set('new_section','key','value')

with open(file, "w") as conf:
    config.write(conf)
"""