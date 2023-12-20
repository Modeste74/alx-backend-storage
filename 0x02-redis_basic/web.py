#!/usr/bin/env python3
"""defines a function get_page"""
import requests
import redis
import time

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """Get the HTML content of a URL and cache it with tracking"""
    # Key for tracking the URL access count
    access_count_key = f"count:{url}"

    # Increment access count for the URL
    redis_client.incr(access_count_key)

    # Retrieve HTML content of the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the HTML content with an expiration time of 10 seconds
    cache_key = f"cache:{url}"
    redis_client.setex(cache_key, 10, html_content)

    return html_content
