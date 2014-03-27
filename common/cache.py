from common.utility import Date_handler
import settings
import datetime
from datetime import timedelta

def fmt_dt(dt = datetime.datetime.utcnow()):
    return dt.strftime("%Y%m%d")
def get_or_create(cache_region, key):
    '''key = 58.1030823,18.083038
        value = utc timestamp
    '''
    dt = fmt_dt()

    # if key exists, update timestamp to show its an active coord which we should keep on scanning
    r = cache_region.get(key)
    if r:
        cache_region.delete(key)
        remove_key_from_dt(cache_region, r, key)
    cache_region.set(key, dt)
    add_dt_key(cache_region, dt, key)
def if_exists(cache_region, key):
    r = cache_region.get(key)
    return_value = False
    if r:
        return True
    get_or_create(cache_region, key)
    return return_value

def add_dt_key(cache_region, dt, key):
    '''Since we are using memory backend for dogpile, we have to find the delete old keys ourselves.
     And since we dont have any method to get all the keys, we are saving also date wise coordinates, to later
     delete them
        key = utc date
        value = [<coord1>, <coord2>,...]
    '''
    key_list = cache_region.get(dt)
    if key_list:
        if not key in key_list:
            key_list.append(key)
            cache_region.delete(dt)
            cache_region.set(dt, key_list)
    else:
        cache_region.set(dt, [key])
def remove_key_from_dt(cache_region, dt, key):
    '''remove the key from key=dt 's value list'''
    i = cache_region.get(dt)
    if i:
        f = list(set(i) - set(key))
        cache_region.delete(dt)
        cache_region.set(dt, f)
def maintain(cache_region):
    '''remove keys from cache which are older than settings.cache_key_expiry_in_days'''
    dt_now = datetime.datetime.utcnow()
    from_dt = dt_now - timedelta(settings.cache_key_expiry_in_days)
    to_dt = from_dt - timedelta(10) # look for 10 days before expiry
    while from_dt >= to_dt:
        coord_list = cache_region.get(fmt_dt(from_dt))
        if coord_list:
            # delete all the coordinate keys
            [cache_region.delete(i) for i in coord_list]
        #remove the date entry
        cache_region.delete(fmt_dt(from_dt))
        from_dt = from_dt - timedelta(1)
def get_all_keys(cache_region):
    '''check last x days'''
    from_dt_now = datetime.datetime.utcnow()
    till_dt = from_dt_now - timedelta(settings.cache_key_expiry_in_days)
    all_keys = []
    while from_dt_now >= till_dt:
        key_list = cache_region.get(fmt_dt(from_dt_now))
        if key_list:
            [all_keys.append(i) for i in key_list]
        from_dt_now = from_dt_now - timedelta(1)
    return all_keys