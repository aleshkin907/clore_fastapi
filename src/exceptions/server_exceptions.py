class ServersNotFoundException(Exception):
    def __init__(self, **kwargs):
        self.filters = kwargs
