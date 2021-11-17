
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from FieldMapper import FieldMapper, InvalidMappingException


class TestFieldMapper(unittest.TestCase):

    def test_correct_mapping(self):
        example_values = {
            u'val_1': u'text_1',
            u'val_2': u'text_2',
            u'val_3': u'text_3',
        }
        example_mapping = {
            u'p_1': u'val_1',
            u'p_2': u'val_2',
            u'p_3': u'val_3',
        }
        desired_output = {
            u'p_1': u'text_1',
            u'p_2': u'text_2',
            u'p_3': u'text_3',
        }
        mapper = FieldMapper(example_values, example_mapping)
        self.assertEqual(mapper.valuedict, desired_output)
        self.assertEqual(mapper.getValues(), desired_output,
                         u'The output not correct!')

    def test_incorrect_mapping(self):
        example_values = {
            u'val_1': u'text_1',
            u'val_2': u'text_2',
            u'val_3': u'text_3',
        }
        example_mapping = {
            u'p_1': u'val_2',
            u'p_2': u'val_3',
            u'p_3': u'val_4',
        }
        self.assertRaises(InvalidMappingException,
                          (lambda: FieldMapper(example_values, example_mapping)))


if (__name__ == u'__main__'):
    unittest.main()
