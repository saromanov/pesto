from typing import List
import redis

client = redis.Redis()

def sadd(path:str, members:List[str]):
    res = client.sadd(path, members)
    if len(members) > 0 and res == 0:
        raise Exception('unable to add members to cache')

def smembers(path:str) -> List[str]:
    return client.smembers(path)