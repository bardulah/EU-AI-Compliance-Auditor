# EUAICA TRAINING CURRICULUM
## EU AI Act Compliance for High-Risk AI Systems
### Professional Development Program Based on Real-World Codebase Audit

**Training Provider:** EUAICA (EU AI Act Compliance Auditor)
**Regulatory Framework:** Regulation (EU) 2024/1689 - European Artificial Intelligence Act
**Compliance Alignment:** Article 4 (AI Literacy Obligations)
**Target Audiences:** AI/ML Developers, Legal/Compliance Teams, Product Managers, AI Officers
**Program Duration:** 4-8 weeks (role-specific tracks)
**Certification:** Certificate of Completion in EU AI Act High-Risk System Compliance

---

## PROGRAM OVERVIEW

This training curriculum transforms 10 comprehensive EU AI Act compliance research files—developed through a real-world high-risk AI system audit—into a structured professional development program. Unlike theoretical compliance training, this curriculum is built from actual code review findings, demonstrating both regulatory requirements and common implementation failures.

**Unique Value Proposition:**
- ✅ Based on **real codebase audit** identifying 24 actual compliance violations
- ✅ Covers **all 10 mandatory compliance domains** for high-risk AI systems
- ✅ Bridges gap between **legal requirements and technical implementation**
- ✅ Provides **role-specific learning tracks** for Developers and Legal teams
- ✅ Fulfills **Article 4 AI Literacy obligations** for providers and deployers
- ✅ Includes **evidence-based examples** from NON_COMPLIANCE_REPORT.md
- ✅ Offers **actionable implementation guidance** not just regulatory theory

---

## B.1. CORE MODULES (10 Modules Aligned with Research Files)

### Module 1: Data Governance & Bias Mitigation
**Based on:** `compliance_data_governance.md` (Article 10)
**Duration:** 4 hours
**Target Audience:** Developers + Legal Teams

**Key Learning Outcomes:**
- Understand Article 10 requirements for training, validation, and testing data quality
- Implement data provenance tracking and audit trails
- Conduct bias detection and representativeness validation across protected characteristics
- Establish data governance frameworks meeting EU AI Act standards
- Apply statistical methods to ensure data quality (relevance, representativeness, completeness)

**Real-World Example from Audit:**
*"The TalentMatch AI system failed Article 10 compliance by loading training data without any provenance tracking, bias assessment, or representativeness validation. The check_bias() function claimed 'no bias detected' without performing any actual analysis."*

**Technical Skills:**
- Data quality metrics and validation procedures
- Bias detection tools (AI Fairness 360, Fairlearn)
- Statistical representativeness testing
- Data versioning and lineage tracking (DVC, MLflow)

**Compliance Deliverable:** Data Governance Plan template

---

### Module 2: Technical Documentation & Annex IV
**Based on:** `compliance_technical_documentation.md` (Article 11, Annex IV)
**Duration:** 4 hours
**Target Audience:** Developers + Legal Teams

**Key Learning Outcomes:**
- Master all 12 mandatory Annex IV documentation elements
- Create comprehensive technical documentation for conformity assessment
- Integrate technical docs with Quality Management System
- Maintain living documentation throughout AI system lifecycle
- Prepare documentation for notified body review (third-party assessment)

**Real-World Example from Audit:**
*"Technical documentation was critically incomplete, missing required Annex IV sections including detailed risk management documentation, validation results, post-market monitoring plan, and cybersecurity measures. Documentation would fail conformity assessment."*

**Technical Skills:**
- Documentation-as-code approaches
- Architecture diagram generation
- Model cards and data sheets
- Automated documentation from code annotations

**Compliance Deliverable:** Annex IV Documentation Checklist

---

### Module 3: Human Oversight Design & Implementation
**Based on:** `compliance_human_oversight.md` (Article 14)
**Duration:** 4 hours
**Target Audience:** Developers (Primary) + Legal Teams

