#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == "__main__":

    import operator
    import csv
    import datetime

    with open('/acme_worksheet.csv', 'r') as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')

        next(csv_reader)

        date_list = []
        name_list = []
        name_dict = {}

        for line in csv_reader:
            # Виділяю основні частини
            name = line[0]
            date = line[1]
            work_time = line[2]
            # Форматую дату
            old_data = datetime.datetime.strptime(date, "%b %d %Y")
            date = old_data.strftime("%Y-%m-%d")

            date_list.append(date)
            name_list.append(name)

            #  створюю словник словників {ім'я : {дата:години}}
            if name not in name_dict.keys():

                name_dict[name] = {}
            new_items = name_dict.get(name)
            new_items[date] = work_time

        date_list = sorted(list(set(date_list)))

        name_list = sorted(list(set(name_list)))

    table = []

    sorted_list_by_names = sorted(
        name_dict.items(), key=operator.itemgetter(0))
    print(sorted_dict_by_names)

    # Заповнюю list для створення таблиці
    for values in sorted_list_by_names:
        row = []
        row.append(values[0])

        for date in date_list:
            if date in values[1].keys():
                row.append(values[1][date])
            else:
                row.append('0')

        table.append(row)

    date_list.insert(0, "Name/Date")

    with open('new_acme_worksheet.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(date_list)
        csv_writer.writerows(table)
