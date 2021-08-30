import unittest
from FieldMapper import FieldMapper, InvalidMappingException

class TestFieldMapper(unittest.TestCase):
    def test_correct_mapping(self):
        example_values : dict = {
            'val_1' : 'text_1',
            'val_2' : 'text_2',
            'val_3' : 'text_3'
        }
        example_mapping : dict = {
            'p_1' : 'val_1',
            'p_2' : 'val_2',
            'p_3' : 'val_3'
        }
        desired_output : dict = {
            'p_1' : 'text_1',
            'p_2' : 'text_2',
            'p_3' : 'text_3'
        }
        mapper = FieldMapper(example_values,example_mapping)
        self.assertEqual(mapper.valuedict, desired_output)
        self.assertEqual(mapper.getValues(), desired_output, "The output not correct!")

    def test_incorrect_mapping(self):
        example_values : dict = {
            'val_1' : 'text_1',
            'val_2' : 'text_2',
            'val_3' : 'text_3'
        }
        example_mapping : dict = {
            'p_1' : 'val_2',
            'p_2' : 'val_3',
            'p_3' : 'val_4'
        }
        self.assertRaises(InvalidMappingException, lambda : FieldMapper(example_values,example_mapping))

if __name__ == '__main__':
    unittest.main()