# EU AI Act Compliance Research: Conformity Assessment (Articles 43-49)

**Official Reference:** Regulation (EU) 2024/1689, Articles 43-49, Annexes VI-VII
**Compliance Domain:** Conformity Assessment Procedures and CE Marking
**Criticality Level:** CRITICAL - Required for Market Access

---

## 1. Executive Summary

Conformity assessment is the process by which providers demonstrate that their high-risk AI systems comply with EU AI Act requirements. After successful assessment, systems receive CE marking and can be legally placed on the EU market. The EU AI Act provides multiple conformity assessment pathways depending on system characteristics and standards used.

---

## 2. Core Legal Requirements

**Article 43(1):** "For high-risk AI systems listed in point 1 of Annex III (biometric identification and categorisation), where the systems are not placed on the market or put into service under the name or trademark of the provider, in addition to the conformity assessment based on the internal control set out in Annex VI, a third party conformity assessment applies."

**Article 43(2):** For high-risk AI systems referred to in points 2 to 8 of Annex III (other high-risk systems), providers shall follow the conformity assessment procedure based on **internal control** as referred to in Annex VI, which does not provide for the involvement of a notified body.

---

## 3. Conformity Assessment Pathways

### 3.1 Pathway Decision Tree

**Step 1: Identify system classification**
- Annex III, point 1 (biometric ID)? → May require third-party assessment
- Annex III, points 2-8 (other high-risk)? → Internal control pathway

**Step 2: For Annex III point 2-8 systems:**
- **Have you fully applied harmonized standards?**
  - YES → Internal control only (Annex VI)
  - NO or PARTIAL → Internal control only (Annex VI) [Note: For these systems, notified body involvement is optional]

**Step 3: For Annex III point 1 biometric systems:**
- Additional third-party assessment may apply depending on specifics

---

## 4. Internal Control Procedure (Annex VI)

**Annex VI: Conformity Based on Internal Control**

### 4.1 Provider Responsibilities

**The provider must:**

#### 4.1.1 Technical Documentation
- Draw up the technical documentation in accordance with Article 11 and Annex IV
- Ensure technical documentation demonstrates compliance with all requirements

#### 4.1.2 QMS Verification
- Verify that the established quality management system is in compliance with Article 17
- Ensure QMS covers all required aspects (a) through (l)

#### 4.1.3 Design and Development Verification
- Verify that the design and development process of the AI system, including the process for its development and, where applicable, its training, is consistent with the technical documentation

#### 4.1.4 Post-Market Monitoring Verification
- Verify that the post-market monitoring plan is consistent with the technical documentation

#### 4.1.5 Compliance Examination
- Examine the technical documentation in order to assess whether it demonstrates that the AI system complies with the requirements set out in Chapter III, Section 2

#### 4.1.6 Instructions for Use
- Verify that the system is accompanied by the instructions for use referred to in Article 13

### 4.2 Evidence Requirements for Internal Control

**Providers must be able to demonstrate:**
- ✅ Complete technical documentation per Annex IV
- ✅ Functioning QMS per Article 17
- ✅ Design/development process documented and followed
- ✅ Post-market monitoring plan in place
- ✅ All Chapter III Section 2 requirements met
- ✅ Instructions for use prepared

### 4.3 EU Declaration of Conformity (Article 47)

**After completing internal control, provider must:**
- Draft EU Declaration of Conformity per Article 47
- Declare sole responsibility for system compliance
- Identify system and conformity assessment procedure used
- List standards or specifications applied
- Sign declaration

### 4.4 CE Marking (Article 48)

**After declaration:**
- Affix CE marking to system (if physical product)
- Or include CE marking on packaging/documentation (if software)
- CE marking indicates compliance with EU AI Act

---

## 5. Third-Party Assessment (Annex VII)

**Annex VII: Conformity Based on Assessment of Quality Management System and Technical Documentation**

### 5.1 When Third-Party Assessment Applies

**Article 43(1):** Third-party (notified body) assessment may apply to:
- Certain biometric systems (Annex III point 1)
- Systems where provider chooses third-party route (even if not required)

### 5.2 Notified Body Selection

**Provider must:**
- Select a notified body from the list of EU-approved notified bodies for AI
- Notified body must be competent for the specific type of AI system

### 5.3 Assessment Process

#### Phase 1: Application
- Provider submits application to notified body
- Provides technical documentation and QMS documentation

#### Phase 2: QMS Assessment
**Notified body examines whether the QMS:**
- Complies with Article 17 requirements
- Ensures compliance of AI systems with applicable requirements
- Is effectively implemented

