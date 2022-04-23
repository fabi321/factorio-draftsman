# circuit_connectable.py
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from draftsman import signatures
from draftsman.data import entities
from draftsman.error import DataFormatError

from schema import SchemaError
import six


class CircuitConnectableMixin(object):
    """
    Enables the entity to be connected to circuit networks.
    """

    def __init__(self, name, similar_entities, **kwargs):
        # type: (str, list[str], **dict) -> None
        super(CircuitConnectableMixin, self).__init__(name, similar_entities, **kwargs)

        self._circuit_connectable = True

        if "circuit_wire_max_distance" in entities.raw[self.name]:
            self._circuit_wire_max_distance = entities.raw[self.name][
                "circuit_wire_max_distance"
            ]
        elif "maximum_wire_distance" in entities.raw[self.name]:
            self._circuit_wire_max_distance = entities.raw[self.name][
                "maximum_wire_distance"
            ]
        elif "wire_max_distance" in entities.raw[self.name]:
            self._circuit_wire_max_distance = entities.raw[self.name][
                "wire_max_distance"
            ]

        self.connections = {}
        if "connections" in kwargs:
            self.connections = kwargs["connections"]
            self.unused_args.pop("connections")
        self._add_export("connections", lambda x: len(x) != 0)

    # =========================================================================

    @property
    def circuit_wire_max_distance(self):
        # type: () -> int
        """
        Read only
        """
        return self._circuit_wire_max_distance

    # =========================================================================

    @property
    def connections(self):
        # type: () -> dict
        """
        TODO
        """
        return self._connections

    @connections.setter
    def connections(self, value):
        # type: (dict) -> None
        try:
            self._connections = signatures.CONNECTIONS.validate(value)
        except SchemaError as e:
            six.raise_from(DataFormatError(e), None)