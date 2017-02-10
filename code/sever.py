
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/index.html", title="My title", h1="it is h1")

class AutoFortune(tornado.web.RequestHandler):
    def get(self):
        from fortune import fortune
        g = fortune()
        self.render("html/fortune.html", title='auto', gua=g[1], guaming=g[2], qian=g[3],  guaci=g[4], yunshi=g[5], daima='null')



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