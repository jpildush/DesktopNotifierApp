import requests
import xml.etree.ElementTree as ET

def loadRSS(RSS_URL):
    RSSitems = requests.get(RSS_URL)

    return RSSitems.content

def getStories(RSS_URL):
    RSS = loadRSS(RSS_URL)

    rootElement = ET.fromstring(RSS)

    for story in rootElement.findall('./channel/item'):
        article = {}
        for item in story:
                article[item.tag] = item.text.encode('utf8') if type(item.text) is str else item.tag.encode('utf8')

        yield article
