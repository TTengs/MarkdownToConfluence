class PageNotFoundError(Exception):
    def __init__(self, page_title, spacekey, message="Page doesn't exist in the space"):
        self.page_title = page_title
        self.spacekey = spacekey
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.page_title} does not exist in space: {self.spacekey}'