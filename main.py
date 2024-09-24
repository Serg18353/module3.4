def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(5, 4, "acdc")
print_params(b=25)
print_params()
values_list = ['kiss', 23, False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(values_list)
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['RHCP', 22.3]
print_params(*values_list_2, 42)
