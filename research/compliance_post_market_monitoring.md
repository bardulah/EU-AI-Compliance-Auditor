# EU AI Act Compliance Research: Post-Market Monitoring (Article 72-73)

**Official Reference:** Regulation (EU) 2024/1689, Articles 72-73
**Compliance Domain:** Post-Market Monitoring and Serious Incident Reporting
**Criticality Level:** CRITICAL - Ongoing Compliance Obligation

---

## 1. Executive Summary

Post-market monitoring is a continuous obligation for providers of high-risk AI systems. Providers must actively collect and analyze data on system performance throughout its lifetime, ensuring ongoing compliance and detecting issues that may emerge in real-world deployment. When serious incidents occur, providers must report them to authorities within strict timelines.

---

## 2. Core Legal Requirements

### 2.1 Post-Market Monitoring System (Article 72)

**Article 72(1):** "Providers shall establish and document a post-market monitoring system in a manner that is **proportionate to the nature of the AI technologies and the risks** of the high-risk AI system."

**Article 72(2):** "The post-market monitoring system shall **actively and systematically collect, document and analyse relevant data** which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems **throughout their lifetime**, and where relevant, on the basis of its intended purpose, allow the provider to evaluate the continuous compliance of the AI systems with the requirements set out in Chapter III, Section 2."

**Key Principles:**
- **Active and systematic:** Not passive or ad-hoc
- **Throughout lifetime:** Continuous, not one-time
- **Evaluate compliance:** Verify ongoing conformity with requirements
- **Proportionate:** Scaled to risk level

---

## 3. Post-Market Monitoring Plan (Article 72(3))

### 3.1 Plan Requirement

**Article 72(3):** "The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026."

**Current Status:**
- Template not yet published (expected by February 2026)
- Providers should develop plans based on Article 72 requirements now

### 3.2 Expected Plan Elements

**Based on Article 72 and similar regulations, plan should include:**

1. **Objectives:**
   - Performance monitoring
   - Compliance verification
   - Risk detection
   - Trend analysis

2. **Data Collection Methods:**
   - Automated logging and telemetry
   - Deployer feedback and reports
   - User complaints and inquiries
   - External sources (publications, social media, news)

3. **Performance Metrics:**
   - Accuracy metrics
   - Robustness indicators
   - Safety metrics
   - Fundamental rights impact indicators

4. **Data Analysis Procedures:**
   - Statistical analysis methods
   - Trend detection algorithms
   - Anomaly detection
   - Root cause analysis

5. **Reporting and Escalation:**
   - Internal reporting cadence
   - Escalation triggers
   - Incident reporting procedures
   - Authority notification procedures

6. **Corrective Actions:**
   - Procedures for addressing issues
   - Update and patching processes
   - Recall or withdrawal procedures if necessary

7. **Resources:**
   - Personnel assigned
   - Tools and infrastructure
   - Budget allocation

8. **Review and Update:**
   - Plan review frequency
   - Update triggers

---

## 4. Data Collection Requirements

### 4.1 Types of Data to Collect

**Article 72(2) refers to "relevant data" which should include:**

#### Performance Data
- Actual accuracy in deployment
- False positive/negative rates
- Precision, recall, F1 scores
- Response times and latency
- System availability and uptime
- Throughput and capacity utilization

#### Safety Data
- Errors and failures
- Near-miss incidents
- Actual incidents causing harm
- Safety mechanism activations

#### User Interaction Data
- Human override frequency and reasons
- User complaints and feedback
- Usage patterns (within vs. outside intended purpose)
- User satisfaction surveys

#### Fundamental Rights Impact Data
- Discrimination or bias incidents
- Privacy breaches or concerns
- Adverse impacts on vulnerable populations
- Fundamental rights complaints

#### Environmental and Contextual Data
- Deployment environments
- Use contexts (geography, demographics, settings)
- Integration with other systems
- Changes in operating conditions

### 4.2 Data Sources

**Sources include:**
- **Automated logging:** System logs per Article 12/19
- **Deployer reports:** Feedback from deployers
- **User reports:** Complaints and inquiries
- **Market surveillance:** Data from authorities
- **Scientific literature:** Research on AI system performance
- **Media and social media:** Public discussions and incidents
- **Legal actions:** Lawsuits or regulatory proceedings

---

## 5. Data Analysis and Evaluation

### 5.1 Analysis Objectives

**Providers must analyze data to:**

1. **Verify Ongoing Compliance:**
   - Does system still meet accuracy requirements (Article 15)?
   - Is robustness maintained?
   - Are cybersecurity measures effective?
   - Is human oversight functioning properly?

