class Character():

    _instance = None
    # Singleton
    '''Возвращается инстанция которая была создана в первый раз,
     новый экземпляр создаваться не будет'''
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.race = 'Elf'


c = Character()
d = Character()
d.race = 'Ork'
print(d.race)
print(c.race)


class Singleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self, setting1, setting2):
        self.setting1 = setting1
        self.setting2 = setting2


settings1 = AppSettings('value1', 'value2')
settings2 = AppSettings('value3', 'value4')

print(settings1 is settings2)
print(settings1.setting1)
