import pickle

phoneBook = {
    'a': '1',
    'b': '2',
    'c': '3'
}

# write the file
with open('files/phoneBook_sample.txt', 'wb') as bin:
    pickle.dump(phoneBook, bin)


# read the binary file
with open('files/phoneBook_sample.txt', 'rb') as bin:
    data = pickle.load(bin)
    print(data)