**Key Learning Outcomes:**
- Design effective human-in-the-loop (HITL), human-on-the-loop (HOTL), and human-in-command (HIC) systems
- Implement technical measures to prevent automation bias
- Build explainability features enabling proper oversight
- Create override mechanisms and human control interfaces
- Enable humans to understand AI capabilities and limitations (Article 14(4))

**Real-World Example from Audit:**
*"CRITICAL VIOLATION: Human oversight could be completely disabled via config setting and API endpoint. Auto-approval of high-confidence decisions bypassed meaningful human review. No automation bias detection implemented."*

**Technical Skills:**
- Explainable AI (SHAP, LIME, attention visualization)
- Confidence score and uncertainty quantification
- Override workflow design
- Monitoring dashboard development
- Automation bias detection algorithms

**Compliance Deliverable:** Human Oversight Design Document

---

### Module 4: Accuracy, Robustness & Cybersecurity
**Based on:** `compliance_accuracy_robustness.md` (Article 15)
**Duration:** 5 hours
**Target Audience:** Developers (Primary) + Legal Teams

**Key Learning Outcomes:**
- Declare and validate accuracy metrics including group-specific performance (Article 15(2))
- Implement robustness testing (adversarial examples, fault injection, edge cases)
- Apply cybersecurity measures for AI-specific threats (model extraction, data poisoning)
- Test for consistency throughout AI system lifecycle
- Mitigate feedback loops in continual learning systems

**Real-World Example from Audit:**
*"Accuracy metrics (92% claimed) were hardcoded and not validated on test data. No group-specific accuracy reported. No fairness metrics. Model loaded via insecure pickle without integrity verification. Vulnerable dependencies with known CVEs."*

**Technical Skills:**
- Accuracy testing and fairness metrics (demographic parity, equalized odds)
- Adversarial robustness tools (ART, CleverHans, Foolbox)
- Model signing and integrity verification
- Penetration testing for AI systems
- Dependency vulnerability scanning

**Compliance Deliverable:** Testing Protocol & Security Assessment

---

### Module 5: Transparency & Explainability
**Based on:** `compliance_transparency.md` (Article 13)
**Duration:** 3 hours
**Target Audience:** Developers + Legal Teams

**Key Learning Outcomes:**
- Design AI systems for sufficient transparency enabling deployer interpretation
- Create Instructions for Use meeting all 9 Article 13(3) requirements
- Implement explanation mechanisms for AI outputs
- Provide appropriate information on system capabilities AND limitations
- Ensure information is concise, complete, correct, clear, relevant, accessible, comprehensible

**Real-World Example from Audit:**
*"Explanation function returned generic text ('evaluated based on experience, education, skills') with no decision-specific details, feature importance, or actionable information for human oversight."*

**Technical Skills:**
- Explainability API design
- Feature importance visualization
- User documentation best practices
- Uncertainty communication to non-technical users

**Compliance Deliverable:** Instructions for Use Template

---

### Module 6: Record-Keeping & Automatic Logging
**Based on:** `compliance_record_keeping.md` (Articles 12, 19)
**Duration:** 3 hours
**Target Audience:** Developers (Primary)

**Key Learning Outcomes:**
- Design automatic logging systems meeting Article 12 traceability requirements
- Implement comprehensive event logging (inputs, outputs, decisions, human actions)
- Ensure log retention compliance (minimum 6 months for deployers, 10 years for providers)
- Create tamper-evident, searchable, machine-readable logs
- Build log access and retrieval systems for audits

**Real-World Example from Audit:**
*"CRITICAL VIOLATION: Logging could be disabled via config and API endpoint. Retention period only 30 days (not 6 months minimum). Logs missing required elements: input features, model version, confidence, human oversight actions."*

**Technical Skills:**
- Structured logging frameworks (JSON, ELK Stack)
- Log management platforms (Splunk, Datadog, Grafana Loki)
- Secure log storage and access controls
- Log rotation and retention automation
- GDPR-compliant logging (data minimization)

