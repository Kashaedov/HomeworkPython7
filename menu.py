import actions
import export as ex


def start_menu():
    print("Доброго времени суток! \nВас приветствует планировщик недели!\nЧтобы работать с планировщиком - введите нужный Вам пункт!")
    while True:
        act = int(input('\n Выберите действие: \n 1. Добавить событие в ежедневник \n 2. Показать ежедневник \n 3. Экспорт \n 4. Выход из меню \n '))
        if act == 4:
            break
        elif act == 1:
            days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
            for key, value in days.items():
                print(key, ':', ''.join(str(x) for x in value))
            day = days[int(input('Выберите день недели: '))]
            time = input('Запишите время события: ')
            event = input('Событие: ')
            actions.write_event(day, time, event)
        elif act == 2:
            actions.show_calendar()
        else:
            extension = ''
            type = int(input('Укажите расширене для экспорта: \n 1. scv\n 2. html \n '))
            if type == 1:
                extension = 'scv'
            elif type == 2:
                extension = 'html'
            ex.export(extension)