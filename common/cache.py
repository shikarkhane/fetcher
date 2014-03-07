from common.utility import Date_handler
import settings


def fmt_dt():
    return Date_handler().get_current_utc_date_string("%Y%m%d")
def fmt_key(lat,lng):
    return "{0},{1}".format(lat,lng)
def get_or_create(cache_region, lat, lng):
    '''key = 58.1030823,18.083038
        value = utc timestamp
    '''
    coord = fmt_key(lat, lng)
    dt = fmt_dt()

    # if key exists, update timestamp to show its an active coord which we should keep on scanning
    r = cache_region.get(coord)
    if r:
        cache_region.delete(coord)
        remove_coord_from_dt(cache_region, r, coord)
    cache_region.set(coord, dt)
    add_dt_coord(cache_region, dt, coord)

def add_dt_coord(cache_region, dt, coord):
    '''Since we are using memory backend for dogpile, we have to find the delete old keys ourselves.
     And since we dont have any method to get all the keys, we are saving also date wise coordinates, to later
     delete them
        key = utc date
        value = [<coord1>, <coord2>,...]
    '''
    coord_list = cache_region.get(dt)
    if coord_list:
        if not coord in coord_list:
            coord_list.append(coord)
            cache_region.delete(dt)
            cache_region.set(dt, coord_list)
    else:
        cache_region.set(dt, [coord])
def remove_coord_from_dt(cache_region, dt, coord):
    '''remove the coord from key=dt 's value list'''
    i = cache_region.get(dt)
    if i:
        f = [a for a in i if a != coord]
        cache_region.delete(dt)
        cache_region.set(dt, f)
def maintain(cache_region):
    '''remove keys from cache which are older than settings.cache_key_expiry_in_days'''
    pass
