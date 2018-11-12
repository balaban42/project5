# Напишите программу вычисляющая за какое время человек сможет добраться из г. Новосибирска до ближайших городов
# разными способами передвижения. Нужные вам данные указаны в исходном файле input.txt.
# Рещение необходимо предоставить в новом файле output.txt. Значения необходимо округлить до десятых.
# Задание выполняется на англ. языке.


with open('input.txt', 'r') as f_in:
    with open('output.txt', 'w') as f_out:
        first_timeMash = round(230 / 80, 1)
        second_timeMash = round(265 / 80, 1)
        third_timeMash = round(265 / 80, 1)
        fourth_timeMash = round(370 / 80, 1)
        f_out.write('If a person was driving:')
        f_out.write('\n')
        first_time = str(first_timeMash)
        f_out.write('{} hours - in that time a person will get to Barnaul '
                    'from Novosibirsk.'.format(first_time))
        f_out.write('\n')
        second_time = str(second_timeMash)
        f_out.write('{} hours - in that time a person will get to Tomsk '
                    'from Novosibirsk.'.format(second_time))
        f_out.write('\n')
        third_time = str(third_timeMash)
        f_out.write('{} hours - in that time a person will get to Kemerovo '
                    'from Novosibirsk.'.format(third_time))
        f_out.write('\n')
        fourth_time = str(fourth_timeMash)
        f_out.write('{} hours - in that time a person will get to Novokuznetsk '
                    'from Novosibirsk.'.format(fourth_time))
        f_out.write(2 * '\n')

        first_timeBike = round(230 / 20, 1)
        second_timeBike = round(265 / 20, 1)
        third_timeBike = round(265 / 20, 1)
        fourth_timeBike = round(370 / 20, 1)

        f_out.write('If a person was riding a bike:')
        f_out.write('\n')
        first_time_bike = str(first_timeBike)
        f_out.write('{} hours - in that time a person will get to Barnaul '
                    'from Novosibirsk.'.format(first_time_bike))
        f_out.write('\n')
        second_time_bike = str(second_timeBike)
        f_out.write('{} hours - in that time a person will get to Tomsk '
                    'from Novosibirsk.'.format(second_time_bike))
        f_out.write('\n')
        third_time_bike = str(third_timeBike)
        f_out.write('{} hours - in that time a person will get to Kemerovo '
                    'from Novosibirsk.'.format(third_time_bike))
        f_out.write('\n')
        fourth_time_bike = str(first_timeBike)
        f_out.write('{} hours - in that time a person will get to Novokuznetsk '
                    'from Novosibirsk.'.format(fourth_time_bike))
        f_out.write(2 * '\n')

        first_timeFoot = round(230 / 7, 1)
        second_timeFoot = round(265 / 7, 1)
        third_timeFoot = round(265 / 7, 1)
        fourth_timeFoot = round(370 / 7, 1)

        if first_timeFoot < 24:
            first_days = 0
        elif 48 > first_timeFoot >= 24:
            first_days = 1
        elif first_timeFoot >= 48:
            first_days = 2
        first_time_hours = round(first_timeFoot - 24, 1)

        if second_timeFoot < 24:
            second_days = 0
        elif 48 > second_timeFoot >= 24:
            second_days = 1
        elif second_timeFoot >= 48:
            second_days = 2
        second_time_hours = round(second_timeFoot - 24, 1)

        if third_timeFoot < 24:
            third_days = 0
        elif 48 > third_timeFoot >= 24:
            third_days = 1
        elif third_timeFoot >= 48:
            third_days = 2
        third_time_hours = round(third_timeFoot - 24, 1)

        if fourth_timeFoot < 24:
            fourth_days = 0
        elif 48 > fourth_timeFoot >= 24:
            fourth_days = 1
        elif fourth_timeFoot >= 48:
            fourth_days = 2
            fourth_time_hours = round(fourth_timeFoot - 48, 1)

        f_out.write('If a person traveled on foot:')
        f_out.write('\n')

        first_time_foot = str(first_time_hours)
        first_timeDays = str(first_days)
        f_out.write('{} day {} hours - in that time a person will get to Barnaul '
                    'from Novosibirsk.'.format(first_timeDays, first_time_hours))
        f_out.write('\n')
        second_time_foot = str(second_time_hours)
        second_timeDays = str(second_days)
        f_out.write('{} day {} hours - in that time a person will get to Tomsk '
                    'from Novosibirsk.'.format(second_timeDays, second_time_hours))
        f_out.write('\n')
        third_time_foot = str(third_time_hours)
        third_timeDays = str(third_days)
        f_out.write('{} day {} hours - in that time a person will get to Kemerovo '
                    'from Novosibirsk.'.format(third_timeDays, third_time_hours))
        f_out.write('\n')
        fourth_time_foot = str(fourth_time_hours)
        fourth_timeDays = str(fourth_days)
        f_out.write('{} days {} hours - in that time a person will get to Novokuznetsk '
                    'from Novosibirsk.'.format(fourth_timeDays, fourth_time_hours))
        f_out.write(2 * '\n')
