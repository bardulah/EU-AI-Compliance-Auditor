# EU AI Act Compliance Research: Data Governance and Data Management (Article 10)

**Official Reference:** Regulation (EU) 2024/1689, Article 10
**Compliance Domain:** Data and Data Governance for High-Risk AI Systems
**Criticality Level:** HIGH - Fundamental Requirement

---

## 1. Executive Summary

Article 10 of the EU AI Act establishes comprehensive requirements for training, validation, and testing data sets used in high-risk AI systems. This article is fundamental to ensuring AI systems are built on quality data that is relevant, representative, error-free, and complete. Non-compliance can result in biased outputs, discriminatory decisions, and fundamental rights violations.

---

## 2. Legal Requirements

### 2.1 Core Obligation

**Article 10(1):** "High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria specified in paragraphs 2 to 5."

### 2.2 Data Governance Practices

**Article 10(2):** Training, validation and testing data sets shall be subject to **data governance and management practices** appropriate for the intended purpose of the high-risk AI system. These practices concern:
- Data collection methodologies
- Data preparation and processing operations
- Formulation of relevant assumptions
- Prior assessment of availability, quantity, and suitability of datasets
- Examination of possible biases
- Identification of data gaps or shortcomings
- Measures to ensure data quality

### 2.3 Data Quality Standards

**Article 10(3):** Training, validation and testing data sets shall meet the following quality criteria:

#### Relevance
- Data must be relevant to the intended purpose of the high-risk AI system
- Must align with the specific use case and operational context

#### Representativeness
- Data must be sufficiently representative of the target population
- Must account for persons or groups of persons in relation to whom the system is intended to be used
- Must include appropriate statistical properties

#### Error-Free
- To the best extent possible, data sets must be free of errors and inconsistencies
- Error detection and correction mechanisms must be implemented

#### Completeness
- Data sets must be complete in view of the intended purpose
- Missing data must be addressed or justified

### 2.4 Contextual Requirements

**Article 10(4):** Data sets shall take into account, to the extent required by the intended purpose:
- Geographical characteristics or elements particular to the deployment region
- Contextual factors specific to the operational environment
- Behavioural patterns relevant to the user population
- Functional settings within which the system is intended to be used

### 2.5 Special Provisions for Non-Training Systems

**Article 10(5):** For high-risk AI systems that do NOT use techniques involving the training of AI models, the requirements in paragraphs 2 to 5 apply only to the **testing data sets**.

---

## 3. Technical Implementation Requirements

### 3.1 Data Collection and Sourcing

**Measurable Criteria:**
- Document data source provenance for 100% of training data
- Establish data collection protocols with version control
- Implement automated data quality checks at ingestion
- Maintain audit trails of all data acquisition activities

**Common Non-Compliance:**
- Using data from unverified sources
- Lack of documentation on data origins
- No audit trail for data changes

### 3.2 Bias Detection and Mitigation

**Technical Controls Required:**
- Statistical analysis to detect demographic biases
- Intersectional bias testing across protected characteristics
- Bias mitigation algorithms applied to training data
- Regular re-evaluation of bias metrics

**Measurable Criteria:**
- Documented bias assessment for all protected groups
- Quantified bias metrics (e.g., demographic parity, equalized odds)
- Mitigation strategies implemented with measurable improvements

**Common Gaps:**
- No formal bias testing procedures
- Bias testing limited to single protected characteristics
- No ongoing bias monitoring

### 3.3 Data Representativeness Validation

**Technical Requirements:**
- Statistical comparison of dataset demographics vs. target population
- Coverage analysis to identify underrepresented groups
- Stratified sampling to ensure adequate representation
- Documentation of representativeness metrics

**Measurable Criteria:**
- Minimum sample sizes per demographic group (statistically significant)
- Representation ratios aligned with target population (±10% tolerance recommended)
- Geographic coverage maps for location-dependent systems

### 3.4 Data Quality Assurance

**Required Processes:**
- Automated data validation pipelines
- Error detection algorithms (outliers, duplicates, inconsistencies)
- Data cleaning and preprocessing documentation
- Quality metrics tracking and reporting

**Measurable Criteria:**
- Error rates < 1% in production datasets
- 100% of data undergoes quality validation
- Documented quality improvement over time

---

## 4. Documentation Requirements

### 4.1 Data Governance Documentation

Providers must maintain comprehensive documentation covering:

1. **Data Collection Methodology**
   - Sources and acquisition methods
   - Collection timeframes and frequencies
   - Selection criteria and sampling strategies

2. **Data Processing Operations**
   - All preprocessing steps (cleaning, normalization, augmentation)
   - Feature engineering procedures
   - Data transformation pipelines

