
class HelpController:
    '''
    Controller for help page
    '''

    def __init__(self, model=None):
        self.model = model

    def get_title(self):
        return "Help"