**Assessment includes:**
- Document review
- On-site audits
- Interviews with personnel
- Review of processes and records

#### Phase 3: Technical Documentation Assessment
**Notified body examines technical documentation to confirm:**
- All Annex IV elements present and complete
- Adequacy of design and development processes
- Appropriateness of training, validation, testing data (Article 10)
- Adequacy of risk management (Article 9)
- Compliance with accuracy, robustness, cybersecurity (Article 15)
- Adequacy of human oversight measures (Article 14)
- Transparency and information provision (Article 13)
- Appropriateness of record-keeping (Article 12)

#### Phase 4: Certificate Issuance
**If assessment successful:**
- Notified body issues **EU Technical Documentation Assessment Certificate**
- Certificate valid for 4 years
- May be renewed for additional 4-year periods

#### Phase 5: Surveillance
**Notified body conducts:**
- Regular surveillance audits during certificate validity
- Reviews of substantial modifications
- Verification of QMS ongoing compliance

### 5.4 EU Declaration of Conformity with Third-Party

**After receiving certificate:**
- Provider drafts EU Declaration of Conformity
- Declaration references notified body and certificate number
- CE marking affixed with notified body identification number

---

## 6. Harmonized Standards

### 6.1 Role of Harmonized Standards

**Harmonized standards provide a presumption of conformity:**
- If provider applies harmonized standards covering EU AI Act requirements
- Presumed to comply with those requirements
- Simplifies conformity assessment

### 6.2 Applying Standards

**Article 43(3) considerations:**
- **Full application:** Apply all relevant parts of harmonized standards
- **Partial application:** Apply only some parts, must justify and demonstrate compliance by other means
- **Non-application:** Don't use harmonized standards, must demonstrate compliance through alternative technical specifications

### 6.3 Current Status

**As of 2025:**
- Harmonized standards under EU AI Act are under development
- European standardization organizations (CEN, CENELEC, ETSI) working on standards
- Until harmonized standards published, providers must use alternative means

---

## 7. Substantial Modifications

### 7.1 Definition

**Article 3(23):** "Substantial modification" means a change to an AI system after its placing on the market or putting into service which:
- Is not foreseen or planned in the initial conformity assessment by the provider
- Affects the compliance of the AI system with the requirements set out in Chapter III, Section 2, or
- Results in a modification to the intended purpose for which the AI system has been assessed

### 7.2 Conformity Assessment for Modifications

**Article 43(4):** "High-risk AI systems that have already been subject to a conformity assessment procedure shall undergo a new conformity assessment procedure in the event of a substantial modification, regardless of whether the modified system is intended to be further distributed or continues to be used by the current deployer."

**Implication:**
- Substantial modification = new conformity assessment required
- Same pathway as original (internal control or third-party)
- New EU Declaration of Conformity
- Updated technical documentation

### 7.3 Managing Modifications

**Providers must:**
- Define what constitutes a substantial modification
- Implement change control processes (part of QMS)
- Assess each modification for substantiality
- Document modification impact assessments
- Conduct new conformity assessment if substantial
- Update technical documentation
- Notify deployers of modifications

---

## 8. EU Declaration of Conformity (Article 47)

### 8.1 Required Content

**Article 47(1):** The EU Declaration of Conformity shall state that the high-risk AI system in question complies with this Regulation. It shall contain the information set out in Annex V and shall be continuously updated.

**Annex V content:**
1. Provider's name and address
2. Authorized representative's name and address (if applicable)
3. Declaration that declaration issued under provider's sole responsibility
4. Identification of the AI system (name, type, version, etc.)
5. Statement that AI system complies with EU AI Act
6. References to relevant harmonized standards or other specifications used
7. Where applicable: notified body name, identification number, and certificate details
8. Place and date of issue
9. Name and function of person signing
10. Signature

### 8.2 Language and Accessibility

- Must be available in language(s) accepted by Member State where system placed on market
- Must accompany AI system
- Made available to authorities upon request

---

## 9. CE Marking (Article 48)

### 9.1 Affixing CE Marking

**Article 48(1):** "High-risk AI systems which are in conformity with this Regulation shall bear the CE marking in order to indicate their conformity with this Regulation, so that they can move freely within the internal market."

**Article 48(2):** "The CE marking shall be affixed visibly, legibly and indelibly to the high-risk AI system. Where that is not possible or not warranted on account of the nature of the high-risk AI system, it shall be affixed to the packaging or to the accompanying documentation, as appropriate."

### 9.2 CE Marking Rules

**Article 48(3):** "Where applicable, the CE marking shall be followed by the identification number of the notified body responsible for the conformity assessment procedures set out in Article 43."

