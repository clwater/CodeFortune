
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/index.html", title="My title", h1="it is h1")

class AutoFortune(tornado.web.RequestHandler):
    def get(self):
        self.write("aaa")

class MyFortune(tornado.web.RequestHandler):
    def get(self):
        self.write("bbb")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/auto" ,AutoFortune),
        (r"/fortune" , MyFortune),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(9002)
    print("run in : " , "127.0.0.1:9002")
    tornado.ioloop.IOLoop.current().start()