3. **Bias Assessment Reports**
   - Statistical analysis of bias across protected characteristics
   - Identified biases and their quantification
   - Mitigation measures implemented

4. **Representativeness Analysis**
   - Target population definitions
   - Statistical comparison of dataset vs. population
   - Justification for representation choices

5. **Quality Assurance Records**
   - Quality metrics and thresholds
   - Error detection results
   - Quality improvement actions

### 4.2 Data Assumptions Documentation

All assumptions made regarding data must be explicitly documented:
- Assumptions about data stationarity
- Assumed correlations and causal relationships
- Temporal validity assumptions
- Generalization assumptions

---

## 5. Verification and Compliance Criteria

### 5.1 Auditable Evidence

**For Conformity Assessment, the following evidence must be available:**

✅ **Data Provenance Records**
- Complete chain of custody for all datasets
- Source verification documentation

✅ **Quality Metrics Dashboard**
- Real-time quality monitoring
- Historical quality trends

✅ **Bias Testing Reports**
- Comprehensive bias analysis across demographics
- Mitigation effectiveness measurements

✅ **Representativeness Validation**
- Statistical proof of adequate representation
- Justification for sampling strategies

✅ **Data Governance Policies**
- Formal documented policies and procedures
- Roles and responsibilities for data management

### 5.2 Common Non-Compliance Patterns

❌ **Critical Deficiencies:**
1. No documented data governance framework
2. Missing bias assessment entirely
3. Unrepresentative datasets (skewed demographics)
4. No error tracking or quality metrics
5. Unknown data provenance

❌ **Minor Deficiencies:**
1. Incomplete bias testing (missing some protected characteristics)
2. Insufficient documentation of preprocessing steps
3. No version control for datasets
4. Limited quality metrics tracking

---

## 6. Best Practices for Implementation

### 6.1 Data Governance Framework

**Recommended Components:**
- Dedicated data governance committee
- Clear roles: Data Owner, Data Steward, Data Custodian
- Data quality scorecards with KPIs
- Automated data lineage tracking tools

### 6.2 Continuous Monitoring

**Implement ongoing processes:**
- Regular re-validation of data quality (quarterly minimum)
- Drift detection to identify changes in data distributions
- Automated alerts for quality threshold violations
- Periodic bias reassessment

### 6.3 Tools and Technologies

**Recommended Implementations:**
- Data validation frameworks (e.g., Great Expectations, TensorFlow Data Validation)
- Bias detection libraries (e.g., AI Fairness 360, Fairlearn)
- Data versioning systems (e.g., DVC, Pachyderm)
- Data cataloging and lineage tools (e.g., Apache Atlas, Amundsen)

---

## 7. Integration with Other Requirements

Article 10 data governance directly supports compliance with:
- **Article 9 (Risk Management):** Quality data reduces risks of biased/discriminatory outcomes
- **Article 11 (Technical Documentation):** Data documentation is part of Annex IV requirements
- **Article 15 (Accuracy & Robustness):** Data quality directly impacts system accuracy
- **Article 72 (Post-Market Monitoring):** Ongoing data quality monitoring is essential

---

## 8. Penalties for Non-Compliance

**Administrative Fines (Article 99):**
- Up to €15,000,000 or 3% of worldwide annual turnover (whichever is higher) for violations of Article 10 requirements

**Operational Consequences:**
- Inability to obtain CE marking
- Prohibition on market placement
- Mandatory product recalls
- Reputational damage

---

## 9. Key Takeaways for Software Implementation

**For Developers and Engineers:**

1. **Build data governance into your ML pipelines from day one**
   - Don't treat it as an afterthought or documentation exercise

2. **Automate quality and bias checks**
   - Manual processes don't scale and are error-prone

3. **Document everything**
   - Every data decision, assumption, and transformation must be traceable

4. **Test representativeness rigorously**
   - Use statistical methods to prove your data represents your user base

5. **Implement continuous monitoring**
   - Data quality and bias are not one-time checks

**Code-Level Indicators of Non-Compliance:**
- No data validation code in training pipelines
- Hardcoded data paths with no versioning
- No bias testing in test suites
- Missing data quality metrics in monitoring dashboards
- No logging of data preprocessing steps

---

## 10. References and Resources

- **Official Text:** Regulation (EU) 2024/1689 - Article 10
- **EU AI Act Portal:** https://artificialintelligenceact.eu/article/10/
- **European Commission AI Act Service Desk:** https://ai-act-service-desk.ec.europa.eu/
- **GDPR Alignment:** Data governance practices must also comply with GDPR where personal data is used

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Compliance Status:** Official EU AI Act Requirements (Enforceable 2026+)
