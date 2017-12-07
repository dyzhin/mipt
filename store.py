"""
Мы с вами реализуем собственный key-value storage.
Вашей задачей будет написать скрипт, который принимает в качестве аргументов ключи и значения
и выводит информацию из хранилища (в нашем случае — из файла)
"""

import argparse, sys, os, json, tempfile

parser = argparse.ArgumentParser(description='Store.')
parser.add_argument("--key")
parser.add_argument("--val")

params = vars(parser.parse_args())

#print(params)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.isfile(storage_path):
    #print("Пидарасы, где файл?!")
    dict_is_empty = True
elif not os.path.getsize(storage_path):
    #print("Вы мне пытаетесь подсунуть пустое файло!")
    dict_is_empty = True
else:
    dict_is_empty = False

if params["val"]:
    #print("Бля, это добавление нового слова!")
    #print(dict_is_empty)

    if dict_is_empty:
        jdict = {}
    else:
        with open(storage_path, 'r') as f:
            jdict = json.load(f)

    if params["key"] in jdict:
        jdict[params["key"]].append(params["val"])
    else:
        jdict[params["key"]] = [params["val"]]
    with open(storage_path, 'w') as f:
        json.dump(jdict,  f)
else:
    #print("Бля, это запрос к базе!")
    if dict_is_empty:
        #print("Негде, блядь, искать, словаря-то нет!")
        print(None)
    else:
        with open(storage_path, 'r') as f:
            jdict = json.load(f)
            #print(jdict)
            #print(params["key"])
            #print(params["val"])
            #print(params["key"] in jdict)
            if params["key"] in jdict:
                testvar = jdict[params["key"]]
                result = ""
                for i in range(len(testvar)):
                    result = result + testvar[i] + ", "*(i != len(testvar)-1)
                print(result)
            else:
                #print("Искали, но не нашли. Подите в хуй.")
                print(None)