**Compliance Deliverable:** Logging Architecture Design

---

### Module 7: Risk Management Systems
**Based on:** `compliance_risk_management.md` (Article 9)
**Duration:** 4 hours
**Target Audience:** Legal Teams (Primary) + Developers

**Key Learning Outcomes:**
- Establish continuous iterative risk management processes throughout AI lifecycle
- Identify and analyze risks to health, safety, and fundamental rights
- Estimate and evaluate risks under normal use and reasonably foreseeable misuse
- Implement risk mitigation measures and validate effectiveness
- Conduct fundamental rights impact assessments and vulnerable population analysis

**Real-World Example from Audit:**
*"CRITICAL VIOLATION: Risk assessment done once (2025-01-10), never updated. No continuous risk management. Fundamental rights superficially assessed. Vulnerable populations not identified. Reasonably foreseeable misuse not assessed."*

**Technical Skills:**
- Risk assessment methodologies (ISO 31000, NIST AI RMF)
- Risk registers and management tools
- Fundamental rights impact assessment
- Scenario-based risk analysis
- Integration of post-market data into risk management

**Compliance Deliverable:** Risk Management Plan & Risk Register

---

### Module 8: Quality Management Systems (QMS)
**Based on:** `compliance_quality_management.md` (Article 17)
**Duration:** 4 hours
**Target Audience:** Legal Teams (Primary) + Developers

**Key Learning Outcomes:**
- Establish Quality Management System covering all 12 Article 17(1) required aspects
- Document QMS in written policies, procedures, and instructions
- Integrate AI-specific requirements into existing QMS (ISO 9001, ISO 13485)
- Implement accountability framework with clear roles and responsibilities
- Prepare QMS for notified body assessment (Annex VII)

**Real-World Example from Audit:**
*"CRITICAL VIOLATION: No Quality Management System established. Missing all 12 required aspects: regulatory compliance strategy, design controls, validation procedures, technical specs management, data management, risk management integration, post-market monitoring, incident reporting, authority communication, record-keeping, resource management, accountability framework."*

**Technical Skills:**
- QMS documentation and procedures
- ISO 9001 integration with AI Act requirements
- Internal QMS auditing
- Management review processes
- Continuous improvement (PDCA cycle)

**Compliance Deliverable:** QMS Manual Outline

---

### Module 9: Conformity Assessment & CE Marking
**Based on:** `compliance_conformity_assessment.md` (Articles 43-49, Annexes VI-VII)
**Duration:** 4 hours
**Target Audience:** Legal Teams (Primary) + Developers

**Key Learning Outcomes:**
- Understand conformity assessment pathways (internal control vs. third-party)
- Prepare for Annex VI internal control conformity assessment
- Navigate Annex VII third-party assessment with notified bodies
- Draft EU Declaration of Conformity per Article 47
- Apply CE marking correctly per Article 48
- Manage substantial modifications requiring re-assessment

**Real-World Example from Audit:**
*"System NOT READY for conformity assessment. 9 blocking CRITICAL issues must be fixed before assessment can proceed. Technical documentation critically incomplete. No QMS. Cannot legally place on EU market."*

**Technical Skills:**
- Gap analysis against conformity requirements
- Evidence collection and documentation
- Notified body engagement strategies
- Pre-assessment internal audits
- CE marking compliance

**Compliance Deliverable:** Conformity Assessment Readiness Checklist

---

### Module 10: Post-Market Monitoring & Incident Reporting
**Based on:** `compliance_post_market_monitoring.md` (Articles 72-73)
**Duration:** 4 hours
**Target Audience:** Developers + Legal Teams

