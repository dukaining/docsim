from collections import abc


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = dict(mapping)

    
    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])


if __name__=='__main__':
    import json
    json_file = r'd:\temp\1.json'
    with open(json_file, encoding='utf-8') as fp:
        conf = json.load(fp)
    print(sorted(conf["Schedule"].keys()))

    for key, value in sorted(conf['Schedule'].items()):
        print('{:3} {}'.format(len(value), key))

    feed = FrozenJSON(conf)
    print(len(feed.Schedule.speakers))
    print(feed.Schedule.speakers[-1].name)