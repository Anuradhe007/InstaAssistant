import instaloader

class Assistant:

    def __init__(self, userName, password):
        loadrObject = instaloader.Instaloader()
        loadrObject.login(userName, password)
        self.loaderObject = loadrObject

