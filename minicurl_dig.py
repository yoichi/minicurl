import socket

def lookup(host):
    info = socket.getaddrinfo(host, None, family=socket.AF_INET)
    return host

if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):
        def test_localhost(self):
            self.assertEqual(lookup('localhost'), "127.0.0.1")

    unittest.main()
