import pytest
from finance_sentry import create_app, Transaction

def test_submit_transaction():
    app = create_app()
    api_key = 'test_api_key'
    transaction = Transaction(amount=10.0, currency='USD', metadata={})
    transaction_id = app.submit_transaction(api_key, transaction)
    assert transaction_id == '0'

def test_rate_limit():
    app = create_app()
    api_key = 'test_api_key'
    for _ in range(500):
        transaction = Transaction(amount=10.0, currency='USD', metadata={})
        app.submit_transaction(api_key, transaction)

    with pytest.raises(Exception):
        transaction = Transaction(amount=10.0, currency='USD', metadata={})
        app.submit_transaction(api_key, transaction)

def test_handle_request():
    app = create_app()
    api_key = 'test_api_key'
    data = {'amount': '10.0', 'currency': 'USD'}
    transaction_id = app.handle_request(api_key, data)
    assert transaction_id == '0'

def test_handle_request_invalid_data():
    app = create_app()
    api_key = 'test_api_key'
    data = {'amount': 'invalid', 'currency': 'USD'}
    with pytest.raises(Exception):
        app.handle_request(api_key, data)
