def count_calls():
    global calls
    calls += 1
    # print(calls)
    return calls


def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_


def is_contains(string, list_to_search):
    flag_ = False

    for i in list_to_search:
        if i.upper() == string.upper():
            flag_ = True
            break
    count_calls()
    return (flag_)


calls = 0
tuple_ = ()
string_ = ' Вася очень любит Олю '
string_1 = 'Три'
list_to_search = ['один', 'два', 'три', 'четыре']

print(string_info(string_))
print(is_contains(string_1, list_to_search))
print(calls)
