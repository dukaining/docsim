from common.frozenjson import FrozenJSON
import json

class Config(FrozenJSON):
    def __init__(self, config_file_name='./config.json'):
        self.config_file_name = config_file_name
        with open(config_file_name, encoding='utf-8') as fp:
            json_mapping = json.load(fp)        
        FrozenJSON.__init__(self, json_mapping)


if __name__=='__main__':
    conf = Config(r'd:\temp\1.json')
    print(len(conf.Schedule.speakers))