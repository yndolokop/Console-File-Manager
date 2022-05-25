word_freq = {'is': [1, 3, 4, 8, 10],
             'at': [3, 10, 15, 7, 9],
             'test': 33,
             'this': [2, 3, 5, 6, 11],
             'why': [10, 3, 9, 8, 12]}
# Iterate over a dictionary with list values using nested for loop
for key, values in word_freq.items():
    print('Key :: ', key)
    if isinstance(values, list):
        for value in values:
            print(value)
    else:
        print(value)

