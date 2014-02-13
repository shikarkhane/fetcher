import tornado.ioloop

from twitter import tweet
from insta.handler import Insta_Popular, Insta_handler

application = tornado.web.Application([
    (r"/twitter/", tweet.Tweet_handler),
    (r"/insta/", Insta_handler),
    (r"/insta/popular/", Insta_Popular),
])

if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()