import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner.Runner('Bob')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner.Runner('Bob')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = Runner.Runner('Bob')
        runner_2 = Runner.Runner('Dave')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
