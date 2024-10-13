from unittest import TestCase, main, skipIf

# Пока только так решил вопрос выполнения модуля 12_3
# (из-за того что разложил по папкам, по-ходу и возникла такая ситуация)
if __name__ == "__main__":
    from runner import Runner
else:
    from .runner import Runner


@skipIf(__name__ != "__main__", "Добавлено для выполнения модуля 12 3")
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
    main(verbosity=2)
