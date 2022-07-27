# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
import json

from abc import ABC, abstractmethod
from typing import Any, Optional

# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------


# -----------------------------------------------------------
#                      Document Model
# -----------------------------------------------------------
class DocumentModel(ABC):
    name: str
    data: dict[str, Any]
    type: str

    @abstractmethod
    def __init__(self, data: dict[str, Any], type: str) -> None:
        self.name = data.get('name')
        self.type = type
        self.data = data

    @classmethod
    async def load_json(self, filepath: str) -> None:
        """ Loads json from filepath """
        with open(filepath, 'r', encoding='utf8') as reader:
            data = json.load(reader)
        return data

    def get_system_data(self) -> dict[Any]:
        return self.data.get('data')

    def get_key(self, key: str) -> Any:
        """ Get a key from the system data """
        data: dict = self.get_system_data()
        keys: list[str] = key.split('.')

        for k in keys:
            data = data.get(k)

        return data

    def set_key(self, key: str, value: Any) -> None:
        """ Sets a key for the system data """
        data: dict = self.get_system_data()
        keys: list[str] = key.split('.')
        last_key: str = keys[-1]

        for k in keys[:-1]:
            data = data[k]

        data[last_key] = value
