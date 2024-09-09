#!/usr/bin/env python3
"""a module that uses the requests module to obtain
    the HTML content of a particular URL and returns it"""
import redis
import requests
rs = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """track how many times a particular URL
        was accessed in the key 'count:{url}'"""
    rs.set(f"cached:{url}", count)
    res = requests.get(url)
    rs.incr(f"count:{url}")
    rs.setex(f"cached:{url}", 10, rs.get(f"cached:{url}"))
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
