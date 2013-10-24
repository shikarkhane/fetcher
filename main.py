import tornado.ioloop
import config

from twitter import tweet

application = tornado.web.Application([
    (r"/", tweet.Tweet_handler),
])

if __name__ == "__main__":
    #create config file
    config.create_config_file("mainkey","mainvalue")
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()