**Article 48(4):** CE marking governed by Regulation (EC) No 765/2008 (general CE marking rules)

### 9.3 Prohibitions

**Article 48(5):** "The CE marking shall be the only marking indicating the conformity of the high-risk AI system with this Regulation."

**Article 48(6):** "High-risk AI systems shall not bear markings, signs or inscriptions which are likely to mislead third parties regarding the meaning or form of the CE marking."

---

## 10. Registration Obligations (Article 49)

### 10.1 EU Database Registration

**Article 49(1):** Before placing a high-risk AI system on the market or putting it into service, providers must register in the EU database referenced in Article 71.

**Information to register:**
- Provider details
- System identification
- Intended purpose
- Risk classification
- Conformity assessment procedure followed
- Declaration of conformity

---

## 11. Timelines and Validity

### 11.1 Certificate Validity (Third-Party Route)

- **Initial certificate:** Valid for 4 years from issuance
- **Renewal:** May be renewed for additional 4-year periods
- **Conditions:** QMS continues to comply; system not substantially modified

### 11.2 Conformity Assessment Duration

**Typical timelines:**
- **Internal control:** Weeks to months (depends on provider readiness)
- **Third-party assessment:** 3-12 months (depends on notified body capacity and system complexity)

---

## 12. Common Non-Compliance Patterns

### 12.1 Critical Failures

❌ **No conformity assessment conducted**
- System placed on market without assessment

❌ **Incomplete assessment**
- Not all requirements verified
- Missing technical documentation elements

❌ **Wrong pathway**
- Used internal control when third-party required (for certain biometric systems)

❌ **No CE marking**
- System compliant but CE marking not affixed

❌ **Invalid EU Declaration**
- Declaration incomplete or inaccurate

❌ **Not registered in EU database**
- Failed to register before market placement

### 12.2 Minor Deficiencies

⚠️ **Insufficient evidence**
- Claims of compliance not fully substantiated

⚠️ **Documentation gaps**
- Technical documentation incomplete

⚠️ **Process deviations**
- QMS or processes not consistently followed

---

## 13. Best Practices

### 13.1 Preparation

1. **Start early:** Conformity assessment takes time
2. **Gap analysis:** Identify compliance gaps early
3. **Documentation discipline:** Maintain comprehensive technical documentation from the start
4. **Internal pre-assessment:** Conduct internal audit before formal assessment

### 13.2 Notified Body Engagement

1. **Early consultation:** Engage notified body early for guidance
2. **Transparency:** Be open about challenges and gaps
3. **Responsiveness:** Respond promptly to notified body requests
4. **Maintain relationship:** Ongoing collaboration for surveillance

### 13.3 Modification Management

1. **Change control:** Robust change management process
2. **Substantiality assessment:** Evaluate every change for impact
3. **Version control:** Clear versioning and traceability
4. **Proactive re-assessment:** Don't delay re-assessment when needed

---

## 14. Verification Checklist

### 14.1 Pre-Assessment Readiness

✅ Technical documentation complete per Annex IV
✅ QMS established and documented per Article 17
✅ All Chapter III Section 2 requirements met
✅ Instructions for use prepared
✅ Post-market monitoring plan in place
✅ Risk management system operational
✅ Testing and validation completed

### 14.2 Assessment Execution

✅ Appropriate conformity assessment pathway selected
✅ If internal control: all Annex VI steps completed
✅ If third-party: notified body selected and engaged
✅ All required evidence provided
✅ Deficiencies addressed

### 14.3 Post-Assessment

✅ EU Declaration of Conformity drafted and signed
✅ CE marking affixed appropriately
✅ System registered in EU database
✅ Technical documentation retained (10 years)
✅ QMS maintained
✅ Surveillance audits passed (if third-party route)

---

## 15. Penalties and Consequences

**Administrative Fines (Article 99):**
- Up to €15,000,000 or 3% of worldwide annual turnover for placing non-compliant systems on market

**Market Consequences:**
- Non-compliant systems cannot be legally marketed in EU
- Market surveillance authorities can order withdrawal
- Reputational damage

---

## 16. Key Takeaways

1. **Conformity assessment is mandatory** - no exceptions for high-risk systems
2. **Multiple pathways exist** - internal control vs. third-party depending on system type
3. **CE marking is the goal** - enables legal market placement
4. **Documentation is critical** - complete technical documentation essential for success
5. **Substantial modifications require re-assessment** - manage changes carefully
6. **Registration required** - must register in EU database before market placement

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Compliance Status:** Official EU AI Act Requirements
