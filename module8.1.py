def add_everything_up(*data):
    try:
        return round(sum(data) if isinstance(data[0], int) or isinstance(data[0], float) else data[0]+data[1], 3)
    except TypeError:
        return str(data[0]) + data[1] if isinstance(data[0], int) or isinstance(data[0], float) \
            else data[0] + str(data[1])


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