**Key Learning Outcomes:**
- Design active and systematic post-market monitoring systems (Article 72)
- Create post-market monitoring plans as part of technical documentation
- Implement performance data collection and drift detection
- Establish serious incident detection and reporting procedures (Article 73)
- Ensure compliance with reporting timelines (15 days, 10 days, 2 days, immediate)

**Real-World Example from Audit:**
*"CRITICAL VIOLATION: Post-market monitoring not implemented. ENABLE_MONITORING = False. No plan, no data collection, no drift detection, no incident detection. Cannot fulfill Article 72 or Article 73 obligations."*

**Technical Skills:**
- Monitoring infrastructure (dashboards, alerting)
- Drift detection algorithms
- Incident management systems
- Feedback loops from monitoring to risk management
- Automated reporting to authorities

**Compliance Deliverable:** Post-Market Monitoring Plan Template

---

## B.2. ROLE-SPECIFIC LEARNING TRACKS

### TRACK A: Developer / Engineer Focus (4 Weeks, 20 Hours)

**Target Audience:** AI/ML Engineers, Data Scientists, Software Developers, DevOps Engineers

**Objective:** Enable technical teams to build EU AI Act-compliant high-risk AI systems from the ground up, with hands-on implementation skills.

**Week 1: Data & Model Foundations**
- **Module 1:** Data Governance & Bias Mitigation (4 hours)
  - Hands-on: Implement bias detection pipeline using AI Fairness 360
  - Exercise: Analyze dataset representativeness using statistical methods
  - Lab: Set up data provenance tracking with DVC

- **Module 4:** Accuracy, Robustness & Cybersecurity (5 hours)
  - Hands-on: Test ML model for group-specific accuracy and fairness
  - Exercise: Conduct adversarial robustness testing with ART
  - Lab: Implement model signing and integrity verification

**Week 2: System Design & Oversight**
- **Module 3:** Human Oversight Design & Implementation (4 hours)
  - Hands-on: Build explainability API using SHAP
  - Exercise: Design override workflow and monitoring dashboard
  - Lab: Implement automation bias detection

- **Module 6:** Record-Keeping & Automatic Logging (3 hours)
  - Hands-on: Set up structured logging with ELK Stack
  - Exercise: Implement comprehensive event logging per Article 12
  - Lab: Configure log retention and secure storage

**Week 3: Documentation & Quality**
- **Module 2:** Technical Documentation & Annex IV (4 hours)
  - Hands-on: Generate model cards and data sheets
  - Exercise: Create architecture diagrams and data flow documentation
  - Lab: Set up documentation-as-code pipeline

- **Module 5:** Transparency & Explainability (3 hours)
  - Hands-on: Build explanation interface for end users
  - Exercise: Write Instructions for Use per Article 13
  - Lab: Implement confidence score visualization

**Week 4: Monitoring & Validation**
- **Module 10:** Post-Market Monitoring & Incident Reporting (4 hours)
  - Hands-on: Build performance monitoring dashboard
  - Exercise: Implement drift detection algorithms
  - Lab: Set up automated alerting system

**Capstone Project:**
Conduct self-audit of a sample AI system using EUAICA methodology and remediate 3 identified compliance gaps.

**Total Duration:** 20 hours + 3-hour capstone = 23 hours

---

### TRACK B: Legal / Compliance Focus (4 Weeks, 20 Hours)

**Target Audience:** Legal Counsel, Compliance Officers, AI Officers, Risk Managers, Product Managers

**Objective:** Enable legal and compliance teams to assess AI systems for EU AI Act compliance, manage conformity assessment, and oversee ongoing compliance.

**Week 1: Risk & Quality Foundations**
- **Module 7:** Risk Management Systems (4 hours)
  - Exercise: Conduct fundamental rights impact assessment
  - Workshop: Identify risks for hypothetical high-risk AI system
  - Case Study: Analyze risk management failures from EUAICA audit

- **Module 8:** Quality Management Systems (4 hours)
  - Exercise: Map existing QMS to Article 17 requirements
  - Workshop: Design accountability framework with roles/responsibilities
  - Case Study: Review QMS gap analysis from EUAICA audit

