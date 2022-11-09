import lib

min1 = int(input("Введите минимальное число:"))
max1 = int(input("Введите максимальное число:"))
number = int(input("Введите количество чисел:"))

lst = []
dct = {}

lib.fill_list(min1, max1, number, lst)
lib.analysis(lst, dct)
for item in sorted(dct):
    print("'%d':%d" % (item, dct[item]))

    