import frontik


class HackatonPage(frontik.handler.PageHandler):

    def get_page(self):
        self.set_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.set_header('Pragma', 'no-cache')
        self.set_header('Expires', '0')

    @property
    def storage(self):
        return self.application.snapshot