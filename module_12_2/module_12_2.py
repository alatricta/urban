from unittest import TestCase, main
from runner_and_tournament import Runner, Tournament
from pprint import pprint


class RunnerTest(TestCase):

    def test_walk(self):
        r = Runner("Max")
        for _ in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

        r2 = Runner("Alex", 10)
        for _ in range(10):
            r2.walk()
        self.assertEqual(r2.distance, 100)

    def test_run(self):
        r = Runner("Max")
        for _ in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

        r2 = Runner("Alex", 10)
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 200)

    def test_eq(self):
        r1 = Runner("Max")
        r2 = Runner("Alex")
        r3 = Runner("Max")
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1, r3)
        self.assertEqual(r2, "Alex")

    def test_challenge(self):
        r1 = Runner("Max")
        r2 = Runner("Alex")
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner("Усэйн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for j, t in cls.all_results.items():
            print("Турнир №", j)
            for i, r in t.items():
                print(i, r.name, end=" ")
            print()

    def test_tournament_1(self):
        t1 = Tournament(90, self.r1, self.r3)
        self.all_results[1] = t1.start()
        self.assertTrue(self.all_results[1][2] == self.r3)

    def test_tournament_2(self):
        t2 = Tournament(90, self.r2, self.r3)
        self.all_results[2] = t2.start()
        self.assertTrue(self.all_results[2][2] == self.r3)

    def test_tournament_3(self):
        t3 = Tournament(90, self.r1, self.r2, self.r3)
        self.all_results[3] = t3.start()
        self.assertTrue(self.all_results[3][3] == self.r3)

    def test_order(self):
        r1 = Runner("Андрей", 9)
        r2 = Runner("Ник", 5)
        t4 = Tournament(10, r2, r1)
        self.all_results[4] = t4.start()
        self.assertTrue(self.all_results[4][2] == r2, "Всё из-за последовательного прибавления в цикле")


if __name__ == "__main__":
    main()
