import datetime

def get_system_time():
    """
    Returns a formatted text with current time
    """
    return '{:%d/%m/%Y %H:%M:%S}'.format(datetime.datetime.now())

def get_filename_from_time():
    return '{:%d%m%Y%H%M%S}'.format(datetime.datetime.now())