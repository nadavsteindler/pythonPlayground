import unittest

from domain_counter import calculate_count_domains, calculate_count_domains_multithread

IMPLEMENTATIONS = [
    ("single_threaded", calculate_count_domains),
    ("multi_threaded", calculate_count_domains_multithread),
]


def _parse_result(result: str) -> dict[str, int]:
    counts = {}
    for entry in result.split(","):
        count_str, domain = entry.split(" ")
        counts[domain] = int(count_str)
    return counts


class TestCalculateCountDomains(unittest.TestCase):

    def test_single_domain(self):
        for name, fn in IMPLEMENTATIONS:
            with self.subTest(impl=name):
                counts = _parse_result(fn("100 apps.google.com"))
                self.assertEqual(counts["apps.google.com"], 100)
                self.assertEqual(counts["google.com"], 100)
                self.assertEqual(counts["com"], 100)

    def test_multiple_domains_same_parent(self):
        for name, fn in IMPLEMENTATIONS:
            with self.subTest(impl=name):
                counts = _parse_result(fn("100 apps.google.com,200 calendar.google.com"))
                self.assertEqual(counts["apps.google.com"], 100)
                self.assertEqual(counts["calendar.google.com"], 200)
                self.assertEqual(counts["google.com"], 300)
                self.assertEqual(counts["com"], 300)

    def test_full_example(self):
        for name, fn in IMPLEMENTATIONS:
            with self.subTest(impl=name):
                counts = _parse_result(fn("100 apps.google.com,200 calendar.google.com,50 my.pony.com"))
                self.assertEqual(counts["apps.google.com"], 100)
                self.assertEqual(counts["calendar.google.com"], 200)
                self.assertEqual(counts["google.com"], 300)
                self.assertEqual(counts["my.pony.com"], 50)
                self.assertEqual(counts["pony.com"], 50)
                self.assertEqual(counts["com"], 350)

    def test_single_level_domain(self):
        for name, fn in IMPLEMENTATIONS:
            with self.subTest(impl=name):
                counts = _parse_result(fn("10 com"))
                self.assertEqual(counts["com"], 10)
                self.assertEqual(len(counts), 1)


if __name__ == "__main__":
    unittest.main()
