from user import User
import pickle

DATA = "data"
data = open(DATA, 'rb')
users = pickle.load(data)
data.close()

UID = "1942473263"
u = users[UID]
print(u)
print(len(users))
