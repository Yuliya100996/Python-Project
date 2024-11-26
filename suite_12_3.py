import unittest
import tests_12_3

tst = unittest.TestSuite()
tst.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tst.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tst)