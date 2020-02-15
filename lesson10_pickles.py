import pickle

str_en = 'abracadabra'
str_ru = 'абракадабра'

d0 = {str_en: str_ru, 'extension': [list(range(10))] * 3}

# f = open('lesson10_nopickle.data', 'w')
# print(repr(d0), file=f)
# f.close()

f = open('lesson10_pickle.data', 'bw')
data0 = pickle.dumps(d0)
f.write(data0)
f.close()

f = open('lesson10_pickle.data', 'br')
data1 = f.read()
d1 = pickle.loads(data1)
f.close()

print(d0)
print(d1)
print(d0 == d1)
