import pprint
import unittest
from typing import Dict

from fingerprint_server_sdk import BaseModel


class ExampleModel(BaseModel):
    """Example model that inherits from BaseModel for testing purposes."""
    swagger_types: Dict[str, str] = {
        'name': 'str',
        'details': 'dict',
        'items': 'list',
        'sub_model': 'object'
    }

    attribute_map: Dict[str, str] = {
        'name': 'name',
        'details': 'details',
        'items': 'items',
        'sub_model': 'sub_model'
    }

    nullable_map: Dict[str, str] = {
        'name': False,
        'details': False,
        'items': False,
        'sub_model': False
    }

    def __init__(self, name=None, details=None, items=None, sub_model=None):
        self.name = name
        self.details = details
        self.items = items
        self.sub_model = sub_model


class SubModel(BaseModel):
    """SubModel to be used in ExampleModel."""
    swagger_types: Dict[str, str] = {
        'id': 'int',
        'value': 'str'
    }

    attribute_map: Dict[str, str] = {
        'id': 'id',
        'value': 'value'
    }

    nullable_map: Dict[str, str] = {
        'id': False,
        'value': False
    }

    def __init__(self, id=None, value=None):
        self.id = id
        self.value = value


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.sub_model = SubModel(id=1, value="sub_value")
        self.model = ExampleModel(name="Test Model", details={"key": "value"}, items=[1, 2, 3], sub_model=self.sub_model)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        expected = {
            'name': "Test Model",
            'details': {"key": "value"},
            'items': [1, 2, 3],
            'sub_model': {'id': 1, 'value': 'sub_value'}
        }
        self.assertEqual(self.model.to_dict(), expected)

    def test_to_dict_with_none(self):
        """Test conversion to dictionary with None values."""
        model = ExampleModel(name=None, details=None, items=None, sub_model=None)
        expected = {}
        self.assertEqual(model.to_dict(), expected)

    def test_to_dict_with_dict_of_models(self):
        """Test conversion to dictionary with a dictionary of models."""
        model = ExampleModel(name="Test Model", details={"key": "value"}, items=[1, 2, 3], sub_model={"sub": self.sub_model})
        expected = {
            'name': "Test Model",
            'details': {"key": "value"},
            'items': [1, 2, 3],
            'sub_model': {'sub': {'id': 1, 'value': 'sub_value'}}
        }
        self.assertEqual(model.to_dict(), expected)

    def test_to_str(self):
        """Test conversion to string."""
        expected_str = pprint.pformat(self.model.to_dict())
        self.assertEqual(self.model.to_str(), expected_str)

    def test_repr(self):
        """Test __repr__ method."""
        expected_repr = self.model.to_str()
        self.assertEqual(repr(self.model), expected_repr)

    def test_eq(self):
        """Test equality comparison."""
        model1 = ExampleModel(name="Test Model", details={"key": "value"}, items=[1, 2, 3], sub_model=self.sub_model)
        model2 = ExampleModel(name="Test Model", details={"key": "value"}, items=[1, 2, 3], sub_model=self.sub_model)
        sub_model2 = SubModel(id=1, value="sub_value")
        model3 = ExampleModel(name="Test Model", details={"key": "value"}, items=[1, 2, 3], sub_model=sub_model2)
        self.assertTrue(model1 == model2)
        self.assertTrue(model1 == model3)

    def test_ne(self):
        """Test inequality comparison."""
        model1 = ExampleModel(name="Test Model", details={"key": "value"}, items=[1, 2, 3], sub_model=self.sub_model)
        sub_model2 = SubModel(id=2, value="different_value")
        model2 = ExampleModel(name="Test Model", details={"key": "value"}, items=[1, 2, 3], sub_model=sub_model2)
        self.assertTrue(model1 != model2)
        self.assertTrue(model1 != sub_model2)
        self.assertTrue(model2 != sub_model2)

    def test_dict_inheritance(self):
        """Test behavior when inheriting from dict."""
        class DictInheritedModel(dict, BaseModel):
            swagger_types: Dict[str, str] = {}
            attribute_map: Dict[str, str] = {}

        dict_inherited_model = DictInheritedModel()
        dict_inherited_model["key"] = "value"
        expected = {"key": "value"}
        self.assertEqual(dict_inherited_model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
