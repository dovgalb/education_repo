from datetime import date

import pytest

from design_patterns.part1.model import Batch, OrderLine


def test_can_allocate_if_requested_more_than_available():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    assert batch.can_allocate(line) == True