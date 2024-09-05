# да да, я и так прекрасно знаю что адекватные люди делают всё на базах данных и т.д
# мне удобнее так, я так привык, по этому не ебите мне мозги пожалуйста
# специально под вас, дорогие друзья, я написал комментарии
# даже не думайте что либо мне говорить за шифрование :)
# кому оно нужно в сервисе блядь продажи б/у техники

DIRECTORY = '' # директория с json файлами

import json

def save(filename:str, data, indenty=4, debug=False):
    '''
    Сохраняет json файлы (users.json, settings.json, sales.json, time.json)
    В filename идёт: users, settings, sales, time
    В data идут словари
    identy можно не заполнять, дефолтное значение - 4

    debug - boolean, опять же можно не заполнять,
    при значении True выводит в консоль успех загрузки файла

    Возвращает 1 - успешно, возвращает 0 - неудачно,
    при неудаче так же в консоль выводится ошибка
    '''
    with open(f'{DIRECTORY}{filename}.json', 'w', encoding='utf-8') as f:
        try:
            json.dump(data, f, ensure_ascii=False, indent=indenty)
            if debug:
                print(f'{filename} сохранён успешно!')
            return 1
        except Exception as ex:
            print(str(ex))
            return 0
        
def load(filename:str, debug=False):
    '''
    Открывает json файлы (users.json, settings.json, sales.json)
    В filename идёт: users, settings, sales

    debug - boolean, опять же можно не заполнять,
    при значении True выводит в консоль успех загрузки файла

    Возвращает данные если удачно, возвращает 0 если неудачно,
    при неудаче так же в консоль выводится ошибка
    '''
    with open(f'{DIRECTORY}{filename}.json', 'r', encoding='utf-8') as f:
        try:
            if debug:
                print(f'{filename} загружен успешно!')
            return json.load(f)
        except Exception as ex:
            print(str(ex))
            return 0
        
def find_key(key: str, value: str, dic: dict) -> list:
    """
    Возвращает список ключей, где значение по заданному ключу равно заданному значению.
    
    :param key: Ключ внутри вложенного словаря, который мы ищем.
    :param value: Значение, которое должно соответствовать.
    :param dic: Основной словарь, в котором проводится поиск.
    :return: Список ключей, удовлетворяющих условию.
    """
    matching_keys = [k for k, v in dic.items() if isinstance(v, dict) and v.get(key) == value]
    print(matching_keys)
    return matching_keys