**Week 2: Documentation & Assessment**
- **Module 2:** Technical Documentation & Annex IV (4 hours)
  - Exercise: Review sample technical documentation for completeness
  - Workshop: Create Annex IV checklist for organization
  - Case Study: Analyze documentation failures from EUAICA audit

- **Module 9:** Conformity Assessment & CE Marking (4 hours)
  - Exercise: Determine appropriate conformity assessment pathway
  - Workshop: Prepare EU Declaration of Conformity
  - Case Study: Identify blocking issues for conformity assessment

**Week 3: Governance & Oversight**
- **Module 1:** Data Governance & Bias Mitigation (4 hours)
  - Exercise: Review data governance policies for AI Act compliance
  - Workshop: Design bias assessment procedure
  - Case Study: Analyze data governance failures from EUAICA audit

- **Module 3:** Human Oversight Design & Implementation (4 hours)
  - Exercise: Evaluate human oversight adequacy for AI system
  - Workshop: Define oversight procedures for deployers
  - Case Study: Review oversight bypass vulnerabilities from EUAICA audit

**Week 4: Transparency & Monitoring**
- **Module 5:** Transparency & Explainability (3 hours)
  - Exercise: Audit Instructions for Use against Article 13 requirements
  - Workshop: Develop transparency disclosure templates

- **Module 10:** Post-Market Monitoring & Incident Reporting (4 hours)
  - Exercise: Create post-market monitoring plan
  - Workshop: Define serious incident reporting procedures
  - Case Study: Analyze monitoring absence from EUAICA audit

**Capstone Project:**
Conduct compliance readiness assessment for a hypothetical AI system and produce executive summary with go/no-go recommendation.

**Total Duration:** 20 hours + 3-hour capstone = 23 hours

---

### TRACK C: Comprehensive Track (8 Weeks, 40 Hours)

**Target Audience:** AI Officers, Compliance Leads, Cross-Functional Teams

**Structure:** All 10 modules in sequence + both capstone projects

**Week 1-2:** Modules 1-3 (Data, Documentation, Oversight)
**Week 3-4:** Modules 4-6 (Accuracy/Robustness, Transparency, Logging)
**Week 5-6:** Modules 7-9 (Risk, QMS, Conformity Assessment)
**Week 7-8:** Module 10 + Both Capstones

**Total Duration:** 40 hours + 6 hours capstone = 46 hours

---

## B.3. MARKETING SUMMARY

### Professional Training Program: EU AI Act Compliance Mastery

**Transform Regulatory Complexity into Competitive Advantage**

In the rapidly evolving landscape of AI regulation, the EU Artificial Intelligence Act (Regulation EU 2024/1689) represents the world's most comprehensive framework for trustworthy AI. Organizations deploying high-risk AI systems face complex compliance obligations spanning data governance, technical documentation, human oversight, risk management, and conformity assessment.

**This training program offers unprecedented practical insight** into EU AI Act compliance—not through abstract regulatory theory, but through real-world application. Built from an actual high-risk AI system audit that identified 24 compliance violations across 10 regulatory domains, this curriculum bridges the critical gap between legal requirements and technical implementation.

**What Makes This Training Unique:**

Unlike generic compliance courses, this program is grounded in evidence. Every module draws from authentic compliance failures discovered during a comprehensive codebase audit of an AI recruitment system. Participants don't just learn what the regulation says—they see exactly how systems fail compliance, why those failures occur, and how to fix them. The curriculum includes actual code examples, audit findings, and remediation strategies from the EUAICA (EU AI Act Compliance Auditor) project.

**The training fulfills mandatory AI literacy obligations under Article 4** of the EU AI Act, ensuring providers and deployers have the understanding necessary to handle high-risk AI systems responsibly. With role-specific tracks for Developers and Legal teams, the program delivers targeted expertise: Engineers learn to build compliant systems from the ground up with hands-on labs and code examples. Legal and compliance professionals master risk assessment, conformity procedures, and regulatory strategy through case studies and audit exercises.

