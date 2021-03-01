if __name__ == '__main__':
    my_dict = {'Tom': 18, 'Charley': 20, 'Tiffany': 22, 'Robert': 25, 'tom': 17}
    print(my_dict['Charley'])
    boys = {'Tom': 18, 'Charley': 20, 'Robert': 25, 'tom': 17}
    girls = {'Tiffany': 22}
    # copy() method to copy entire dictionary to new dictionary
    dict_G = girls.copy()
    dict_B = boys.copy()
    print("Boys' data:", dict_B)
    print("Girls' data:", dict_G)
    # update() method to update the dictionary by adding new entry or deleting an existing entry
    girls.update({'Reeta': 21})
    girls.update({'Tiffany': 32})
    print(girls)
    # del keyword to delete an key from the dictionary
    del boys['tom']
    print(boys)
    # adding new key in dictionary
    boys['Ram'] = 21
    print(boys)
    # items() method returns list of tuple pairs (key, value) in the dictionary
    print("Students Name: %s" % list(boys.items()))
    # for accessing a key value pair, use get() method whether key exist or not
    print(boys.get('Robert'))
    print(boys.get('Rahul'))
    # accessing key that doesn't exist gives KeyError
    # print(my_dict['Rahul'])
    # len() method to count number of pairs in dictionary
    print('Length of my dict: ', len(my_dict))
    print('Length of my dict: ', len(girls))
    print('Length of my dict: ', len(boys))
    # type() method
    print('Type: %s ' % type(my_dict))
    print(str(boys))
    # in keyword to check if key is in dictionary or not
    print('Ram' in boys)
    print('Email' in boys)


