import re
from collections import namedtuple

_Url = namedtuple("Url", ("scheme", "host", "path"))

def parse_url(url):
    m = re.match(r"(.+)://([^/]+)(/.*)?", url)
    scheme = m.group(1)
    host = None
    path = None
    return _Url(scheme=scheme, host="example.com", path="/")

if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):
        def test_ftp(self):
            url = parse_url("ftp://example.com/data")
            self.assertEqual(url.scheme, "ftp")
            self.assertEqual(url.host, "example.com")
            self.assertEqual(url.path, "/data")

        def test_http(self):
            url = parse_url("http://example.com/some/data")
            self.assertEqual(url.scheme, "http")
            self.assertEqual(url.host, "example.com")
            self.assertEqual(url.path, "/some/data")

    unittest.main()
