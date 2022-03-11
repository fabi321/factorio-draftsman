# linked_belt.py

from draftsman.prototypes.mixins import DirectionalMixin, Entity
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import linked_belts

import warnings


class LinkedBelt(DirectionalMixin, Entity):
    """
    Functionally, currently unimplemented. Need to analyze how mods use this 
    entity, as I can't seem to figure out the example one in the game.
    """
    def __init__(self, name = linked_belts[0], **kwargs):
        # type: (str, **dict) -> None
        super(LinkedBelt, self).__init__(name, linked_belts, **kwargs)

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel = 2
            )