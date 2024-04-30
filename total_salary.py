def total_salary(path):
    try:
        with open (path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
            total_salary = 0
            for line in lines:
                salary = int(line.strip().split(',')[1])
                total_salary += salary
            avarage_salary = int(total_salary / len(lines))
            return total_salary, avarage_salary
    except FileNotFoundError:
        print(f'Файл {path} не знайдено')
        return 0, 0
    except Exception as e:
        print(f'Помилка: {e}')
        return 0, 0


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
