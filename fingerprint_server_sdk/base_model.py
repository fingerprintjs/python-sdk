import pprint
from typing import Union, Dict


class BaseModel:
    """Base class for all models with utility methods."""

    swagger_types: Dict[str, str] = {}
    attribute_map: Dict[str, str] = {}
    nullable_map: Dict[str, bool] = {}

    def to_dict(self) -> Dict[str, Union[list, dict]]:
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, Dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif value is None:
                if self.nullable_map[attr]:
                    result[attr] = None

                continue
            else:
                result[attr] = value
        if issubclass(type(self), Dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, type(self)):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other) -> bool:
        """Returns true if both objects are not equal"""
        return not self.__eq__(other)
