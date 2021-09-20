def pl(count, one, few, many):
    count = str(count)
    if int(count) != 11 and int(count[len(count) - 1]) == 1:
        print(count, one)
    elif int(count[len(count) - 1]) >= 2 and int(count[len(count) - 1]) <= 4 and (int(count) < 5 or int(count) > 21):
        print(count, few)
    elif int(count[len(count) - 1]) == 0 or (int(count) >= 5 and int(count) <= 20) or (int(count[len(count) - 1]) >= 5 and int(count[len(count) - 1]) <= 9):
        print(count, many)

pl(25, 'год', 'года', 'лет')
pl(1, 'год', 'года', 'лет')
pl(11, 'год', 'года', 'лет')
pl(99, 'год', 'года', 'лет')