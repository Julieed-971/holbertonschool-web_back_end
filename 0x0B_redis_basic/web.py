#!/usr/bin/env python3
"""Module that uses the requests module to obtain
the HTML content of a particular url and returns it
"""

import functools
import redis
import requests

redis_instance = redis.Redis()


def count_access(func):
    """Decorator that counts calls to a url
    """
    @functools.wraps(func)
    def wrapper(url):
        """Wrapper function that increments call count when url is called"""
        redis_instance.incr(f"count:{url}")
        result = func(url)
        return result
    return wrapper


def cache_with_expiration(func):
    """Decorator that checks if cached html from a url is cached in redis
    and fetch it and cache it if not
    """
    @functools.wraps(func)
    def wrapper(url):
        """Wrapper function that checks if
        cached html from a url is cached in redis
        and fetch it and cache it if not
        """
        cached_html = redis_instance.get(f"cached:{url}")

        if cached_html is not None:
            return cached_html.decode('utf-8')

        result = func(url)
        redis_instance.set(f"cached:{url}", result, ex=10)
        return result
    return wrapper


@count_access
@cache_with_expiration
def get_page(url: str) -> str:
    """Uses the requests module to obtain the HTML
    content of a particular URL and returns it
    """
    return requests.get(url).text
