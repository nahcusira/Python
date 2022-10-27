dict = {'I' : 1, 'IV' : 4,  'V': 5, 'IX' : 9, 'X': 10, 'L' : 50, 'XC' : 90, 'C' : 100, 'XL' : 40, 'CM' : 900, 'CD' : 400, 'D' : 500, 'M' : 1000, 'MM' : 2000, 'MMM' : 3000, 'II' : 2, 'III': 3, 'VI':6, 'VII': 7, 'VIII':8, 'XX':20, 'XXX':30, 'LX' : 60, 'LXX': 70, 'LXXX': 80, 'CC': 200, 'CCC': 300, 'DC': 600, 'DCC': 700, 'DCCC': 800, '':0}
roman = ''
num = int(input())
thousands = num - (num % 1000)
hundred = num % 1000 - num % 100
ten = ((num % 100) // 10)*10
one = num - thousands - hundred - ten
key_list = list(dict.keys())
val_list = list(dict.values())
position = val_list.index(thousands)
roman += key_list[position]
position = val_list.index(hundred)
roman += key_list[position]
position = val_list.index(ten)
roman += key_list[position]
position = val_list.index(one)
roman += key_list[position]
print(roman)
