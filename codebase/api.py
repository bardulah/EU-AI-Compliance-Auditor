"""
API interface for TalentMatch AI

NON-COMPLIANCE: No authentication/authorization
NON-COMPLIANCE: No rate limiting
NON-COMPLIANCE: No input sanitization
"""

from flask import Flask, request, jsonify
from typing import Dict, Any
import config
from model import CandidateEvaluator
from data_handler import DataHandler
from logging_module import system_logger
from human_oversight import oversight_manager

app = Flask(__name__)

# NON-COMPLIANCE: No API key required, anyone can access
# NON-COMPLIANCE: No rate limiting - vulnerable to abuse

evaluator = CandidateEvaluator()
data_handler = DataHandler()

@app.route('/api/evaluate', methods=['POST'])
def evaluate_candidate():
    """Evaluate a candidate

    NON-COMPLIANCE: No input validation
    NON-COMPLIANCE: No authentication required
    NON-COMPLIANCE: No audit logging of API access
    """
    try:
        # NON-COMPLIANCE: No input sanitization
        data = request.get_json()

        candidate_id = data.get('candidate_id', 'unknown')
        resume_text = data.get('resume_text', '')

        # Extract features - can crash on malformed input
        features = data_handler.preprocess_resume(resume_text)

        # Get prediction
        prediction = evaluator.evaluate_candidate(features)

        # Check if human review required
        needs_review = oversight_manager.requires_human_review(prediction)

        # NON-COMPLIANCE: Decision logged but incompletely
        system_logger.log_decision(candidate_id, features, prediction)

        response = {
            "candidate_id": candidate_id,
            "score": prediction['score'],
            "recommendation": prediction['recommendation'],
            "confidence": prediction['confidence'],
            "requires_human_review": needs_review,
            # Missing: explanation, uncertainty quantification
        }

        return jsonify(response), 200

    except Exception as e:
        # NON-COMPLIANCE: Poor error handling, may leak sensitive info
        return jsonify({"error": str(e)}), 500

@app.route('/api/override', methods=['POST'])
def override_decision():
    """Allow human to override AI decision

    NON-COMPLIANCE: No authorization check - anyone can override!
    """
    try:
        data = request.get_json()

        candidate_id = data['candidate_id']
        new_decision = data['new_decision']
        justification = data.get('justification', '')

        result = oversight_manager.override_ai_decision(
            candidate_id, new_decision, justification
        )

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """Get system performance metrics

    NON-COMPLIANCE: Returns claimed metrics, not actual measurements
    """
    # Returns hardcoded metrics, not real performance data
    metrics = evaluator.get_accuracy_metrics()
    oversight_stats = oversight_manager.get_oversight_statistics()

    return jsonify({
        "accuracy_metrics": metrics,
        "oversight_statistics": oversight_stats,
        # Missing: bias metrics, fairness metrics, real-time performance
    }), 200

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

@app.route('/api/admin/disable_logging', methods=['POST'])
def disable_logging():
    """Disable logging for performance

    NON-COMPLIANCE: Should never be possible to disable logging!
    """
    # Critical compliance violation: logging can be disabled
    config.ENABLE_LOGGING = False
    return jsonify({"message": "Logging disabled"}), 200

@app.route('/api/admin/disable_oversight', methods=['POST'])
def disable_oversight():
    """Disable human oversight

    NON-COMPLIANCE: Should never be possible to disable oversight!
    """
    # Critical compliance violation: human oversight can be disabled
    oversight_manager.disable_oversight()
    return jsonify({"message": "Human oversight disabled"}), 200

def run_api():
    """Run the API server

    NON-COMPLIANCE: Runs without HTTPS
    NON-COMPLIANCE: No security headers
    """
    # Running on HTTP not HTTPS - security issue
    app.run(host=config.API_HOST, port=config.API_PORT, debug=True)

if __name__ == '__main__':
    run_api()
