
def get_cats_info(path):
    try:
        with open (path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
            cats = []
            for line in lines:
                line_strip = line.strip().split(',')
                cat_info = {'id': line_strip[0], 'name': line_strip[1], 'age': line_strip[2],}
                cats.append(cat_info)
            return cats
    except FileNotFoundError: 
        return f'Файл {path} не знайдено'
    except Exception as e:
        return f'Помилка: {e}'

cats_info = get_cats_info("cats_info.txt")
print(cats_info)