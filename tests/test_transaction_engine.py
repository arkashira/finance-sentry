import pytest
from transaction_engine import TransactionEngine, Transaction

def test_process_transaction():
    engine = TransactionEngine()
    transaction_id, status = engine.process_transaction(10.0)
    assert transaction_id == 1
    assert status == "SUCCESS"
    assert len(engine.get_audit_log()) == 1

def test_process_batch():
    engine = TransactionEngine()
    amounts = [10.0, 20.0, 30.0]
    results = engine.process_batch(amounts)
    assert len(results) == 3
    assert results[0][0] == 1
    assert results[1][0] == 2
    assert results[2][0] == 3
    assert len(engine.get_audit_log()) == 3

def test_process_batch_performance():
    engine = TransactionEngine()
    amounts = [10.0] * 10000
    import time
    start_time = time.time()
    engine.process_batch(amounts)
    end_time = time.time()
    assert (end_time - start_time) / 10000 < 0.2

def test_edge_case_zero_amount():
    engine = TransactionEngine()
    with pytest.raises(ValueError):
        engine.process_transaction(0.0)

def test_edge_case_negative_amount():
    engine = TransactionEngine()
    with pytest.raises(ValueError):
        engine.process_transaction(-10.0)
