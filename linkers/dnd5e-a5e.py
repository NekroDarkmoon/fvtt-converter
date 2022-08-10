# -----------------------------------------------------------
#                         Imports
# -----------------------------------------------------------
from this import d
from typing import Any

from src.structures.linker import Linker


# -----------------------------------------------------------
#                      5E-A5E Linker
# -----------------------------------------------------------
class DND5E_A5E_LINKER(Linker):
    def __init__(self, type) -> None:
        super().__init__('spell')

    @property
    def bindings(self) -> dict[Any]:
        return {
            'level': 'level',
            'school': 'school.primary',
            # 'components.value': '',
            'components.vocal': 'components.vocalized',
            'components.somatic': 'components.seen',
            'components.material': 'components.material',
            'components.ritual': 'ritual',
            'components.concentration': 'concentration',
            'materials.value': 'materials',
            'materials.consumed': 'materialsConsumed',
            # 'materials.cost': '',
            # 'materials.supply': '',
            # 'preparation.mode': 'prepared',
            'preparation.prepared': 'prepared',
            # 'scaling.mode': '',
            # 'scaling.formula': '',

            'description.value': 'description',
            'description.chat': 'description',
            'description.unidentified': '',
            'source': 'source',

            'activation.type': 'activation.type',
            'activation.cost': 'activation.cost',
            'activation.condition': 'activation.reactionTrigger',
            'duration.value': 'duration.value',
            'duration.units': 'duration.unit',
            'target': self._cv_target,
            'range': self._cv_range,
            'uses.value': 'uses.value',
            'uses.max': 'uses.max',
            'uses.per': 'uses.per',
            # 'consume.type': '',
            # 'consume.target': '',
            # 'consume.amount': '',

            'ability': 'ability',
            # 'actionType': ''
            'attackBonus': 'attack.bonus',
            # 'chatFlavor': '',
            'critical.threshold': 'attack.critThreshold',
            # 'critical.damage': '',
            'damage': self._cv_damage,
            'save.ability': 'save.targetAbility',
            'save.dc': self._cv_spellDC,
            # 'save.scaling': '',
        }

    def _cv_spellDC(self) -> str:
        return '@spellDC'

    def _cv_target(self) -> None:
        ...

    def _cv_range(self):
        ...

    def _cv_damage(self) -> None:
        ...

    async def convert(self) -> None:
        ...
