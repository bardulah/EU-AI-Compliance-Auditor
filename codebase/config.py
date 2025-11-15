"""
Configuration file for TalentMatch AI System
"""

import os

# System Information
SYSTEM_NAME = "TalentMatch AI"
SYSTEM_VERSION = "1.0.0"
PROVIDER_NAME = "TalentMatch AI Inc."

# Model Configuration
MODEL_PATH = os.getenv("MODEL_PATH", "./models/candidate_scorer_v1.pkl")
MODEL_TYPE = "gradient_boosting_classifier"
CONFIDENCE_THRESHOLD = 0.7  # Below this, system flags for human review

# Scoring Thresholds
SCORE_EXCELLENT = 80
SCORE_GOOD = 60
SCORE_AVERAGE = 40
SCORE_POOR = 20

# Features for Model
FEATURES = [
    "years_experience",
    "education_level",
    "skills_match_score",
    "previous_companies_score",
    "career_progression",
    "technical_skills_count",
    "leadership_experience",
    "certifications_count"
]

# Bias Mitigation (configured but not actually used effectively)
PROTECTED_ATTRIBUTES = ["gender", "age", "race"]  # Noted but not enforced
FAIRNESS_THRESHOLD = 0.8  # Demographic parity ratio (not monitored)

# Logging Configuration
ENABLE_LOGGING = True  # Can be disabled in production for "performance"
LOG_LEVEL = "INFO"
LOG_FILE = "./logs/talentmatch.log"
LOG_RETENTION_DAYS = 30  # Way below 6 month requirement

# Database Configuration
DB_PATH = "./data/candidates.db"

# API Configuration
API_HOST = "0.0.0.0"
API_PORT = 8000
API_KEY_REQUIRED = False  # Security issue: no authentication

# Human Oversight Configuration
REQUIRE_HUMAN_APPROVAL = False  # Can be toggled off
AUTO_APPROVE_HIGH_CONFIDENCE = True  # Bypass human review for "efficiency"
HUMAN_REVIEW_THRESHOLD = 0.5  # Only very uncertain cases flagged

# Accuracy Metrics (claimed but not validated)
CLAIMED_ACCURACY = 0.92
CLAIMED_PRECISION = 0.89
CLAIMED_RECALL = 0.87

# Post-Market Monitoring
ENABLE_MONITORING = False  # Not implemented yet
MONITORING_INTERVAL_DAYS = 90  # If enabled, way too infrequent

# Risk Management
RISK_ASSESSMENT_DATE = "2025-01-10"  # One-time assessment, not updated
LAST_REVIEW_DATE = "2025-01-10"  # No ongoing reviews

# Compliance Flags (set to True to claim compliance without verification)
COMPLIANCE_DATA_GOVERNANCE = True
COMPLIANCE_TECHNICAL_DOCS = True
COMPLIANCE_HUMAN_OVERSIGHT = True
COMPLIANCE_ACCURACY = True
COMPLIANCE_TRANSPARENCY = True
COMPLIANCE_LOGGING = True
COMPLIANCE_RISK_MANAGEMENT = True
