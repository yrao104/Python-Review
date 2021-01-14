class SearchEngineEntry:
    secure_prefix = "https://"
    def __init__(self, url):
        self.url = url

    def secure(self):
        return "{prefix}{site}".format(prefix = self.secure_prefix, site=self.url)

wikipedia = SearchEngineEntry("www.wikipedia.org")

print(wikipedia.url)
#prints "www.wikipedia.org"