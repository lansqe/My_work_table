from copy import deepcopy, copy


class Character:

    def __init__(self, race: str, class_char: list[str], level: int):
        self.race = race
        self.class_char = class_char
        self.level = level

    def skills(self):
        if self.race == 'Elf':
            side = input('Light or darkness?').title()

            if isinstance(self.class_char, list):
                self.class_char = ' '.join(map(str, self.class_char))

            self.class_char = ' '.join([self.class_char, side])

        return [f'{self.race}, {[self.class_char]}, {self.level}']


c1 = Character('Elf', ['Priest'], 13)
print(c1.skills())

d1 = copy(c1)
d1.class_char += ' and darkness'

print(d1.class_char)
print(c1.class_char)

lst1 = [1, 2, 3, 4, [5, 6, 7]]
copy_lst1 = copy(lst1)
copy_lst1[4].append(32)

print(copy_lst1)
print(lst1)

deepcopy_lst1 = deepcopy(lst1)
deepcopy_lst1[4].append(12)

print(deepcopy_lst1)
print(copy_lst1)
print(lst1)
