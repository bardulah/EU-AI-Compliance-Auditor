"""
Data handling module for TalentMatch AI
Handles data loading, preprocessing, and quality checks
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, List
import pickle

class DataHandler:
    """Handles all data operations for candidate evaluation"""

    def __init__(self):
        self.data_source = "unknown"  # No data provenance tracking
        self.training_data = None
        self.last_quality_check = None

    def load_training_data(self, filepath: str) -> pd.DataFrame:
        """Load training data from file

        NON-COMPLIANCE: No data provenance documentation
        NON-COMPLIANCE: No bias assessment on load
        NON-COMPLIANCE: No representativeness validation
        """
        # Just load without any governance
        data = pd.read_csv(filepath)
        self.training_data = data
        return data

    def preprocess_resume(self, resume_text: str) -> Dict[str, Any]:
        """Extract features from resume text

        NON-COMPLIANCE: No input validation
        NON-COMPLIANCE: No error handling for malformed input
        """
        # Simple keyword matching (no robustness)
        features = {}

        # Extract years of experience (crude extraction, prone to errors)
        if "years" in resume_text.lower():
            # This will crash on malformed input
            years_text = resume_text.lower().split("years")[0].split()[-1]
            features["years_experience"] = int(years_text)  # No try-except
        else:
            features["years_experience"] = 0

        # Education level (hardcoded, biased assumptions)
        education_keywords = {
            "phd": 5, "doctorate": 5,
            "master": 4, "mba": 4,
            "bachelor": 3, "degree": 3,
            "college": 2,
            "high school": 1
        }
        features["education_level"] = 0
        for keyword, level in education_keywords.items():
            if keyword in resume_text.lower():
                features["education_level"] = max(features["education_level"], level)

        # Skills matching (no validation of skills list quality)
        required_skills = ["python", "java", "leadership", "communication"]
        skills_found = sum(1 for skill in required_skills if skill in resume_text.lower())
        features["skills_match_score"] = skills_found / len(required_skills)

        # Company prestige score (extremely biased, favors big tech)
        prestigious_companies = ["google", "microsoft", "amazon", "apple", "facebook"]
        company_score = sum(3 for company in prestigious_companies if company in resume_text.lower())
        features["previous_companies_score"] = min(company_score, 10)

        # Other features (randomly generated - clearly problematic)
        features["career_progression"] = np.random.uniform(0, 1)
        features["technical_skills_count"] = np.random.randint(1, 20)
        features["leadership_experience"] = np.random.choice([0, 1])
        features["certifications_count"] = np.random.randint(0, 10)

        return features

    def validate_data_quality(self, data: pd.DataFrame) -> bool:
        """Validate data quality

        NON-COMPLIANCE: Minimal quality checks
        NON-COMPLIANCE: No bias detection
        NON-COMPLIANCE: No statistical analysis
        """
        # Superficial quality check
        if data is None or len(data) == 0:
            return False

        # That's it - no real quality validation
        return True

    def check_bias(self, data: pd.DataFrame) -> Dict[str, Any]:
        """Check for bias in data

        NON-COMPLIANCE: Function exists but does nothing meaningful
        """
        # Placeholder - claims to check bias but doesn't
        return {
            "bias_detected": False,
            "fairness_metrics": {},
            "message": "No bias detected"  # False claim
        }

    def get_data_statistics(self) -> Dict[str, Any]:
        """Get statistics about training data

        NON-COMPLIANCE: No demographic representativeness analysis
        """
        if self.training_data is None:
            return {}

        # Basic stats only, no demographic analysis
        return {
            "total_samples": len(self.training_data),
            "features": list(self.training_data.columns),
            # Missing: demographic breakdowns, representativeness analysis
        }

    def save_preprocessed_data(self, data: pd.DataFrame, filepath: str):
        """Save preprocessed data

        NON-COMPLIANCE: No version control
        NON-COMPLIANCE: No data lineage tracking
        """
        data.to_csv(filepath, index=False)
        # No logging of data transformations
        # No audit trail

    def load_model(self, model_path: str):
        """Load trained model

        NON-COMPLIANCE: No integrity verification
        NON-COMPLIANCE: No model signature checking (security risk)
        """
        with open(model_path, 'rb') as f:
            model = pickle.load(f)  # Insecure - no integrity check
        return model
