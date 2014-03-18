import tornado.ioloop
from web.handler import Base_handler
from apscheduler.scheduler import Scheduler
from insta_as_service import insta_service
from common.cache import maintain
import settings
from dogpile.cache import make_region

region = make_region().configure(
    'dogpile.cache.memory'
)
# Start the scheduler
sched = Scheduler()
sched.start()

application = tornado.web.Application([
    (r"/location/(\-?\d+(?:\.\d+)?)/(\-?\d+(?:\.\d+)?)/", Base_handler, dict(my_shared_cache=region)),
])

if __name__ == "__main__":
    sched.add_interval_job(lambda: insta_service(region), minutes=settings.insta_fetch_window_in_minutes)
    sched.add_interval_job(lambda: maintain(region), days=settings.cache_key_expiry_in_days)
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()