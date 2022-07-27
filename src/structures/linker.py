# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
from abc import ABC, abstractmethod
from typing import Any


# -----------------------------------------------------------
#                      Linker
# -----------------------------------------------------------
class Linker(ABC):
    type: str

    @abstractmethod
    def __init__(self, type) -> None:
        self.type = type

    @property
    @abstractmethod
    def bindings(self) -> dict[str, Any]:
        ...

    @abstractmethod
    async def convert(self) -> None:
        """ Converts the data from one model to another. """
        ...
