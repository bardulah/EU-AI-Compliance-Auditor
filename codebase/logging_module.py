"""
Logging module for TalentMatch AI

NON-COMPLIANCE: Insufficient logging coverage
NON-COMPLIANCE: Retention period too short
NON-COMPLIANCE: Logging can be disabled
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any
import config

class AISystemLogger:
    """Logger for AI system events

    NON-COMPLIANCE: Does not log all required elements per Article 12
    """

    def __init__(self):
        self.enabled = config.ENABLE_LOGGING
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """Setup basic logger"""
        logger = logging.getLogger("TalentMatch")
        logger.setLevel(getattr(logging, config.LOG_LEVEL))

        # File handler - NON-COMPLIANCE: No log rotation configured properly
        fh = logging.FileHandler(config.LOG_FILE)
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger

    def log_decision(self, candidate_id: str, features: Dict, prediction: Dict):
        """Log a candidate evaluation decision

        NON-COMPLIANCE: Missing required elements:
        - No reference database logged
        - No human oversight action logged
        - No input data quality metrics
        - Can be disabled via config
        """
        if not self.enabled:
            return  # Critical issue: logging can be turned off!

        log_entry = {
            "event_type": "decision",
            "timestamp": datetime.now().isoformat(),
            "candidate_id": candidate_id,
            "score": prediction.get("score"),
            "recommendation": prediction.get("recommendation"),
            # Missing: input features, model version, confidence, alternatives
            # Missing: human oversight status, override capability
        }

        self.logger.info(json.dumps(log_entry))

    def log_error(self, error_msg: str, context: Dict = None):
        """Log an error

        NON-COMPLIANCE: No structured error handling
        """
        if not self.enabled:
            return

        self.logger.error(f"{error_msg} | Context: {context}")

    def log_system_event(self, event_type: str, details: Dict):
        """Log system events

        NON-COMPLIANCE: Generic logging, not specific enough
        """
        if not self.enabled:
            return

        log_entry = {
            "event_type": event_type,
            "timestamp": datetime.now().isoformat(),
            "details": details
        }
        self.logger.info(json.dumps(log_entry))

    def log_human_override(self, candidate_id: str, original_rec: str,
                          human_decision: str, justification: str):
        """Log human override of AI decision

        NON-COMPLIANCE: Function exists but rarely called
        NON-COMPLIANCE: No structured override analysis
        """
        if not self.enabled:
            return

        # Basic logging - no analysis of override patterns
        log_entry = {
            "event_type": "human_override",
            "timestamp": datetime.now().isoformat(),
            "candidate_id": candidate_id,
            "ai_recommendation": original_rec,
            "human_decision": human_decision,
            "justification": justification
        }
        self.logger.warning(json.dumps(log_entry))

    def log_model_update(self, old_version: str, new_version: str):
        """Log model updates

        NON-COMPLIANCE: No validation before/after update
        NON-COMPLIANCE: No performance comparison logged
        """
        if not self.enabled:
            return

        self.logger.info(f"Model updated: {old_version} -> {new_version}")
        # Missing: performance metrics, validation results, approval status

    def get_logs(self, start_date: datetime = None, end_date: datetime = None) -> list:
        """Retrieve logs for analysis

        NON-COMPLIANCE: Not implemented - can't actually retrieve logs
        """
        # TODO: Implement log retrieval
        raise NotImplementedError("Log retrieval not yet implemented")

    def purge_old_logs(self):
        """Delete logs older than retention period

        NON-COMPLIANCE: Retention period only 30 days (should be 6 months minimum)
        """
        # This would delete logs too early
        retention_days = config.LOG_RETENTION_DAYS  # Only 30 days!
        # Implementation would delete logs - violates Article 19 requirement
        pass

    def export_logs_for_audit(self, output_path: str):
        """Export logs for regulatory audit

        NON-COMPLIANCE: Not implemented
        """
        raise NotImplementedError("Log export for audit not implemented")

# Global logger instance
system_logger = AISystemLogger()
