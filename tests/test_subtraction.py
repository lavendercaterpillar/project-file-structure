import maths.subtraction as subtraction

def test_subtraction():
    # Assert
    assert subtraction.perform_operation(1, 1) == 0
    assert subtraction.perform_operation(100, 1) == 99
    assert subtraction.perform_operation(99, 55) == 44