import tornado.ioloop
from web.handler import Base_handler
from apscheduler.scheduler import Scheduler
from insta_as_service import insta_service
import settings
from dogpile.cache import make_region

region = make_region().configure(
    'dogpile.cache.memory'
)
region.get_multi()
# Start the scheduler
sched = Scheduler()
sched.start()

application = tornado.web.Application([
    (r"/location/(\-?\d+(?:\.\d+)?)/(\-?\d+(?:\.\d+)?)/", Base_handler),
], my_shared_cache = region)

if __name__ == "__main__":
    sched.add_interval_job(insta_service, minutes=settings.insta_fetch_window_in_minutes)
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()