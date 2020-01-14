def count_elements():

    my_list = input("Пожалуйста введите список элементов через пробелы: ")
    element = input("Введите нужный вам элемент: ")

    count_element = my_list.count(element) 
    return print(count_element)

count_elements() 