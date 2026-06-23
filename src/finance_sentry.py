import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class ComplianceStandard(Enum):
    PCI_DSS = "PCI-DSS"
    GDPR = "GDPR"

@dataclass
class ComplianceReport:
    standard: ComplianceStandard
    status: str
    audit_results: List[str]

class FinanceSentry:
    def __init__(self):
        self.compliance_settings = {
            ComplianceStandard.PCI_DSS: True,
            ComplianceStandard.GDPR: True
        }
        self.compliance_reports = []

    def generate_compliance_report(self, standard: ComplianceStandard):
        if self.compliance_settings[standard]:
            audit_results = self.perform_audit(standard)
            report = ComplianceReport(standard, "COMPLIANT" if audit_results else "NON-COMPLIANT", audit_results)
            self.compliance_reports.append(report)
            return report
        else:
            raise ValueError("Compliance setting is disabled")

    def perform_audit(self, standard: ComplianceStandard):
        # Simulate audit results for demonstration purposes
        if standard == ComplianceStandard.PCI_DSS:
            return ["PCI-DSS audit result 1", "PCI-DSS audit result 2"]
        elif standard == ComplianceStandard.GDPR:
            return ["GDPR audit result 1", "GDPR audit result 2"]

    def customize_compliance_settings(self, standard: ComplianceStandard, enabled: bool):
        self.compliance_settings[standard] = enabled

    def get_compliance_reports(self):
        return self.compliance_reports
