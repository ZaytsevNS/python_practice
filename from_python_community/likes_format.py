# Вам нужно создать систему лайков, как в Facebook. 
# То есть функция принимает имена людей, которым нравится этот пост и возвращает его в виде красивой строки.

# Примеры:

# likes_format([]) -->  "no one likes this"
# likes_format(["Peter"]) -->  "Peter likes this"
# likes_format(["Jacob", "Alex"]) -->  "Jacob and Alex like this"
# likes_format(["Max", "John", "Mark"]) -->  "Max, John and Mark like this"
# likes_format(["Alex", "Jacob", "Mark", "Max"])  -->  "Alex, Jacob and 2 others like this"

def likes_format(names: list) -> str:
    if not names:
        return "no one likes this"
    type1: str = "{} likes this"
    type2: str = "{} and {} like this"
    type3: str = "{}, {} and {} like this"
    type4: str = "{}, {} and {} others like this"
    len_names: int = len(names)
    if len_names == 1:
        return type1.format(names[0])
    elif len_names == 2:
        return type2.format(names[0], names[1])
    elif len_names == 3:
        return type3.format(names[0], names[1], names[2])
    else:
        return type4.format(names[0], names[1], len_names - 2)
        
print(likes_format(["Alex", "Jacob", "Mark", "Max"]))