import pickle

dict_1 = {1: 2, 3:4}

write = open('dict_1.pickle', 'wb')
pickle.dump(dict_1, write)
write.close()

read = open('dict_1.pickle', 'rb')
new_dict = pickle.load(read)
read.close()

print(new_dict[1])

dict_2 = {'apple': 2, 'orange': 5}

write = open('dict_2.pickle', 'wb')
pickle.dump(dict_2, write)
write.close()

read = open('dict_2.pickle', 'rb')
new_dict_2 = pickle.load(read)
read.close()

print(new_dict_2['orange'])