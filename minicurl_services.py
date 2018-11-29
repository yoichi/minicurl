_SERVICES = {
    "http": 80,
}

def get_port(scheme):
    return _SERVICES[scheme]

if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):
        def test_http(self):
            self.assertEqual(get_port("http"), 80)

        def test_https(self):
            self.assertEqual(get_port("https"), 443)

    unittest.main()


