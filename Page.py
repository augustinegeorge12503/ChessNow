"""
holds information about current page
"""
class Page:

    def __init__(self) -> None:
        self.page = 'home'
    
    def changePage(self, toPage):
        self.page = toPage