"""
holds information about current page
"""
class Page:

    def __init__(self) -> None:
        self.page = 'home'
    
    def change_page(self, to_page):
        self.page = to_page