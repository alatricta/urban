from unittest import TestCase, main
from runner import Runner


class RunnerTest(TestCase):

    def test_walk(self):
        r = Runner("Max")
        for _ in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = Runner("Max")
        for _ in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r1 = Runner("Max")
        r2 = Runner("Alex")
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == "__main__":
    main()
