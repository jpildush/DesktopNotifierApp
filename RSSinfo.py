'''
DesktopNotifierApp has been solely created by Joseph Pildush.

Third party modules have been imported and used, to enhance the application.
These third party modules listed below have NOT been tampered or altered in any way and I, Joseph Pildush, am NOT the original author.

Python/Third-Party Modules used:
time
notify2
requests
pickle
os
xml
'''


class RSSINFO:
    def __init__(self, name, url):
        self.RSSname = name
        self.RSSurl = url
        self.data = []