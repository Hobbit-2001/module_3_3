def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)
#1
print_params()
print_params(5, 'pyramid', False)
print_params(466, 'водопад')
print_params(b = 'экзамен')
print_params(b = 25)
print_params(c = [1, 2, 3])
#2
values_list = [458, 'Violetta', False]
values_dict = {'a': 500, 'b': 'Alexandr', 'c': True }
print_params(*values_list)
print_params(**values_dict)
#3
values_list_2 = [15, 'Argus']
print_params(*values_list_2, 69)