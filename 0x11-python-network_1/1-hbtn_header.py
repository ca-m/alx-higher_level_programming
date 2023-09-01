#!/usr/bin/python3
"""displays X-Request-Id header variable of request to given URL

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
	url = sys.argv[1]

	request = urllib.request.Request(url)
	with urllib.request.urlopen(request) as response:
		print(dict(response.headers).get("X-Request-Id"))
