from typing import Mapping, Any, Optional, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    print(safely_get_value.__annotations__)