# 2-1 索引操作实例
# 将以数指定年、月、日的日期打印出来

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

#  一个列表，其中也包含数 1 - 31 对应的结尾
# endings[0 - 30] 1st, 2nd , 3rd, 4th -  20th - 21st ,22nd, 23rd, 24th - 30 th , 31st
endings = ['st','nd','rd'] + 17 * ['th'] \
    + ['st','nd','rd'] + 7 * ['th'] \
    + ['st']

year = input('year: ')
month = input('Month (1-12):')
day = input('Day (1-31):')

month_number = int(month)
day_number = int(day)

#  别忘了将月和日的数减一，这样才能得到正确的索引

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print(month_name + ' ' + ordinal + ', ' + year)

