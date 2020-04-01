from typing import List
import redis

client = redis.Redis()

def sadd(path:str, members:List[str]):
    if len(members) == 0:
        return     
    client.sadd(path, *members)

def smembers(path:str) -> List[str]:
    return client.smembers(path)