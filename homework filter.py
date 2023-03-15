def func(work):
    if work == work[::-1]:
        return work

inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

result = list(filter(func, inputdata))

print('result:', result)