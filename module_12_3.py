import unittest
from module_12_1 import tests_12_1 as m121
from module_12_2 import module_12_2 as m122


runnerTest = unittest.TestSuite()
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(m121.RunnerTest))
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(m122.RunnerTest))
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(m122.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTest)
