from unittest import TestCase, main
from rt_with_exceptions import Runner
import logging


class RunnerTest(TestCase):

    def test_walk(self):
        try:
            r = Runner("Alex", -10)

            for _ in range(10):
                r.walk()
            self.assertEqual(r.distance, 50)

            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            r = Runner(["Max"])
            for _ in range(10):
                r.run()
            self.assertEqual(r.distance, 100)

            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == "__main__":
    logging.basicConfig(filemode='w', filename='runner_tests.log', level=logging.INFO, encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    main()
