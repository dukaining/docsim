from common.frozenjson import FrozenJSON
import json
from common.singleton import Singleton

@Singleton
class Config(FrozenJSON):
    def __init__(self, config_file_name='./config.json'):
        self.config_file_name = config_file_name
        json_mapping = self.load_json_file()
        #with open(config_file_name, encoding='utf-8') as fp:
        #    json_mapping = json.load(fp)        
        FrozenJSON.__init__(self, json_mapping)

    def load_json_file(self):
        with open(self.config_file_name, encoding='utf-8') as fp:
            json_mapping = json.load(fp)  
        return json_mapping

    def reload(self):
        self.loadmapping(self.load_json_file())

if __name__=='__main__':
    conf1 = Config()
    conf2 = Config()
    print(conf1.Gensim.dictionaryFile)
    print(id(conf1))
    print(id(conf2))
    conf2.reload()
    print(conf2.Gensim.corpusFile)
