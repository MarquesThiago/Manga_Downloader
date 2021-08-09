import sys 

class KeyError(Exception):
    def __init__(self, *args, **kwargs):
        super(KeyError, self).__init__(*args, **kwargs)

class NotFoundButtonAlternPg(Exception):
    def __init__(self, *args, **kwargs):
        super(NotFoundButtonAlternPg, self).__init__(*args, **kwargs)

class BrowserNotSupported(Exception):
    def __init__(self, *args, **kwargs):
        super(BrowserNotSupported, self).__init__(*args, **kwargs)

class FlagInvalied(Exception):
    def __init__(self, *args, **kwargs):
        super(FlagInvalied, self).__init__(*args, **kwargs)