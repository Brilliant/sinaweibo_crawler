from user import User
import pickle
import time

def crawling(uid, depth):
    u = users[uid]
    if depth == 0 or u.num_weibo >= 0:
        return
    u.get_information()
    u.get_follow(users)
    u.get_fans(users)
    global count
    count += 1
    print(u)
    for follow in u.follow:
        crawling(follow, depth - 1)
    for fan in u.fans:
        crawling(fan, depth - 1)

TIME_BEGIN = time.time()
UID = "1942473263"
users = {UID: User(UID, "Durex")}
count = 0
crawling(UID, 3)
TIME_END = time.time()
print(TIME_END - TIME_BEGIN, count)

DATA = "data"
output = open(DATA, "wb")
pickle.dump(users, output)
output.close()
