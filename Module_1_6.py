my_dict = {'Ivan':'12.03.2003' ,'Katya':'24.05.1993','Vasya':'30.09.1987'}
print (my_dict)
print ('Значение существующего элемента:', my_dict['Ivan'], 'Значение отсутствующего элемента:',my_dict.get('semen'))
my_dict.update({'Egor':'19.05.1999','Max':'05.11.1989'})
print (my_dict)
print ('Значение, которое вырезали из словаря:',my_dict.pop('Ivan'))
print (my_dict)

my_set = {1,3,2,2,3,4,4,'iphone',3.43,(1,3)}
print ('первоначальное множество:',my_set)
my_set.update({7,'vanya'})
print ('множество, после добавления двух эелементов',my_set)
my_set.discard('iphone')
print ('множество, после удаления элемента',my_set)





