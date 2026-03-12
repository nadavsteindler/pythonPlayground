import unittest

from domain_counter import calculate_count_domains


class TestCalculateCountDomains(unittest.TestCase):

    def test_single_domain(self):
        result = calculate_count_domains("100 apps.google.com")
        counts = self._parse_result(result)
        self.assertEqual(counts["apps.google.com"], 100)
        self.assertEqual(counts["google.com"], 100)
        self.assertEqual(counts["com"], 100)

    def test_multiple_domains_same_parent(self):
        result = calculate_count_domains("100 apps.google.com,200 calendar.google.com")
        counts = self._parse_result(result)
        self.assertEqual(counts["apps.google.com"], 100)
        self.assertEqual(counts["calendar.google.com"], 200)
        self.assertEqual(counts["google.com"], 300)
        self.assertEqual(counts["com"], 300)

    def test_full_example(self):
        result = calculate_count_domains("100 apps.google.com,200 calendar.google.com,50 my.pony.com")
        counts = self._parse_result(result)
        self.assertEqual(counts["apps.google.com"], 100)
        self.assertEqual(counts["calendar.google.com"], 200)
        self.assertEqual(counts["google.com"], 300)
        self.assertEqual(counts["my.pony.com"], 50)
        self.assertEqual(counts["pony.com"], 50)
        self.assertEqual(counts["com"], 350)

    def test_single_level_domain(self):
        result = calculate_count_domains("10 com")
        counts = self._parse_result(result)
        self.assertEqual(counts["com"], 10)
        self.assertEqual(len(counts), 1)

    def _parse_result(self, result: str) -> dict[str, int]:
        counts = {}
        for entry in result.split(","):
            count_str, domain = entry.split(" ")
            counts[domain] = int(count_str)
        return counts


if __name__ == "__main__":
    unittest.main()
