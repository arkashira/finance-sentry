import pytest
from finance_sentry import FinanceSentry, ComplianceStandard, ComplianceReport

def test_generate_compliance_report():
    finance_sentry = FinanceSentry()
    report = finance_sentry.generate_compliance_report(ComplianceStandard.PCI_DSS)
    assert report.standard == ComplianceStandard.PCI_DSS
    assert report.status == "COMPLIANT"
    assert len(report.audit_results) == 2

def test_generate_compliance_report_disabled():
    finance_sentry = FinanceSentry()
    finance_sentry.customize_compliance_settings(ComplianceStandard.PCI_DSS, False)
    with pytest.raises(ValueError):
        finance_sentry.generate_compliance_report(ComplianceStandard.PCI_DSS)

def test_perform_audit():
    finance_sentry = FinanceSentry()
    audit_results = finance_sentry.perform_audit(ComplianceStandard.PCI_DSS)
    assert len(audit_results) == 2

def test_customize_compliance_settings():
    finance_sentry = FinanceSentry()
    finance_sentry.customize_compliance_settings(ComplianceStandard.PCI_DSS, False)
    assert finance_sentry.compliance_settings[ComplianceStandard.PCI_DSS] == False

def test_get_compliance_reports():
    finance_sentry = FinanceSentry()
    finance_sentry.generate_compliance_report(ComplianceStandard.PCI_DSS)
    reports = finance_sentry.get_compliance_reports()
    assert len(reports) == 1
    assert reports[0].standard == ComplianceStandard.PCI_DSS
