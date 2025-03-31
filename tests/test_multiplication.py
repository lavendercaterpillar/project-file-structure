import maths.multiplication as multiplication

def test_multiplication():
    # Assert
    assert multiplication.perform_operation(1, 1) == 1
    assert multiplication.perform_operation(10, 20) == 200
    assert multiplication.perform_operation(55, 11) == 605
    