import json

person = [
    {
        'username':"何小韩",
        'age':19,
        'country':'四川'
    },
    {
        'username': "lisi",
        'age': 20,
        'country': '四川'
    }
]
with open('person.json','w',encoding='utf-8') as fp:
    json.dump(person,fp,ensure_ascii=False)

# loads将string字符串变成python对象
json_str = '[{"username": "何小韩", "age": 19, "country": "四川"}, {"username": "lisi", "age": 20, "country": "四川"}]'
persons = json.loads(json_str)
# print(type(persons))
# for person in persons:
    # print(person)

with open('person.json','r',encoding='utf-8') as fp:
    persons = json.load(fp)
    print(type(persons))
    for person in persons :
        print(person)



