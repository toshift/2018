import tornado.web
import tornado.ioloop


class Mainhandler(tornado.web.RequestHandler):
    def get(self):
        self.write("test site")


def make_app():
    return tornado.web.Application([(r"/", Mainhandler),])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)

    tornado.ioloop.IOLoop.current().start()
