import unittest
from main import Student
class studenttest(unittest.TestCase):
    def test_walk_distance(self):

        student = Student(name="Иван")
        expected_distance = 500  # Если поставить 275 тест будет пройден
        actual_distance = 0

        for _ in range(10):
            student.walk()
            actual_distance += student.distance

        self.assertEqual(actual_distance, expected_distance,
                         msg=f"Дистанции не равны [дистанция человека(объекта)] != {expected_distance}")

    def test_run_distance(self):

        student = Student("Петр")
        expected_distance = 1000  # Если поставить 550 тест будет пройден
        actual_distance = 0

        for _ in range(10):
            student.run()
            actual_distance += student.distance

        self.assertEqual(actual_distance, expected_distance,
                         msg=f"Дистанции не равны [дистанция человека(объекта)] != {expected_distance}")

    def test_competition(self):
        runner = Student("Сергей")
        walker = Student("Михаил")
        run_actual_distance = 0
        walk_actual_distance = 0
        for _ in range(10):
            runner.run()
            run_actual_distance += runner.distance
            walker.walk()
            walk_actual_distance += walker.distance

        self.assertGreater(run_actual_distance, walk_actual_distance,
                           msg=f"[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]")