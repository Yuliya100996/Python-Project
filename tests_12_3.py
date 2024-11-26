import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        race1 = Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results.append(race1.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        race2 = Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results.append(race2.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        race3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results.append(race3.start())
        self.assertTrue(TournamentTest.all_results[-1][3] == self.runner3)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test1 = Runner('t_W')
        for i in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test2 = Runner('t_R')
        for i in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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