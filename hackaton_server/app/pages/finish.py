import frontik.handler


class Page(frontik.handler.PageHandler):
    def get_page(self):
        self.json.put({
            'text': 'Hello, world!'
        })

        # для тестирвоания
        self.application.snapshot.increment_counters(1, 0, 1)
        self.application.snapshot.increment_counters(1, 1, 1)

