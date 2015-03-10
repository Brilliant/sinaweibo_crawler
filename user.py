from utils import *
import re

class User:
    def __init__(self, uid, nick = ""):
        self.uid = uid
        self.nick = nick
        self.num_weibo = -1
        self.num_follow = 0
        self.num_fans = 0
        self.follow = set()
        self.fans = set()

    def __str__(self):
        return self.uid + " " + self.nick + " "

    def get_information(self):
        url = HOST + self.uid
        soup = get(url)
        div = soup.find(attrs = {"class": "tip2"})
        counts = re.findall(r"\d+", div.text)
        self.num_weibo = counts[0]
        self.num_follow = counts[1]
        self.num_fans = counts[2]

    def fetching(self, suffix, page_number, users):
        url = HOST + self.uid + suffix + str(page_number)
        soup = get(url)
        follow = set()
        for table in soup.find_all("table"):
            information = table.find_all("td")[-1].find_all("a")
            nick = information[0].text
            user_id = re.search(r"\d{4,}", information[-1].get("href")).group(0)
            follow.add(user_id)
            if user_id not in users:
                users[user_id] = User(user_id, nick)
        return follow

    def get(self, pattern, follow_or_fans, users):
        for page_number in range(2):
            ids = self.fetching(pattern, page_number + 1, users)
            if len(ids) == 0:
                break
            follow_or_fans |= ids

    def get_follow(self, users):
        self.get("/follow?page=", self.follow, users)

    def get_fans(self, users):
        self.get("/fans?page=", self.fans, users)

    def print(self):
        print(self.uid, self.nick, self.num_weibo)
        print(self.num_follow, self.follow)
        print(self.num_fans, self.fans)
