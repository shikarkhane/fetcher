import tornado.ioloop
import config

from twitter import tweet

application = tornado.web.Application([
    (r"/", tweet.Tweet_Handler),
])

if __name__ == "__main__":
    #create config file
    config.create_config_file()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()