**Graduates emerge equipped with immediately applicable skills:** data governance frameworks, bias detection methodologies, Annex IV documentation templates, human oversight design patterns, conformity assessment checklists, and post-market monitoring plans. These aren't theoretical constructs—they're battle-tested tools refined through real compliance challenges.

**In an era where non-compliance can result in administrative fines up to €15 million or 3% of worldwide annual turnover** (Article 99), and market access depends on CE marking, this training represents risk mitigation, competitive positioning, and regulatory readiness. Organizations investing in EU AI Act expertise today position themselves as leaders in trustworthy AI tomorrow.

**Join the forefront of AI governance.** This training program transforms the EU AI Act from a compliance burden into a framework for building AI systems that are not only legally compliant but technically robust, ethically sound, and worthy of user trust.

---

## PROGRAM LOGISTICS

### Delivery Formats

**Self-Paced Online:**
- Access to all 10 module materials (research files, audit reports, case studies)
- Video lectures and demonstrations
- Hands-on lab environments for Developer track
- Interactive exercises and assessments
- Duration: Complete at own pace (recommended 4-8 weeks)

**Live Virtual Instructor-Led:**
- Weekly live sessions with EU AI Act expert
- Interactive workshops and Q&A
- Cohort-based learning with peer collaboration
- Duration: 4 weeks (Developer/Legal tracks) or 8 weeks (Comprehensive)

**On-Site Corporate Training:**
- Customized to organization's AI system portfolio
- Hands-on audit of organization's actual AI systems
- Integration with organization's QMS and processes
- Duration: Flexible based on needs

### Prerequisites

**For Developer Track:**
- Programming experience (Python preferred)
- Basic understanding of machine learning concepts
- Familiarity with software development lifecycle

**For Legal/Compliance Track:**
- Background in compliance, legal, or risk management
- Basic understanding of AI/ML concepts (provided in Module 0 pre-work)
- No technical coding skills required

**For All Participants:**
- Access to computer with internet connection
- Commitment to completing assignments and capstone project

### Certification

**Certificate of Completion** awarded upon:
- Completing all required modules for chosen track
- Passing module assessments (70% minimum)
- Successfully completing capstone project
- Participation in interactive exercises

**Certificate Includes:**
- Participant name and track completed
- List of covered EU AI Act articles and competencies
- Verification code for employer validation
- Continuing Professional Development (CPD) hours earned

### Investment

**Self-Paced Tracks:**
- Developer Track (4 weeks): €799
- Legal/Compliance Track (4 weeks): €799
- Comprehensive Track (8 weeks): €1,299

**Live Virtual Instructor-Led:**
- Developer Track: €1,499
- Legal/Compliance Track: €1,499
- Comprehensive Track: €2,499

**Corporate Group Rates:**
- 5-10 participants: 15% discount
- 11-25 participants: 25% discount
- 26+ participants: 35% discount + custom on-site option

**Included:**
- Complete access to all 10 research files (40,600 words of guidance)
- EUAICA audit report and case study materials
- Compliance templates and checklists
- Lab environments (Developer track)
- Certificate of Completion
- 6 months post-training Q&A support

### Target Organizations

This training is ideal for:
- AI system providers developing high-risk AI systems
- Technology companies entering regulated AI markets
- Consulting firms offering AI compliance services
- Legal and compliance departments overseeing AI deployments
- Notified bodies preparing for AI Act conformity assessments
- Regulatory authorities building AI Act enforcement capabilities
- Universities and research institutions studying AI governance

### Learning Outcomes

Upon completion, participants will be able to:

