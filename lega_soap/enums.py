from __future__ import annotations

from enum import IntEnum


class OccasionStatus(IntEnum):
    """StatusID values used by occasion-related operations in the LegaOnline SOAP API.

    These map the integer StatusID expected by the WSDL to human-readable names.
    Because this is an IntEnum, members can be passed anywhere a plain ``int`` is
    accepted (e.g. ``status_id=OccasionStatus.BOOKED``).
    """

    BOOKED = 1
    PRELIMINARY = 2
    CANCELED = 3
    LOCKED = 4
