class ErrorNotlogged(Exception):
    def __init__(self, *args, **kwargs):
        super(ErrorNotlogged, self).__init__(*args, **kwargs)
