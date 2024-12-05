immutable_var = 1,4,6,'Privet',True, [1,45,34]
print (type(immutable_var[2]))
print (type(immutable_var[3]))
print (type(immutable_var[4]))
#immutable_var [2] = 69 Нельзя изменить элементы кортежа, изменение возможно, если этот элемент состоит из списка
immutable_var [5][2] = 56
print (immutable_var)
mutable_list = ['tadle',34,'true','f',11]
print (mutable_list)
mutable_list [0] = 'yandex'
mutable_list [1] = 'akademiya'
mutable_list [2] = 54
mutable_list [3] = 1
mutable_list [4] = 'false'
print (mutable_list)


