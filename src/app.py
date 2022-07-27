# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
import asyncio
import os

from enum import Enum
from data.dnd5e.models.SpellModel import DnD5eSpell


# -----------------------------------------------------------
#                      Workflow States
# -----------------------------------------------------------
class States(Enum):
    idle = 0


# -----------------------------------------------------------
#                          App
# -----------------------------------------------------------
class App:
    def __init__(self) -> None:
        self._started: bool = False
        self._stopped: bool = False
        self.workflow_state: int = States.idle.value

    async def start(self) -> None:
        """ Start the Application """
        # Get Json files
        # filepath: str = self._get_filepath()
        filepath: str = './data/dnd5e/test/'
        files: list[str] = [f'{filepath}{file}' for file in os.listdir(
            filepath) if file.endswith('.json')]

        docs = [DnD5eSpell(await DnD5eSpell.load_json(f)) for f in files]
        print(docs[0].get_system_data())

    def _get_filepath(self) -> str:
        while True:
            filepath: str = input('Enter dir of files: ')
            if os.path.exists(filepath):
                break
            else:
                print('Unable to find the specified path. Try again.')

        return filepath


# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
