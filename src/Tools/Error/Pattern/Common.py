class ErrorUnknown(Exception):
    def __init__(self, *args, **kwargs):
        super(ErrorUnknown, self).__init__(*args, **kwargs)