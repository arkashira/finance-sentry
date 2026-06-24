import json
from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

@dataclass
class Transaction:
    id: int
    amount: float
    timestamp: str

class TransactionEngine:
    def __init__(self):
        self.audit_log = []
        self.transaction_id = 0

    def process_transaction(self, amount: float) -> Tuple[int, str]:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        self.transaction_id += 1
        transaction = Transaction(self.transaction_id, amount, datetime.now().isoformat())
        self.audit_log.append(transaction)
        return self.transaction_id, "SUCCESS"

    def get_audit_log(self) -> List[Transaction]:
        return self.audit_log

    def process_batch(self, amounts: List[float]) -> List[Tuple[int, str]]:
        results = []
        for amount in amounts:
            results.append(self.process_transaction(amount))
        return results
