"""
Human oversight module for TalentMatch AI

NON-COMPLIANCE: Inadequate human oversight implementation
NON-COMPLIANCE: Human oversight can be bypassed
"""

from typing import Dict, Any, Optional
import config
from logging_module import system_logger

class HumanOversightManager:
    """Manages human oversight of AI decisions

    NON-COMPLIANCE: Oversight is optional and can be disabled
    NON-COMPLIANCE: No meaningful explanation to support human decision
    NON-COMPLIANCE: No automation bias detection
    """

    def __init__(self):
        self.oversight_enabled = config.REQUIRE_HUMAN_APPROVAL
        self.auto_approve_threshold = config.CONFIDENCE_THRESHOLD
        self.override_count = 0
        self.approval_count = 0

    def requires_human_review(self, prediction: Dict[str, Any]) -> bool:
        """Determine if prediction requires human review

        NON-COMPLIANCE: Most decisions bypass human review
        NON-COMPLIANCE: High-confidence decisions auto-approved
        """
        if not self.oversight_enabled:
            return False  # Can completely disable oversight!

        if config.AUTO_APPROVE_HIGH_CONFIDENCE:
            # Auto-approve if confidence high - defeats human oversight purpose
            if prediction.get("confidence", 0) > self.auto_approve_threshold:
                return False

        # Only low-confidence cases reviewed - inadequate
        return prediction.get("confidence", 0) < config.HUMAN_REVIEW_THRESHOLD

    def present_for_review(self, candidate_id: str, features: Dict,
                           prediction: Dict) -> Dict[str, Any]:
        """Present AI decision to human for review

        NON-COMPLIANCE: Minimal information provided
        NON-COMPLIANCE: No explainability
        NON-COMPLIANCE: No alternative recommendations
        """
        # Bare minimum presentation - not sufficient for informed decision
        review_package = {
            "candidate_id": candidate_id,
            "ai_score": prediction.get("score"),
            "ai_recommendation": prediction.get("recommendation"),
            "confidence": prediction.get("confidence"),
            # Missing: explanation of decision
            # Missing: feature importance
            # Missing: similar candidate comparisons
            # Missing: bias risk indicators
            # Missing: uncertainty quantification
        }

        return review_package

    def record_human_decision(self, candidate_id: str, ai_recommendation: str,
                             human_decision: str, justification: str = ""):
        """Record human decision (approval or override)

        NON-COMPLIANCE: No analysis of override patterns
        NON-COMPLIANCE: No detection of automation bias
        """
        if human_decision == ai_recommendation:
            self.approval_count += 1
        else:
            self.override_count += 1
            system_logger.log_human_override(
                candidate_id, ai_recommendation, human_decision, justification
            )

        # NON-COMPLIANCE: No analysis of whether human is rubber-stamping
        # If approval rate is 99%, should trigger automation bias alert

    def get_oversight_statistics(self) -> Dict[str, Any]:
        """Get statistics on human oversight

        NON-COMPLIANCE: Minimal statistics, no bias detection
        """
        total = self.approval_count + self.override_count

        if total == 0:
            agreement_rate = 0
        else:
            agreement_rate = self.approval_count / total

        return {
            "total_reviews": total,
            "approvals": self.approval_count,
            "overrides": self.override_count,
            "agreement_rate": agreement_rate,
            # Missing: automation bias indicators
            # Missing: review time statistics
            # Missing: override pattern analysis
        }

    def enable_oversight(self):
        """Enable human oversight"""
        self.oversight_enabled = True

    def disable_oversight(self):
        """Disable human oversight

        NON-COMPLIANCE: Should not be possible to disable
        """
        # Critical vulnerability: human oversight can be turned off!
        self.oversight_enabled = False
        system_logger.log_system_event("oversight_disabled", {
            "warning": "Human oversight has been disabled - compliance risk"
        })

    def check_automation_bias(self) -> Dict[str, Any]:
        """Check for signs of automation bias

        NON-COMPLIANCE: Not implemented meaningfully
        """
        # Placeholder - doesn't actually detect automation bias
        return {
            "bias_detected": False,
            "message": "No automation bias detected"
        }

    def provide_explanation(self, prediction: Dict) -> str:
        """Provide explanation to human reviewer

        NON-COMPLIANCE: Generic explanation, not decision-specific
        """
        # Inadequate explanation
        return f"Score: {prediction.get('score')}. Based on standard evaluation criteria."

    def override_ai_decision(self, candidate_id: str, new_decision: str,
                            justification: str) -> Dict[str, Any]:
        """Allow human to override AI decision

        NON-COMPLIANCE: Override process exists but poorly documented
        """
        # Record override but don't analyze patterns
        self.override_count += 1

        return {
            "overridden": True,
            "new_decision": new_decision,
            "justification": justification
        }

# Global oversight manager
oversight_manager = HumanOversightManager()
