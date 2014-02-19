from flickr.flickr_talker import Base
import settings

Base(settings.flickr_client_id).write_flickrs_to_file('14.479980,58.240164,19.423828,61.175033')