from island_counting import count_islands


class TestIslandCounting:
    def test_zero(self):
        map = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
        assert count_islands(map) ==0

    def test_one(self):
        map = [
            [0,0,1,0],
            [0,1,1,0],
            [1,0,1,0],
            [1,1,1,0]]
        assert count_islands(map) ==1

    def test_three(self):
        map = [
            [0,0,1,0],
            [1,1,0,1],
            [0,1,0,1],
            [0,1,0,0]]
        assert count_islands(map) ==3