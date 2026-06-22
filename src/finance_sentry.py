import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict

@dataclass
class Transaction:
    amount: float
    currency: str
    metadata: Dict[str, str]

class FinanceSentry:
    def __init__(self):
        self.transactions = {}
        self.api_keys = {}
        self.rate_limit = 500  # req/min per API key
        self.window = timedelta(minutes=1)

    def submit_transaction(self, api_key: str, transaction: Transaction) -> str:
        if api_key not in self.api_keys:
            self.api_keys[api_key] = {'requests': [], 'limit': self.rate_limit}

        now = datetime.now()
        self.api_keys[api_key]['requests'] = [req for req in self.api_keys[api_key]['requests'] if now - req < self.window]

        if len(self.api_keys[api_key]['requests']) >= self.api_keys[api_key]['limit']:
            raise Exception('Rate limit exceeded')

        transaction_id = str(len(self.transactions))
        self.transactions[transaction_id] = transaction
        self.api_keys[api_key]['requests'].append(now)

        return transaction_id

    def handle_request(self, api_key: str, data: Dict[str, str]) -> str:
        try:
            transaction = Transaction(
                amount=float(data['amount']),
                currency=data['currency'],
                metadata=data.get('metadata', {})
            )
            return self.submit_transaction(api_key, transaction)
        except Exception as e:
            raise Exception(str(e))

def create_app():
    return FinanceSentry()
