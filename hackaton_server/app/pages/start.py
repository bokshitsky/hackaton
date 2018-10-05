import frontik.handler

class Page(frontik.handler.PageHandler):
    def get_page(self):
        self.set_template('start.html')
        self.json.put({
            'text': 'Hello, world!'
        })

    def post_page(self):
        self.redirect('/stage')
