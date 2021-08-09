import sys 
sys.path.insert(0, "./../../../src/")

class NotFoundDriver(Exception):
    def __init__(self, *args, **kwargs):
        super(NotFoundDriver, self).__init__(*args, **kwargs)

class NotFoundBrowser(Exception):
    def __init__(self, *args, **kwargs):
        super(NotFoundBrowser, self).__init__(*args, **kwargs)

class BrowserNotSupported(Exception):
    def __init__(self, *args, **kwargs):
        super(BrowserNotSupported, self).__init__(*args, **kwargs)

class FlagInvalied(Exception):
    def __init__(self, *args, **kwargs):
        super(FlagInvalied, self).__init__(*args, **kwargs)




