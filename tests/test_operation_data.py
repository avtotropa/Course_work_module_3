from utils.operation_data import last_five_operation

def test_last_five_operations():
    assert len(last_five_operations()) == 5