2. **Detect Performance Degradation:**
   - Accuracy drift over time
   - Increasing error rates
   - Changing user behavior patterns

3. **Identify New Risks:**
   - Risks not identified during development
   - Emerging risks from new use contexts
   - Changing threat landscape (cybersecurity)

4. **Assess Real-World Impact:**
   - Are intended benefits realized?
   - Are there unintended adverse impacts?
   - Disproportionate impacts on specific groups?

### 5.2 Analysis Frequency

**Continuous vs. Periodic:**
- **Real-time monitoring:** Critical metrics monitored continuously
- **Regular analysis:** Statistical analysis at defined intervals (e.g., monthly, quarterly)
- **Triggered analysis:** In-depth investigation when anomalies detected

**Proportionality:** Higher-risk systems require more frequent analysis.

---

## 6. Feedback Loop to Development and Risk Management

**Article 72 integration with other requirements:**

### 6.1 Risk Management (Article 9(2)(c))

**Article 9(2)(c) requires:** "Evaluation of other possibly arising risks based on the analysis of data gathered from the post-market monitoring system referred to in Article 72."

**Feedback mechanism:**
- Post-market data identifies new risks
- Risk register updated
- Risk mitigation measures implemented
- System may require updates or modifications

### 6.2 System Updates

**When post-market monitoring reveals issues:**
- Software updates and patches
- Model retraining with new data
- Configuration changes
- Improved human oversight measures

**Substantial modifications:**
- If changes substantial, new conformity assessment required (Article 43(4))

---

## 7. Serious Incident Reporting (Article 73)

### 7.1 Definition of Serious Incident

**Article 3(49):** "'Serious incident' means an incident or malfunctioning of an AI system that directly or indirectly leads to any of the following:
a) the death of a person or serious harm to a person's health;
b) a serious and irreversible disruption of the management or operation of critical infrastructure;
c) the infringement of obligations under Union law intended to protect fundamental rights;
d) serious harm to property or the environment."

**Examples:**
- Medical AI system misdiagnosis leading to patient death
- Biometric identification system wrongly identifying person, leading to false arrest (fundamental rights)
- AI-controlled infrastructure system causing power grid failure
- AI system causing significant environmental damage

### 7.2 Reporting Obligations (Article 73(1))

**Article 73(1):** "Providers of high-risk AI systems placed on the Union market shall report any serious incident to the market surveillance authorities of the Member States where that incident occurred."

**What to report:**
- Incident description
- System involved (identification)
- Time and location
- Nature of harm or damage
- Affected persons or property
- Preliminary root cause analysis
- Corrective actions taken or planned

### 7.3 Reporting Timelines

**Article 73 does not specify exact timelines in all cases, but based on comparable regulations:**

**General principle (Article 73(1)):** Report "without undue delay, and in any event immediately after the provider has established a causal link between the AI system and the incident or malfunctioning, or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider becomes aware of the serious incident."

**More urgent incidents may require faster reporting:**
- Death or imminent threat to life: Immediate (hours, not days)
- Serious harm: Within days
- Less urgent serious incidents: Within 15 days

**For widespread infringements (Article 73(2)):**
- **10 days** after becoming aware, or immediately if death involved
- **2 days** for certain serious incidents specified by implementing acts

### 7.4 Multi-Jurisdictional Incidents

**Article 73(4):** "Where a serious incident has occurred which is related to an AI system and which has impacted or may impact more than one Member State, the provider shall inform the market surveillance authorities of all Member States concerned."

**Implication:**
- Providers must track where systems deployed
- Report to each affected Member State
- Coordinate with multiple authorities

### 7.5 Investigation and Follow-Up (Article 73(3))

**Article 73(3):** "Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned, including a risk assessment of the incident, and corrective action."

**Required actions:**
- Root cause analysis
- Risk assessment of incident
- Corrective actions (immediate and long-term)
- Preventive actions to avoid recurrence
- Follow-up reporting to authorities

### 7.6 Deployer Reporting to Provider

**Article 26(9):** Deployers must inform providers of any serious incident.

**Mechanism:**
- Deployers often first to detect incidents
- Must report to provider
- Provider then reports to authorities

---

## 8. Record-Keeping

**Providers must maintain records of:**
- Post-market monitoring plan
- Data collected
- Analysis performed
- Reports generated
- Incidents detected (serious and non-serious)
- Corrective actions taken
- Communications with deployers and authorities

**Retention:** Aligned with technical documentation retention (10 years recommended).

---

## 9. Integration with Quality Management System

**Article 17(1)(g) and (h):**
- Post-market monitoring system is part of QMS
- Incident reporting procedures are part of QMS

