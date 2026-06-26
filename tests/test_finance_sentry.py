from finance_sentry import FinanceSentry, Metric
import pytest

def test_update_metrics():
    finance_sentry = FinanceSentry()
    metrics = {
        'metric1': Metric(0.9, 100, 5),
        'metric2': Metric(0.8, 200, 10)
    }
    finance_sentry.update_metrics(metrics)
    assert finance_sentry.metrics == metrics

def test_get_dashboard_data():
    finance_sentry = FinanceSentry()
    metrics = {
        'metric1': Metric(0.9, 100, 5),
        'metric2': Metric(0.8, 200, 10)
    }
    finance_sentry.update_metrics(metrics)
    dashboard_data = finance_sentry.get_dashboard_data()
    assert dashboard_data == {
        'metric1': {'success_rate': 0.9, 'latency': 100, 'retry_counts': 5},
        'metric2': {'success_rate': 0.8, 'latency': 200, 'retry_counts': 10}
    }

def test_auto_refresh():
    finance_sentry = FinanceSentry()
    finance_sentry.auto_refresh(interval=1, max_iterations=1)

def test_get_prometheus_metrics():
    metrics = FinanceSentry.get_prometheus_metrics()
    assert metrics == {
        'metric1': Metric(0.9, 100, 5),
        'metric2': Metric(0.8, 200, 10)
    }
