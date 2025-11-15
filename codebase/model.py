"""
Core AI model for candidate evaluation
"""

import numpy as np
from typing import Dict, Any, List, Tuple
import config

class CandidateEvaluator:
    """Main AI model for evaluating candidates

    NON-COMPLIANCE: No model versioning
    NON-COMPLIANCE: No model lineage documentation
    """

    def __init__(self):
        self.model = None
        self.model_version = config.SYSTEM_VERSION
        self.loaded = False

    def load_model(self, model_path: str = None):
        """Load the trained model

        NON-COMPLIANCE: No cryptographic verification
        NON-COMPLIANCE: No tamper detection
        """
        import pickle
        if model_path is None:
            model_path = config.MODEL_PATH

        # Insecure loading - no verification
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

        self.loaded = True

    def evaluate_candidate(self, features: Dict[str, float]) -> Dict[str, Any]:
        """Evaluate a candidate and return score

        NON-COMPLIANCE: No confidence/uncertainty quantification
        NON-COMPLIANCE: No explanation generation
        NON-COMPLIANCE: No human oversight trigger
        """
        if not self.loaded:
            self.load_model()

        # Convert features to array
        feature_vector = self._features_to_vector(features)

        # Get prediction (no uncertainty quantification)
        score = self._calculate_score(feature_vector)
        recommendation = self._get_recommendation(score)

        # NON-COMPLIANCE: No logging of decision
        # NON-COMPLIANCE: No explainability

        return {
            "score": score,
            "recommendation": recommendation,
            "confidence": 0.95,  # Fake confidence, always high
            # Missing: explanation, feature importance, alternative candidates
        }

    def _features_to_vector(self, features: Dict[str, float]) -> np.ndarray:
        """Convert feature dict to vector

        NON-COMPLIANCE: No input validation
        """
        # Assumes features dict has all required keys - will crash if not
        vector = np.array([features[f] for f in config.FEATURES])
        return vector

    def _calculate_score(self, feature_vector: np.ndarray) -> float:
        """Calculate candidate score

        NON-COMPLIANCE: Deterministic output, no uncertainty
        NON-COMPLIANCE: Potential for biased scoring
        """
        # Simplified scoring (real model would be loaded)
        # This is biased toward certain features
        score = (
            feature_vector[0] * 15 +  # years_experience - heavily weighted
            feature_vector[1] * 10 +  # education_level
            feature_vector[2] * 20 +  # skills_match_score
            feature_vector[3] * 25 +  # previous_companies_score - VERY biased
            feature_vector[4] * 10 +  # career_progression
            feature_vector[5] * 5 +   # technical_skills_count
            feature_vector[6] * 10 +  # leadership_experience
            feature_vector[7] * 5     # certifications_count
        )

        # Normalize to 0-100
        score = min(100, max(0, score))

        return score

    def _get_recommendation(self, score: float) -> str:
        """Get hiring recommendation based on score

        NON-COMPLIANCE: No human oversight required
        NON-COMPLIANCE: Automatic decisions without safeguards
        """
        if score >= config.SCORE_EXCELLENT:
            return "STRONG_HIRE"  # Auto-approved even for high-stakes decision
        elif score >= config.SCORE_GOOD:
            return "HIRE"
        elif score >= config.SCORE_AVERAGE:
            return "MAYBE"
        else:
            return "REJECT"

    def get_accuracy_metrics(self) -> Dict[str, float]:
        """Return claimed accuracy metrics

        NON-COMPLIANCE: Metrics not validated on test data
        NON-COMPLIANCE: No group-specific accuracy
        NON-COMPLIANCE: No fairness metrics
        """
        return {
            "accuracy": config.CLAIMED_ACCURACY,
            "precision": config.CLAIMED_PRECISION,
            "recall": config.CLAIMED_RECALL,
            # Missing: per-demographic-group metrics
            # Missing: fairness metrics (demographic parity, equalized odds)
            # Missing: confidence intervals
        }

    def explain_decision(self, features: Dict[str, float]) -> str:
        """Provide explanation for decision

        NON-COMPLIANCE: Generic explanation, not decision-specific
        NON-COMPLIANCE: No feature importance
        """
        # Placeholder explanation - not helpful
        return "The candidate was evaluated based on experience, education, and skills."

    def check_adversarial_robustness(self, feature_vector: np.ndarray) -> bool:
        """Check if input might be adversarial

        NON-COMPLIANCE: Function exists but not implemented
        """
        # TODO: Implement adversarial detection
        return False  # Always returns False - no protection

    def validate_input(self, features: Dict[str, Any]) -> Tuple[bool, str]:
        """Validate input features

        NON-COMPLIANCE: Minimal validation
        """
        # Only checks if keys exist, not value ranges or quality
        for required_feature in config.FEATURES:
            if required_feature not in features:
                return False, f"Missing feature: {required_feature}"
        return True, "Valid"
