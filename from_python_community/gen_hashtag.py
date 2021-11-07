# Условие:

# Ваша задача — написать функцию, которая превращает строку в hashtag. 
# У них есть парочка правил: никаких символов из string.punctuation быть не должно, пробелы отсутствуют, а длина обязана быть не более 140 символов. 
# Если последнее правило нарушено, выбрасываем ошибку.

from string import punctuation


def gen_hashtag(s: str) -> str:
    k = []
    for i in s.split():
        i = i.title()
        for j in i:
            if j not in punctuation:
                k.append(j)
    if len("".join(k)) < 140:
        return f'#{"".join(k)}'
    else: return 'Error!'

s = 'i like python community!'
print(gen_hashtag(s))