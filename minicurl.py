from minicurl_dig import lookup
from minicurl_http import create_request
from minicurl_http import extract_response_body
from minicurl_services import get_port
from minicurl_tcp import connect
from minicurl_tcp import read
from minicurl_tcp import write
from minicurl_url import parse_url

def main(url):
    scheme, host, path = parse_url(url)
    ip = lookup(host)
    s = connect(ip, get_port(scheme))
    write(s, create_request(host, path))
    body = extract_response_body(read(s))
    print(body)

if __name__ == '__main__':
    import sys

    main(sys.argv[1])
