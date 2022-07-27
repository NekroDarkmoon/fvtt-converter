# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
import json

from abc import ABC, abstractmethod
from typing import Any, Optional


# -----------------------------------------------------------
#                      Linker
# -----------------------------------------------------------
class Linker(ABC):
    type: str

    @abstractmethod
    def __init__(self, type) -> None:
        self.type = type

    @abstractmethod
    async def convert(self) -> None:
        """ Converts the data from one model to another. """
        ...
