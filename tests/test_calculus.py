import unittest
from src.calculus import Calculus

class TestCalculus(unittest.TestCase):

    def test_manipulate_json(self):
        cases = [
            ("{\"key\": \"value\"}", 2, "{\"key\": \"value\", \"pair\": true}"),
            ("{\"key\": \"value\"}", 1, "{\"key\": \"value\", \"pair\": false}")
        ]
        
        calc = Calculus()
        
        for case  in cases:
            data, index, expected = case
            with self.subTest(data=data, index=index, expected=expected):
                self.assertEqual(calc._Calculus__manipulate_json(index, data), expected)

    def test_apply_rules(self):
        cases = [
            ("{\"key\": \"value\"}", 5, "Multiple de 5"),
            ("Process 222 succesfully run", 1, "Rien à afficher"),
            ("{\"key\": \"value\"}", 1, "{\"key\": \"value\", \"pair\": false}"),
            ("{\"key\": \"value\"}.", 1, "{\"key\": \"value\"}."),
            ("{\"key\": \"value\"}.", 5, "Multiple de 5"),
            ("Process 222$succesfully run", 1, "Process_222$succesfully_run"),
        ]
        
        calc = Calculus()
        
        for case  in cases:
            data, index, expected = case
            with self.subTest(data=data, index=index, expected=expected):
                self.assertEqual(calc._Calculus__apply_rules(index, data, 0), expected)

    def test_process_file(self):
        logs = [
            "{\"key\": \"value\"}",
            "Process 222 succesfully run",
            "{\"key\": \"value\"}",
            "{\"key\": \"value\"}.",
            "Process 222$succesfully run",
            "{\"key\": \"value\"}."            
        ]

        expected = [
            "Multiple de 5",
            "Rien à afficher",
            "{\"key\": \"value\", \"pair\": true}",
            "{\"key\": \"value\"}.",
            "Process_222$succesfully_run",
            "Multiple de 5"
        ]
        
        calc = Calculus()
        calc._Calculus__raw_data = logs
        
        calc.process_logs()

        for i, processed_line in enumerate(calc._Calculus__new_data):
            self.assertEqual(processed_line, expected[i])


if __name__ == '__main__':
    unittest.main()
