import re

def create_request(host, path):
    return f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"

def extract_response_body(response):
    delimiter = "\r\n\r\n"
    index = response.find(delimiter)
    if index < 0:
        return ""
    return response[index + len(delimiter):]
