def export(extension):
    with open('calendar.txt', 'r+') as data:
        exp = data.readlines()
        for text in exp:
            with open(f'Diary.{extension}', 'w') as file:
                file.writelines(text)