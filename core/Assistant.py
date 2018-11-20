import instaloader
import datetime
from itertools import dropwhile, takewhile

class Assistant:

    def initializeAssistant(self, userName, password, userNameList, timeToSearch, proxy, filePath):
        loadrObject = instaloader.Instaloader()
        loadrObject.login(userName, password)
        self.loaderObject = loadrObject
        self.userNameList = userNameList
        self.timeToSearch = timeToSearch
        self.proxy = proxy
        self.filePath = filePath
        self.startedTime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                            "%Y-%m-%d %H:%M:%S")
        self.endingTime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                           "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=24)

    def getUserPosts(self, userName):
        posts = instaloader.Profile.from_username(self.loaderObject.context, userName).get_posts()
        SINCE = self.startedTime
        UNTIL = self.endingTime
        filteredPosts = takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts))
        return filteredPosts

    def getPostLikers(self, post):
        likers = []
        for like in post.get_likes():
            likers.append(like['username'])
        return likers

    def getUserFollowers(self, userName):
        followers = instaloader.Profile.from_username(self.loaderObject.context, userName).get_followers()
        return followers

