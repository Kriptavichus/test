def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Невозможно прочитать строку: {line}")
                    continue

            if count == 0:
                return 0, 0

            average = total // count  
            return total, average

    except FileNotFoundError:
        print(f"Файл по пути '{path}' не найден.")
        return 0, 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0, 0
    
total, average = total_salary("dz4")
print(f"Общая сумма заработной платы: {total}, Средняя заработная плата: {average}")
  