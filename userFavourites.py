import time
import notify2
from RSSinfo import RSSINFO
from getstories import getStories

class UserFavourites:
    def __init__(self, currentUser):
        self.userName = currentUser
        self.maxLimit = 20
        self.favourites = {}

    def addRSS(self):
        if len(self.favourites) <= self.maxLimit:
            RSS_URL = input("Please enter RSS URL: ").strip()
            if len(RSS_URL) < 200:
                if ".xml" in RSS_URL.split("/")[-1]:
                    while True:
                        RSS_NAME = input("Please provide name for new RSS: ").strip()
                        if len(RSS_NAME) < 20:
                             break
                        else:
                            print("RSS Name too long!")

                    self.favourites[RSS_NAME] = RSSINFO(RSS_NAME, RSS_URL)
            else:
                print("Link too long!")
        else:
            print("Max of 20 saved RSS feeds reached!")

    def showRSS(self):
        RSS_URL = input("Please enter RSS URL: ").strip()
        if ".xml" in RSS_URL.split("/")[-1]:
            article = getStories(RSS_URL)
            try:
                # path to notification window icon
                ICON_PATH = "put full path to icon image here"

                notify2.init("News Notifier")

                notify = notify2.Notification(None, icon=ICON_PATH)

                # set urgency level
                notify.set_urgency(notify2.URGENCY_NORMAL)

                # set timeout for a notification
                notify.set_timeout(10000)
                while True:
                    info = next(article)

                    # update notification data for Notification object
                    notify.update(info['title'], info['description'])

                    # show notification on screen
                    notify.show()

                    # short delay between notifications
                    time.sleep(5)
            except (GeneratorExit, StopIteration):
                print("Caught exit and finished displaying notifications!")
        else:
            print("Not an RSS Page!")
