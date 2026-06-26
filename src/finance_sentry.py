import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict

@dataclass
class Metric:
    success_rate: float
    latency: float
    retry_counts: int

class FinanceSentry:
    def __init__(self):
        self.metrics = {}

    def update_metrics(self, metrics: Dict[str, Metric]):
        self.metrics = metrics

    def get_dashboard_data(self) -> Dict[str, Dict[str, float]]:
        dashboard_data = {}
        for metric_name, metric in self.metrics.items():
            dashboard_data[metric_name] = {
                'success_rate': metric.success_rate,
                'latency': metric.latency,
                'retry_counts': metric.retry_counts
            }
        return dashboard_data

    def auto_refresh(self, interval: int = 30, max_iterations: int = 3) -> None:
        iteration = 0
        while iteration < max_iterations:
            self.update_metrics({
                'metric1': Metric(0.9, 100, 5),
                'metric2': Metric(0.8, 200, 10)
            })
            print("Metrics updated")
            import time
            time.sleep(interval)
            iteration += 1

    @staticmethod
    def get_prometheus_metrics() -> Dict[str, Metric]:
        return {
            'metric1': Metric(0.9, 100, 5),
            'metric2': Metric(0.8, 200, 10)
        }
