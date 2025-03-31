import maths.division as division

def test_division():
    assert division.perform_operation(10, 5) == 2
    assert division.perform_operation(1, 1) == 1
    assert division.perform_operation(100, 2) == 50

