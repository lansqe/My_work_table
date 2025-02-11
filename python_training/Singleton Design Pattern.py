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
