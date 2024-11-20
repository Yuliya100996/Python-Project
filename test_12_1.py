import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test1 = Runner('t_W')
        for i in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    def test_run(self):
        test2 = Runner('t_R')
        for i in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    def test_challenge(self):
        test3_2 = Runner('t_R')
        test3_1 = Runner('t_W')
        for i in range(10):
            test3_2.run()
            test3_1.walk()
        self.assertNotEqual(test3_2.distance, test3_1.distance)

if __name__ == '__main__':
    result = unittest.main
    print(result)







