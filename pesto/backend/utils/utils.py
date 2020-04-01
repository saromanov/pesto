import datetime

def time_now_formatted(title):
    return datetime.datetime.now().strftime(f'{title}:%Y:%m:%d:%H')