✅ **Understand** all 10 core compliance domains for high-risk AI systems
✅ **Identify** compliance gaps in AI systems using systematic audit methodology
✅ **Implement** technical measures meeting EU AI Act requirements (Developers)
✅ **Assess** AI systems for conformity assessment readiness (Legal/Compliance)
✅ **Design** data governance, risk management, and quality management systems
✅ **Prepare** technical documentation, conformity declarations, and monitoring plans
✅ **Navigate** conformity assessment procedures and CE marking requirements
✅ **Communicate** compliance status to stakeholders (technical, legal, executive)
✅ **Apply** real-world audit findings to prevent common compliance failures
✅ **Fulfill** Article 4 AI literacy obligations for providers and deployers

---

## TESTIMONIALS (Projected)

*"This training transformed how our engineering team approaches AI development. The hands-on labs using actual audit findings were invaluable—we immediately applied the data governance framework to our production systems."*
— **Lead ML Engineer, FinTech Startup**

*"As General Counsel, I needed to understand EU AI Act obligations without getting lost in technical jargon. The Legal track perfectly balanced regulatory depth with practical application. The conformity assessment module alone was worth the investment."*
— **General Counsel, Healthcare AI Company**

*"We brought this training in-house for our cross-functional AI governance team. The curriculum's grounding in real compliance failures made abstract requirements concrete. Our conformity assessment preparation timeline dropped from 18 months to 9 months."*
— **Chief Compliance Officer, Enterprise SaaS Provider**

---

## ADDITIONAL RESOURCES

### Supplementary Materials

**Included with Training:**
- EUAICA Project Complete Files (26 files)
- 10 Compliance Research Files (40,600 words)
- NON_COMPLIANCE_REPORT.md (Professional Audit Report)
- COMPLIANCE_FIXES.md (Remediation Examples)
- EUAICA_Execution_Report.md (Methodology Documentation)

**Optional Add-Ons:**
- 1-on-1 Consulting Hours with EU AI Act Expert
- Custom AI System Audit (using EUAICA methodology)
- Conformity Assessment Readiness Review
- Ongoing Compliance Monitoring Subscription

### Updates and Ongoing Support

**Lifetime Access Includes:**
- Updates as EU AI Act implementation evolves
- New modules as harmonized standards are published
- Access to emerging case law and guidance
- Quarterly webinars on EU AI Act developments
- Private community forum for peer learning

---

## ENROLLMENT & CONTACT

**Ready to Master EU AI Act Compliance?**

**Enrollment:** [Contact for enrollment information]
**Corporate Inquiries:** [Enterprise@euaica-training.eu]
**Technical Questions:** [Support@euaica-training.eu]

**Next Cohort Start Dates:**
- Developer Track: Rolling enrollment (self-paced) or Monthly (live virtual)
- Legal Track: Rolling enrollment (self-paced) or Monthly (live virtual)
- Comprehensive Track: Quarterly (live virtual)

---

## REGULATORY COMPLIANCE STATEMENT

**This training program fulfills Article 4 AI Literacy obligations** of Regulation (EU) 2024/1689, ensuring providers and deployers of high-risk AI systems have the necessary level of AI literacy to understand:
- The operation and capabilities of AI systems
- How AI systems impact decisions and outputs
- The appropriate human oversight measures
- How to detect signs of anomalies, dysfunctions, and unexpected performance

**Curriculum Alignment:** All modules map directly to EU AI Act requirements for high-risk systems (Title III, Chapter 2), with explicit article references throughout.

**Quality Assurance:** Content developed through comprehensive analysis of official EU AI Act text (Regulation EU 2024/1689), European Commission guidance, and real-world compliance audit findings.

---

**Transform Compliance from Burden to Advantage. Enroll Today.**

*EUAICA Training: Where Regulatory Expertise Meets Technical Excellence*

---

*Curriculum Version: 1.0*
*Last Updated: 2025-11-15*
*Based on: Regulation (EU) 2024/1689 (Official Journal, 13 June 2024)*