**QMS ensures:**
- Post-market monitoring plan implemented
- Data collection systematic and comprehensive
- Analysis procedures followed
- Incidents properly managed
- Continuous improvement based on monitoring

---

## 10. Common Non-Compliance Patterns

### 10.1 Critical Failures

❌ **No post-market monitoring**
- No monitoring system established
- No data collection after deployment

❌ **Passive monitoring only**
- Waiting for complaints; not actively collecting data

❌ **No plan**
- Ad-hoc monitoring without documented plan

❌ **Failure to report serious incidents**
- Serious incident occurs but not reported
- Reported late (beyond timelines)

❌ **No corrective actions**
- Issues identified but no action taken

### 10.2 Minor Deficiencies

⚠️ **Incomplete data collection**
- Some data sources monitored, others missed

⚠️ **Insufficient analysis**
- Data collected but not thoroughly analyzed

⚠️ **Delayed response**
- Slow to act on identified issues

---

## 11. Best Practices

### 11.1 Monitoring Infrastructure

**Implement robust infrastructure:**
- Automated telemetry and logging
- Centralized data aggregation (data lake or warehouse)
- Real-time dashboards for key metrics
- Automated alerting for anomalies
- Analytics tools for deep-dive analysis

### 11.2 Deployer Engagement

**Collaborate with deployers:**
- Provide easy reporting mechanisms (portals, APIs)
- Request regular performance reports
- Conduct periodic surveys
- Establish user communities for feedback

### 11.3 Proactive Monitoring

**Don't wait for problems:**
- Continuous monitoring of key metrics
- Statistical process control for anomaly detection
- Regular analysis even when no issues apparent
- Benchmarking against expected performance

### 11.4 Incident Management

**Prepare for incidents:**
- Incident response plan defined
- Roles and responsibilities clear
- Reporting templates prepared
- Authority contacts established
- Regular incident response drills

### 11.5 Continuous Improvement

**Use monitoring to improve:**
- Regular review of monitoring data in product meetings
- Feedback loop to R&D for next version improvements
- Share learnings across product portfolio
- Publish transparency reports (voluntary)

---

## 12. Tools and Technologies

**Monitoring Platforms:**
- Application Performance Monitoring (APM): Datadog, New Relic, Dynatrace
- ML Monitoring: Arize, Fiddler, WhyLabs, Evidently AI
- Log Management: ELK Stack, Splunk, Sumo Logic
- Analytics: Tableau, Power BI, Looker

**Data Infrastructure:**
- Data Lakes: AWS S3, Azure Data Lake, Google Cloud Storage
- Data Warehouses: Snowflake, BigQuery, Redshift
- Stream Processing: Apache Kafka, AWS Kinesis

---

## 13. Verification Checklist

### 13.1 Post-Market Monitoring System

✅ Post-market monitoring system established and documented
✅ Post-market monitoring plan created and part of technical documentation
✅ Data collection methods defined and implemented
✅ Data sources comprehensive (logs, deployer feedback, external sources)
✅ Performance metrics defined and tracked
✅ Analysis procedures documented and followed
✅ Continuous compliance evaluation conducted
✅ Feedback loop to risk management and development established
✅ Resources allocated (personnel, tools, budget)
✅ Plan reviewed and updated regularly

### 13.2 Serious Incident Reporting

✅ Serious incident definition understood by relevant personnel
✅ Incident detection mechanisms in place
✅ Reporting procedures documented
✅ Reporting timelines defined (15 days, 10 days, 2 days, immediate)
✅ Authority contacts established for all deployment jurisdictions
✅ Reporting templates prepared
✅ Investigation procedures defined
✅ Corrective action processes established
✅ Incident records maintained

---

## 14. Penalties and Consequences

**Administrative Fines (Article 99):**
- Up to €15,000,000 or 3% of worldwide annual turnover for violations of post-market monitoring and incident reporting

**Operational Consequences:**
- Undetected issues leading to harm
- Liability for damages from incidents
- Market surveillance enforcement actions
- Loss of customer trust
- Reputational damage

---

## 15. Key Takeaways

1. **Post-market monitoring is mandatory and continuous** - not optional or one-time
2. **Active, not passive** - providers must proactively collect and analyze data
3. **Plan required** - must have documented post-market monitoring plan
4. **Serious incidents must be reported** - strict timelines (15 days, 10 days, 2 days, or immediate)
5. **Feedback to risk management** - monitoring data feeds back into risk assessment
6. **Proportionate to risk** - higher-risk systems require more intensive monitoring
7. **Infrastructure investment needed** - proper tools and processes essential

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Compliance Status:** Official EU AI Act Requirements
