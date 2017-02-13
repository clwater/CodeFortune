
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        from date_utils import getNewDate
        getNewDate()
        self.render("html/index.html", title="My title", y_day="正月十六 丁酉年 ︻ 鸡年 ︼ 壬寅月 庚午日"
                    , r_day="二零一七年 二月十二日  没有节"
                    , day="12" , yi="写bug" , ji="改需求")

class AutoFortune(tornado.web.RequestHandler):
    def get(self):

        from fortune import fortune
        g = fortune()
        self.render("html/fortune.html", title='auto', gua=g[1], guaming=g[2], qian=g[3],  guaci=g[4], yunshi=g[5], daima='null')



class MyFortune(tornado.web.RequestHandler):
    def get(self):
        from fortune import fortunewithseed
        g = fortunewithseed(123)
        self.render("html/fortune.html", title='choose', gua=g[1], guaming=g[2], qian=g[3], guaci=g[4], yunshi=g[5],
                    daima='null')


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