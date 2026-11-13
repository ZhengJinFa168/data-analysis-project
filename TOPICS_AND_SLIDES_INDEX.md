# Data Analysis Course — Complete Topics & Slides Index

This document indexes every topic, framework, mathematical formula, tool, architecture, and case study across all slide decks and project files in your workspace.

---

## 0. Workspace Folder Structure

```text
data analysis/
├── .gitignore                        # Excludes Slides/, .venv/, and OS/cache files
├── requirements.txt                  # Python dependencies
├── TOPICS_AND_SLIDES_INDEX.md        # Master course & project file/topic index
├── Slides/                           # Course lecture decks (gitignored)
│   ├── Session_01_CourseIntroduction.pdf
│   ├── Session_02_CRISP_DM_PDF.pdf
│   ├── Session 04 - Team Project_DA.pdf
│   ├── Session 05- BussinesCast-Part_1.pdf
│   ├── Session 05 - BussinesCast-Part_2.pdf
│   ├── Session_6_Data_Engineering-Part_1.pdf
│   ├── Sessions_07.Data_Engineering-Part_2.pdf
│   ├── Sessions_08.Healthcare.pdf
│   └── TheODen_Federated_Learning.pptx
├── project/                          # Initial dataset proposal
│   └── Dataset_Proposal_SPARCS.pdf
├── WP1/                              # Work Package 1 — Business Case & EDA
│   ├── download_sparcs.py
│   ├── WP1_Executive_EDA_and_Business_Case.ipynb
│   ├── WP1 – Early Discharge Planning Business Case.pptx
│   ├── SPARCS_Data_Extract_Scope_and_Rationale_WP1.pdf
│   ├── WP1_Analysis_and_Findings_Simple_Guide.docx
│   ├── data/                         # Downloaded SPARCS Parquet/CSV files (85 MB)
│   └── figures/                      # WP1 charts (PNG)
└── WP2/                              # Work Package 2 — Data Engineering Architecture
    ├── wp2_slide_0511.pdf
    ├── WP2_Master_Technical_Document.md
    ├── build_wp2_deck.py
    ├── WP2 – Data Engineering Architecture.pptx
    ├── WP2 – Data Engineering Architecture.pdf
    └── WP2_Presentation_Notes.md
```

---

## 1. Files Overview

### Course Lecture Slide Decks
| Session | File | Pages | Main Focus |
| :--- | :--- | :---: | :--- |
| **Session 01** | [Session_01_CourseIntroduction.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_01_CourseIntroduction.pdf) | 36 | Data Science Production Pipelines, Roles (DE/DS/DA), 7-Stage Data Value Chain, LLM Disruption, AWS Architecture, Course Syllabus & Grading |
| **Session 02** | [Session_02_CRISP_DM_PDF.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_02_CRISP_DM_PDF.pdf) | 51 | CRISP-DM Methodology (6 Phases) + Full Worked Case Study (€1M Action Banner Campaign for Premium Frying Pans) |
| **Session 04** | [Session 04 - Team Project_DA.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2004%20-%20Team%20Project_DA.pdf) | 15 | Team Project Guidelines, Dataset Selection, Work Packages (WP1–WP4), Executive Memo, Rubrics & Milestones |
| **Session 05 (Part 1)** | [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) | 78 | Company Data Systems (OLTP/OLAP, Star Schema, ERP, CRM), P&L & Unit Economics (CAC, LTV, Churn), Online Marketing & Attribution, Ecommerce (CDP, RFM, BG/NBD, Lookalikes, Recommenders) |
| **Session 05 (Part 2)** | [Session 05 - BussinesCast-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005%20-%20BussinesCast-Part_2.pdf) | 44 | Commercial/Operational/Financial KPIs + Sector Deep Dives: Banking (Credit Scoring PD/LGD/EAD), Media & VOD (Heartbeats, Churn/Uplift), Industrial Controlling (SCADA vs SAP, OEE, Variances), Logistics (TMS, ETA & Failed Delivery) |
| **Session 06** | [Session_6_Data_Engineering-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_6_Data_Engineering-Part_1.pdf) | 80 | Data Engineering Part 1: Running Case (ShopCo Black Friday), Distributed Storage/Compute, Cloud & AWS Serverless, Stage 1 Generate (DBs, APIs, Events), Stage 2 Ingest (Batch vs Stream, Kafka, Kinesis, NiFi, Airflow, Debezium CDC) |
| **Session 07** | [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) | 100 | Data Engineering Part 2: Stage 3 Store (S3, CSV/JSON/Avro/Parquet/ORC, Lakehouse/Iceberg, Medallion), Stage 4 Transform (Cleaning, Missing/Outliers, dbt Quality), Scalability (HDFS, MapReduce, Spark/PySpark), Stages 5–6 Persist & Exploit (PostgreSQL, Redis, MongoDB, Cassandra, Redshift, TimescaleDB, Elasticsearch, Vector DBs), Stage 8 End-to-End Streaming (Flink/Watermarks), Stage 9 Data Governance |
| **Session 08** | [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) | 83 (78 slides) | Healthcare Data Science & Engineering: Clinical Systems (HIS, EHR, LIS, RIS/PACS), HL7 v2 / FHIR / DICOM, 6 Clinical Modalities, Analytics Ladder (Descriptive to Prescriptive), Ontologies (SNOMED CT, ICD-10, LOINC, RxNorm, UMLS), Medical Embeddings & Knowledge Graphs, Clinical NLP & LLMs, Medical RAG (Document & RWE/OMOP), OMOP CDM & ELADAIS Federated Platform |
| **Federated Learning** | [TheODen_Federated_Learning.pptx](file:///Users/luigizheng/Desktop/data analysis/Slides/TheODen_Federated_Learning.pptx) | — | Federated Learning slides (`Slides/` — gitignored) |

### Team Project & WP1 Files
| Folder / File | Link | Description |
| :--- | :--- | :--- |
| **Dataset Proposal** | [Dataset_Proposal_SPARCS.pdf](file:///Users/luigizheng/Desktop/data analysis/project/Dataset_Proposal_SPARCS.pdf) | 1-page proposal for NY SPARCS Inpatient Discharges (Early Discharge Planning & Bed Capacity) |
| **WP1 Data Scope** | [SPARCS_Data_Extract_Scope_and_Rationale_WP1.pdf](file:///Users/luigizheng/Desktop/data analysis/WP1/SPARCS_Data_Extract_Scope_and_Rationale_WP1.pdf) | 10-page technical rationale for the SPARCS Socrata API extraction, year roles (2017/2018–19/2023), filtering funnel, and anti-leakage column rules |
| **WP1 Slide Deck** | [WP1 – Early Discharge Planning Business Case.pptx](file:///Users/luigizheng/Desktop/data analysis/WP1/WP1%20%E2%80%93%20Early%20Discharge%20Planning%20Business%20Case.pptx) | 10-slide board presentation for Finger Lakes Health System (\$17.5M net annual value) |
| **WP1 Notebook** | [WP1_Executive_EDA_and_Business_Case.ipynb](file:///Users/luigizheng/Desktop/data analysis/WP1/WP1_Executive_EDA_and_Business_Case.ipynb) | Jupyter Notebook reproducing all WP1 EDA statistics, baselines, financial ROI calculations, and charts |
| **WP1 Findings Guide** | [WP1_Analysis_and_Findings_Simple_Guide.docx](file:///Users/luigizheng/Desktop/data analysis/WP1/WP1_Analysis_and_Findings_Simple_Guide.docx) | Word document explaining the WP1 analysis and findings |
| **WP1 Ingestion Script** | [download_sparcs.py](file:///Users/luigizheng/Desktop/data analysis/WP1/download_sparcs.py) | Python script querying the NY State Health Data Socrata API and producing the WP1 Parquet/CSV datasets |

### WP2 Files (Data Engineering)
| Document | Link | Description |
| :--- | :--- | :--- |
| **WP2 Brief Slides** | [wp2_slide_0511.pdf](file:///Users/luigizheng/Desktop/data analysis/WP2/wp2_slide_0511.pdf) | Course assignment brief and CTO evaluation questions for WP2 |
| **WP2 Master Technical Doc** | [WP2_Master_Technical_Document.md](file:///Users/luigizheng/Desktop/data analysis/WP2/WP2_Master_Technical_Document.md) | Complete end-to-end technical specification with Fact/Assumption tags and rationales |
| **WP2 Slide Deck (PPTX)** | [WP2 – Data Engineering Architecture.pptx](file:///Users/luigizheng/Desktop/data analysis/WP2/WP2%20%E2%80%93%20Data%20Engineering%20Architecture.pptx) | Editable 10-slide presentation matching WP1 visual style, with embedded speaker notes |
| **WP2 Slide Deck (PDF)** | [WP2 – Data Engineering Architecture.pdf](file:///Users/luigizheng/Desktop/data analysis/WP2/WP2%20%E2%80%93%20Data%20Engineering%20Architecture.pdf) | Matching 10-slide PDF export |
| **WP2 Speaker Notes** | [WP2_Presentation_Notes.md](file:///Users/luigizheng/Desktop/data analysis/WP2/WP2_Presentation_Notes.md) | Concise speaker notes with core concepts, Slide 2 source provenance, and walk-in guides |
| **Deck Generator Script** | [build_wp2_deck.py](file:///Users/luigizheng/Desktop/data analysis/WP2/build_wp2_deck.py) | Python OpenXML + Matplotlib script generating the WP2 `.pptx` and `.pdf` |

---

## 2. Quick Topic Finder (Cross-Deck Thematic Index)

Use this section to quickly locate any topic across all lectures:

### A. Methodology, Lifecycle & Roles
- **7-Stage Data Value Chain (Generate → Ingest → Store → Transform → Persist → Exploit → Act)**:
  - [Session_01_CourseIntroduction.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_01_CourseIntroduction.pdf) — Slides 15–16, 18
  - [Session_02_CRISP_DM_PDF.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_02_CRISP_DM_PDF.pdf) — Slide 7
  - [Session_6_Data_Engineering-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_6_Data_Engineering-Part_1.pdf) — Slides 4–5
  - [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) — Slides 2, 97–98
- **Data Roles (Data Engineer vs Data Scientist vs Data Analyst)**:
  - [Session_01_CourseIntroduction.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_01_CourseIntroduction.pdf) — Slides 10–12 (Venn diagram & AI impact on seniority), Slides 17–21 (Roles comparison & responsibilities), Slide 23 (LLM disruption by role)
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slide 17
- **CRISP-DM (6 Phases, Checklists & Effort Split)**:
  - [Session_02_CRISP_DM_PDF.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_02_CRISP_DM_PDF.pdf) — Slides 3–19 (Theory & phase-by-phase breakdown), Slides 20–50 (Complete worked case study: €1M banner campaign)
- **Feature Engineering & Anti-Leakage Rules**:
  - [Session_02_CRISP_DM_PDF.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_02_CRISP_DM_PDF.pdf) — Slide 15 (Operations, SHAP/permutation selection, 4 golden rules), Slides 32–34 (ABT, RFM, time-window features, cut-off dates)
- **Families of Modelling Techniques (Supervised, Unsupervised, LLMs/Foundation Models)**:
  - [Session_01_CourseIntroduction.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_01_CourseIntroduction.pdf) — Slide 22
  - [Session_02_CRISP_DM_PDF.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_02_CRISP_DM_PDF.pdf) — Slide 17

### B. Business Case, P&L, KPIs & Unit Economics
- **P&L (Profit & Loss) Statement & Executive Levers**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slides 2–3 (7-step chain from P&L to impact), Slide 19 (P&L structure: Revenue, COGS, Gross Margin, OPEX, EBITDA, EBIT, Net Profit), Slide 20 (3 Executive Levers: Sell more, Spend less, Use less capital), Slide 21 (Use-case map by P&L line)
- **ROI, Break-Even Threshold, Decile & Lift Analysis**:
  - [Session_02_CRISP_DM_PDF.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_02_CRISP_DM_PDF.pdf) — Slide 22 ($p^* = \text{cost} / \text{margin}$), Slide 24 (ROI formula & common traps), Slides 39–42 (Decile table, cumulative profit curve, business levers)
- **CAC, LTV (CLTV), Payback, and Churn Math**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slides 22–23 (Unit economics & SQL queries), Slide 24 (Churn formulas: $\text{Expected Life} = 1/\text{churn}$, $\text{LTV} = \text{margin}/\text{churn}$), Slide 25 (Sector benchmarks for LTV/CAC)
- **Bridging Model Metrics (AUC, RMSE, NDCG) to Business Metrics (€)**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slide 26
- **KPIs (Leading vs Lagging, KPI Trees, SQL Formulas for Commercial, Operational & Financial KPIs)**:
  - [Session 05 - BussinesCast-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005%20-%20BussinesCast-Part_2.pdf) — Slides 3–7

### C. Enterprise Systems & Sector Business Cases
- **OLTP vs OLAP & Kimball Star Schema (`fact_sales`, `dim_*`, SCD Type 2)**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slides 6–8
  - [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) — Slides 48–54
- **ERP (SAP, Oracle, Odoo) & CRM (Salesforce, HubSpot) & Their 6 Integrations**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slides 10–15
- **Digital Marketing, Tag Manager (GTM/GA4), Ad Auctions & Multi-Touch Attribution (Last-Click, Shapley/Markov, MMM, Geo-Holdout)**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slides 29–56 (Value-based bidding pLTV on Slides 41–44; 4 Attribution methods compared on Slide 52)
- **Ecommerce: CDP, RFM Segmentation, BG/NBD + Gamma-Gamma vs LightGBM LTV, Uplift, Lookalikes, Two-Tower Recommender Systems**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slides 57–77
- **Banking: P&L (NIM, Cost of Risk), Core Banking vs Real-Time Fraud, Credit Scoring (`EL = PD × LGD × EAD`, WoE Scorecard, PSI)**:
  - [Session 05 - BussinesCast-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005%20-%20BussinesCast-Part_2.pdf) — Slides 8–16
- **Media & Video on Demand (Streaming): Hybrid P&L, Player Heartbeat Events, Subscriber RFM, Ad Yield, Churn & Uplift Modelling**:
  - [Session 05 - BussinesCast-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005%20-%20BussinesCast-Part_2.pdf) — Slides 17–27
- **Industrial Controlling: SCADA/PLC (OT) vs SAP (IT), MES, Standard Cost Stack, OEE, Weekly Price/Usage/Efficiency/Volume Variances**:
  - [Session 05 - BussinesCast-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005%20-%20BussinesCast-Part_2.pdf) — Slides 28–34
- **Logistics & 3PL: P&L, TMS 6-Step Workflow, WMS, Telematics, Quantile Regression ETA & Failed-Delivery Prediction**:
  - [Session 05 - BussinesCast-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005%20-%20BussinesCast-Part_2.pdf) — Slides 35–43

### D. Data Engineering, Cloud, Big Data & Databases
- **Cloud Computing & AWS Architecture (S3, Lambda, ECS/Fargate, Glue, EMR, SQS, SNS, Kinesis, MSK, Redshift, Lake Formation)**:
  - [Session_01_CourseIntroduction.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_01_CourseIntroduction.pdf) — Slides 7–8, 24–25
  - [Session_6_Data_Engineering-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_6_Data_Engineering-Part_1.pdf) — Slides 28–40
- **Data Generation & Extraction (Full Load vs Watermark Incremental vs CDC / Debezium WAL, REST API Pagination)**:
  - [Session_6_Data_Engineering-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_6_Data_Engineering-Part_1.pdf) — Slides 41–51, 76–78
- **Data Ingestion: Batch vs Streaming, Apache Kafka (Topics, Partitions, Consumer Groups, Compaction), Kinesis, Apache NiFi, Apache Airflow**:
  - [Session_6_Data_Engineering-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_6_Data_Engineering-Part_1.pdf) — Slides 52–79
- **Storage Formats (CSV, JSONL, Avro, Parquet, ORC), Row vs Columnar, Data Lake vs Warehouse vs Lakehouse (Apache Iceberg) & Medallion (Bronze/Silver/Gold)**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slide 5
  - [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) — Slides 3–19
- **Data Transformation, Curation (Deduplication, Missing Values, Outliers, String/JSON Normalisation), Identity Resolution & `dbt` Data Quality Tests**:
  - [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) — Slides 20–29
- **Distributed Storage & Compute: HDFS, MapReduce, Apache Spark / PySpark (Lazy Evaluation, Catalyst, Shuffles, Broadcast Joins, Skew)**:
  - [Session_6_Data_Engineering-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_6_Data_Engineering-Part_1.pdf) — Slides 23–27
  - [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) — Slides 30–47
- **Database Systems (PostgreSQL, Redis/DynamoDB, MongoDB, Cassandra/HBase, Redshift/Athena, TimescaleDB/InfluxDB, Elasticsearch, Vector DBs/HNSW & CAP Theorem)**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slide 9
  - [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) — Slides 48–80 (Master Comparison Table on Slide 76; Decision Flowchart on Slide 77)
- **End-to-End Streaming: Event Time vs Processing Time, Tumbling/Sliding/Session Windows, Watermarks, Delivery Guarantees (At-most/At-least/Exactly-once)**:
  - [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) — Slides 81–90
- **Data Governance: Data Catalogue, Data Lineage, Data Dictionary & Contracts, GDPR/PII Masking**:
  - [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf) — Slide 16
  - [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf) — Slides 91–96

### E. Healthcare Data Science, Clinical NLP & OMOP CDM
- **Hospital Data Systems (HIS, EHR, LIS, RIS/PACS, ICU) & Messaging Standards (HL7 v2, FHIR, DICOM)**:
  - [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) — PDF Pages 4–17, 26–27
- **6 Clinical Data Modalities (Structured EHR, Free Text, Imaging, Biosignals, Omics) & Multimodal Fusion**:
  - [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) — PDF Pages 18–25
- **Clinical Analytics Ladder (Descriptive, Diagnostic, Predictive, Causal / Target Trial Emulation, Prescriptive)**:
  - [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) — PDF Pages 28–39
- **Medical Terminologies & Ontologies (SNOMED CT, ICD-10, LOINC, RxNorm, ATC, UMLS Metathesaurus/CUIs)**:
  - [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) — PDF Pages 40–45
- **Medical Embeddings (ClinicalBERT, SapBERT, BioLORD), Vector Search & Neurosymbolic Knowledge Graphs**:
  - [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) — PDF Pages 46–50
- **Clinical NLP & LLMs in Medicine (NER, Entity Linking/Normalisation, Polarity/Negation, Temporality, Evaluation & Risks)**:
  - [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) — PDF Pages 51–59, 77–81
- **Medical RAG (Document RAG vs Real-World-Evidence OMOP RAG via MCP/Text-to-SQL)**:
  - [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) — PDF Pages 60–65
- **OMOP Common Data Model (CDM), OHDSI Tools (ATLAS, Achilles, DQD), ELADAIS ETL & Federated Analysis**:
  - [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf) — PDF Pages 66–76

---

## 3. Detailed Deck-by-Deck & Slide-by-Slide Breakdown

---

### Deck 1: [Session_01_CourseIntroduction.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_01_CourseIntroduction.pdf)
*Introductory Session: Data Science Production Pipelines, from the Data Source to Decisions (36 Pages)*

- **Slides 1–4**: Course title, introduction, and the "Raw data is like crude oil" analogy (value comes from refining it through pipelines into decisions).
- **Slide 5 — Context: The Growth of Data**: Exponential growth (2 to 181 zettabytes/year, 2010–2025) and the value hierarchy (`Data → Information → Knowledge → Decision`).
- **Slide 6 — Where the Data Comes From**: Proliferation of automated data acquisition systems (45% machine-to-machine, 45% unstructured: IoT/sensors, video, social/personal content, CRM/ERP).
- **Slide 7 — Why Now: Affordable Compute**: Exponential drop in hardware cost per unit across **Moore's Law** (compute), **Kryder's Law** (storage), and **Nielsen's Law** (bandwidth).
- **Slide 8 — The Cloud as Catalyst**: Cloud adoption & market share (AWS, Azure, GCP); shift from CAPEX to OPEX, elasticity, and managed services.
- **Slide 9 — The Democratisation of Techniques**: Evolution across four eras:
  - *2000s*: Specialist tools (SAS, SPSS, MATLAB)
  - *2010s*: Open-source ecosystem (Python, pandas, scikit-learn, Jupyter)
  - *2018+*: AutoML & low-code (Power BI, KNIME, Dataiku)
  - *2023+*: AI assistants & vibe coding
- **Slide 10 — What a Data Scientist Is (Venn Diagram Revisited in 2026)**: Intersection of Computer Science & IT, Maths & Statistics, and **Domain & Business Knowledge** (the only circle not automated by AI).
- **Slides 11–12 — AI Adoption & Seniority**: Why senior profiles benefit most from AI; comparison of Junior ("solves tasks") vs Senior ("solves the right problems") across daily tasks, autonomy, and communication.
- **Slide 13 — Applications: Sector & Function Map**: Data science use cases across Consumer Goods, Telecoms, Banking & Insurance, Industrial Goods, E-commerce, and Media mapped to Sales, Marketing, Operations, and Customer LTV.
- **Slide 14 — Applications: Health Sciences**: 12 healthcare use cases across 4 pillars:
  1. *Clinical decision*: Predictive diagnosis, Personalised treatment, Clinical decision support (CDSS), Medical imaging.
  2. *Data foundation*: Free-text structuring, Multimodal record, Hospital Data Federation.
  3. *Management & operations*: Active patient management, Remote monitoring, Evidence reasoning with LLMs.
  4. *Research*: Drug discovery, Genomic medicine.
- **Slide 15 — Process / Operational Architecture: The Data Science Pipeline**:
  - **7 Sequential Phases**: `1. Generate → 2. Ingest → 3. Store (raw) → 4. Transform/Integrate (curated) → 5. Persist (consumption) → 6. Exploit → 7. Act`.
  - **Transversal Layer**: Governance, Data Quality, Lineage, Security/GDPR, FinOps.
- **Slide 16 — Pipeline Technologies & Stakeholders**: Mapping tools to each of the 7 stages (IoT/CRM/ERP; Kafka/Kinesis/NiFi/Airflow; S3/HDFS/Parquet/CSV/JSON; Spark/Databricks/Flink; PostgreSQL/MongoDB/Cassandra/Redshift/Hive/Iceberg/Elastic/HBase; Jupyter/Power BI/RStudio/Kibana/Superset).
- **Slide 17 — Data Roles Comparison**: Side-by-side table of **Data Analyst**, **Data Scientist**, and **Data Engineer** (Core mission, typical tasks, skills, and tools).
- **Slide 18 — Who Intervenes Where**: Mapping Systems/IT, Data Engineer, Data Scientist, Data Analyst, and Business across the 7 pipeline stages.
- **Slide 19 — Role: Data Engineer**: 4 core responsibilities (Ingestion, Architecting, Transformation, Governance & Security).
- **Slide 20 — What is Data Science?**: Data Science lifecycle diagram and classic Venn diagram.
- **Slide 21 — Role: Data Scientist (The Modelling Process Pipeline inside Step 6 Exploit)**: `1. Data understanding → 2. Data preparation → 3. Model training → 4. Model evaluation → 5. Deploy & MLOps → 6. Model update`.
- **Slide 22 — Modelling: Three Families of Technique**:
  1. *Supervised Learning* (Regression, Classification: XGBoost, LightGBM, Random Forest, GLM, Neural Nets)
  2. *Unsupervised Learning* (Clustering, Dimensionality reduction, Anomaly detection: K-Means, DBSCAN, PCA, Isolation Forest, Autoencoders)
  3. *Language & Foundation Models* (NLP, RAG, Agents, Multimodal: Transformers, BERT, GPT/Claude/Llama)
- **Slide 23 — Technology: LLM Disruption by Role**: Specific new capabilities LLMs bring to Data Engineers, Data Scientists, and Data Analysts.
- **Slides 24–25 — Architecting the Solution on AWS**: End-to-end AWS architecture diagrams for data engineering and SageMaker ML pipelines.
- **Slides 26–30 — Course Plan & Objectives**: Sessions 01–14 schedule and 6 course learning outcomes.
- **Slide 31 — Assignment Structure**: 4 Work Packages (WP1 Planning & Business Case, WP2 Data Engineering, WP3 Data Science, WP4 Exploitation & Consumption) on one team dataset.
- **Slides 32–34 — Course Assessment & Faculty**: Grading breakdown (50% Assignments, 50% Final Exam), continuous evaluation rules, and contact details for Prof. Ernestina Menasalvas Ruiz and Borja Jordan de Urries Ruiz.
- **Slide 35 — Readings & Open Data Sources**: Recommended bibliography and public dataset portals.

---

### Deck 2: [Session_02_CRISP_DM_PDF.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_02_CRISP_DM_PDF.pdf)
*CRISP-DM: Cross-Industry Standard Process for Data Mining (51 Pages)*

#### Block 1: CRISP-DM Theory (Slides 1–19)
- **Slides 1–5 — Overview of CRISP-DM**: Origins (1996–2000 consortium), the 6 iterative phases, the core question each phase answers, and the concrete deliverables of each phase.
- **Slide 6 — Complete CRISP-DM Task Map**: Full breakdown of generic tasks and specialised outputs across all 6 phases (Chapman et al., 2000).
- **Slide 7 — Where CRISP-DM Sits in the Value Chain**: CRISP-DM governs **Step 6 (Exploit)**, connecting back to business understanding and forward into operational deployment.
- **Slide 8 — Three Principles & Effort Split**: Iteration is normal, business anchors the loop, and typical project effort allocation (**~50% spent in Phase 3: Data Preparation**, 10% Business Understanding, 15% Data Understanding, 10% Modeling, 5% Evaluation, 10% Deployment).
- **Slides 9–10 — Phase 1: Business Understanding**: Determining business objectives, assessing situation (risks, constraints, SWOT), translating to data mining goals, and producing the project plan.
- **Slide 11 — Phase 2: Data Understanding**: 6 activities (Collect initial data, Describe data, Explore data / EDA, Verify data quality, Formulate initial hypotheses, Document).
- **Slides 12–14 — Phase 3: Data Preparation**: Selecting, cleaning (handling collinearity, meaningful nulls, technical vs business outliers), constructing, integrating, and formatting the Analytic Base Table (ABT).
- **Slide 15 — Phase 3 Deep Dive: Feature Engineering**:
  - *Feature Operations*: Window aggregations, RFM (Recency/Frequency/Monetary), categorical encoding, scaling, ratios/interactions, temporal/text/image features.
  - *Feature Selection*: SHAP/permutation importance, collinearity check, temporal stability, leakage test, missingness as signal, compute cost.
  - *4 Golden Rules*: **1. No temporal leakage**, **2. Same grain as the decision**, **3. Train-production parity**, **4. Explainable by construction**.
- **Slides 16–17 — Phase 4: Modeling**: Selecting modelling techniques, designing validation (train/validation/test split or temporal split, baseline comparison), building and assessing models across the 3 technique families.
- **Slide 18 — Phase 5: Evaluation**: 3 evaluation pillars — **Performance** (metrics on unseen data), **Interpretation** (does it make domain sense?), and **Impact** (net profit in € vs baseline).
- **Slide 19 — Phase 6: Deployment**: Defining *Who* consumes the output, *How* (batch table, real-time API, dashboard), and *How often*; monitoring data drift, calibration, and business uplift.

#### Block 2: CRISP-DM Worked Case Study — €1M Action Banner Campaign for Premium Frying Pans (Slides 20–50)
- **Slides 21–24 — Phase 1 (Business Understanding)**:
  - **5 Key Numbers**: €1M budget, €10 CPM (€0.20 per 20-impression flight per customer), 5M customers in CRM, €80 retail price, €40 gross margin per pan.
  - **Break-Even Conversion Threshold**: $p^* = \frac{€0.20}{€40} = 0.005 = 0.50\%$.
  - **Pilot Baseline**: 400k random pilot yielded $0.41\%$ conversion $\Rightarrow$ full random rollout would **lose -€180k** (or -€224k annualized).
  - **ROI Math (Slide 24)**: Margin vs revenue trap, incremental vs total sales, and why maximizing net € profit beats maximizing ROI %.
- **Slides 25–30 — Phase 2 (Data Understanding)**:
  - **3 Data Sources**: `CRM` (5M customers, 1 row/customer), `Order Book` (7.1M order lines), `Pilot` (400k targeted customers with binary label `bought_pan`).
  - **Schema & EDA**: 18 source columns, `recency_days = 999` sentinel value for never-buyers, EDA showing **10x conversion lift** for prior cookware buyers with recent purchases, and data quality action plan.
- **Slides 31–34 — Phase 3 (Data Preparation)**:
  - **ETL Pipeline**: Aggregate order book prior to cut-off date $\rightarrow$ Join to CRM $\rightarrow$ Engineer 12 features $\rightarrow$ Join pilot labels $\rightarrow$ 70/30 stratified train/test split (280k train / 120k test).
  - **Analytic Base Table (ABT) & 12 Features (Slide 33)**: RFM features, category affinities (`cookware_share`, `has_bought_cookware`), ratios (`avg_ticket_trend`), and strict anti-leakage cut-off enforcement.
- **Slides 35–38 — Phase 4 (Modeling)**:
  - **Models Compared**: Logistic Regression (baseline, Test ROC AUC = `0.807`) vs `HistGradientBoostingClassifier` (Test ROC AUC = `0.812`).
  - **Explainability**: Permutation importance and partial dependence plots showing top 4 drivers (`has_bought_cookware`, `recency_days`, `orders_12m`, `monetary_12m`), plus scored customer table ranked into deciles.
- **Slides 39–43 — Phase 5 (Evaluation)**:
  - **Decile Analysis Table (Slide 39)**: Decile 1 converts at `1.88%` (Lift `4.59x`), Decile 2 converts at `0.83%` (Lift `2.02x`), Decile 3 drops to `0.38%` (below the `0.50%` break-even threshold).
  - **Financial Outcome (Slides 40–41)**: Target **only Deciles 1 & 2** (1M customers, spending €200k instead of €1M) $\Rightarrow$ **+€361k net profit** vs **-€224k loss** under mass campaign, freeing €800k of budget.
  - **Compounding Business Levers (Slide 42)**: Negotiating CPM (-25%), bundling a lid (+€15 margin), landing page A/B test (+15% CVR), and capturing web browse data compound net profit from **€361k to €1.09M**.
- **Slides 44–50 — Phase 6 (Deployment & Summary)**:
  - Weekly scoring pipeline to DSP + 5% random holdout control group, drift/calibration alerts, Swagger REST API spec for real-time CRM scoring (Slide 46), live campaign dashboard (Slide 47), next-iteration roadmap (uplift modelling, clickstream), and 1-page summary table across all 6 phases (Slides 49–50).

---

### Deck 3: [Session 04 - Team Project_DA.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2004%20-%20Team%20Project_DA.pdf)
*Team Project Guidelines & Evaluation Rubric (15 Pages)*

- **Slide 2 — Project Overview**: Teams of 5 students, 1 real-world open dataset, 4 Work Packages (WP1–WP4) tailored to 4 distinct stakeholders, random presenter selection, final Executive Memo & oral defence.
- **Slides 3–4 — Task 1: Dataset Selection**: Must support a real operational/financial decision with sufficient volume and complexity (no toy datasets like Titanic or Iris); proposal submission checklist.
- **Slide 5 — Four Work Packages, Four Audiences**:
  - **WP1**: Board / Clinical Director ("Should we fund this?")
  - **WP2**: CTO / CDO / Data Engineering Team ("Can we build and run the data pipeline?")
  - **WP3**: Decision Owner ("Does the model work and can I trust its recommendations?")
  - **WP4**: End Users & Finance ("How do I use it Monday morning and did it deliver the P&L impact?")
- **Slide 6 — WP1 Requirements (Planning & Business Case)**: Context, specific decision, primary KPI & baseline, executive EDA, expected financial value (ROI/P&L), data sources & hypotheses, delivery mode.
- **Slide 7 — WP2 Requirements (Data Engineering)**: Source systems, end-to-end architecture diagram, batch vs streaming justification, raw storage layer, ETL curation steps, scalability plan, target analytical schema (PK/FK), data dictionary, and quality/governance tests.
- **Slide 8 — WP3 Requirements (Data Science)**: Feature engineering & target definition, technique family justification, candidate models & validation design, cost matrix of False Positives vs False Negatives, explainability (SHAP/drivers), scalability, uncertainty & final recommendation.
- **Slide 9 — WP4 Requirements (Exploitation & Consumption)**: Consumption mode (dashboard, worklist, API), working prototype, adoption/change-management plan, reconciliation with WP1 financial baseline, and user tutorial or OpenAPI/Swagger specification.
- **Slide 10 — Final Executive Memo & Defence**: 5-part executive memo + technical annexes; 10-minute presentation + 5-minute Q&A evaluated on Coherence, Judgement, Honesty, and Command.
- **Slides 11–14 — Assessment Rubrics & Calendar**: Presentation rules, qualitative rubric across 6 dimensions (Slide 12), quantitative grading weights (Slide 13), and milestone schedule (Slide 14).

---

### Deck 4: [Session 05- BussinesCast-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005-%20BussinesCast-Part_1.pdf)
*From Data Systems to Positive Impact on the Company's P&L — Part 1 (78 Pages)*

- **Slides 1–3 — Core Thesis**: Every data science project exists to move a P&L line (`P&L line → Business question → Source systems → Pipeline → Model → Action → Measured impact`).

#### Block 1: The Data Systems of a Company (Slides 4–17)
- **Slide 5 — Modern Data Architecture**: Sources $\rightarrow$ Ingestion $\rightarrow$ Storage $\rightarrow$ Transformation $\rightarrow$ Serving across **Bronze (Raw)**, **Silver (Curated)**, and **Gold (Consumption)** medallion layers.
- **Slide 6 — Operational (OLTP) vs Analytical (OLAP)**: Comparison of workload, normalization (3NF vs Star Schema), latency, query patterns, and users.
- **Slides 7–8 — Building the Kimball Star Schema**: How 4 nightly `dbt` jobs transform OLTP tables into `fact_sales`, `dim_date`, `dim_customer` (with **Slowly Changing Dimension SCD Type 2** `valid_from`/`valid_to`), and `dim_product`.
- **Slide 9 — Database Selection Matrix**: When to use Relational OLTP, Columnar/MPP Warehouse, Lakehouse, Document/Key-Value, Time-series, Event log, Graph, or Vector DBs.
- **Slides 10–11 — ERP (System of Record)**: Core modules (FI/CO, MM, SD, PP, WM, HCM), vendors by tier (SAP S/4HANA, Oracle, Microsoft Dynamics, Odoo), core tables (`customers`, `orders`, `order_lines`, `products`, `invoices`, `gl_entries`, `stock_movements`), and analytical pitfalls (credit notes, fiscal periods, unit conversions).
- **Slides 12–13 — CRM (System of Intent)**: Marketing, Sales, and Service lifecycles; core objects (`leads`, `contacts`, `accounts`, `opportunities`, `quotes`, `cases`, `activities`, `campaigns`); Salesforce/HubSpot; and the `erp_customer_id` identity gap.
- **Slide 14 — The 6 CRM ↔ ERP Integrations**: Customer master sync, Catalogue & price lists, Quote-to-order, Order/invoice status, Payments/dunning, Credit limit checks.
- **Slide 15 — Sector-Specific Operational Systems**: POS, Ecommerce, Core Banking, MES/SCADA, TMS/WMS, OTT/Ad servers, HCM, Contact Centre, Web Analytics.
- **Slide 16 — Data Governance**: Master Data Management (MDM), Data Catalogue, Data Quality Tests, Lineage, Privacy/Regulation (GDPR, PSD2, Basel, EU AI Act), and Ownership/Data Mesh.
- **Slide 17 — Roles Along the Value Chain**: Systems/IT, Data Engineer, Data Scientist, Data Analyst, Business Owner.

#### Block 2: How Companies Make and Lose Money (Slides 18–28)
- **Slide 19 — The P&L Statement at a Glance**: Waterfall from `Revenue - COGS = Gross Margin - OPEX (S&M, R&D, G&A) = EBITDA - D&A = EBIT - Interest & Tax = Net Profit`, plus operating leverage.
- **Slide 20 — The Three Executive Levers**: 1. Sell more (Revenue), 2. Spend less (COGS & OPEX), 3. Use less capital (Working capital & CAPEX).
- **Slide 21 — The Use-Case Map**: Mapping data science projects and KPIs to specific P&L lines.
- **Slides 22–23 — Digital Unit Economics (P&L of One Customer)**:
  - Definitions & SQL queries from source tables (`ad_spend`, `users`, `fct_orders`) for **CAC**, **Contribution Margin per Order**, **LTV (CLTV)**, **Payback Period**, and **LTV/CAC Ratio** (healthy $\ge 3\times$, payback $< 12$ months).
- **Slide 24 — Churn: The Multiplier**: Sector churn benchmarks, 3 core formulas ($\text{Expected Life} = 1/\text{churn}$, $\text{LTV} = \text{Monthly Margin}/\text{churn}$, $\text{Payback} = \text{CAC}/\text{Monthly Margin}$), and profit sensitivity to churn reduction.
- **Slide 25 — LTV/CAC & Payback Benchmarks**: Comparison across 11 industries and cohort vs blended measurement rules.
- **Slide 26 — Bridging Model Metrics to Business Metrics**: How AUC/F1, MAPE/RMSE, and NDCG translate into euro impact via cost matrices, inventory simulations, and A/B holdout tests.
- **Slides 27–28 — Whiteboard Challenge 1 (20 M€ Online Fashion Shop)**: Comparing a returns-reduction model vs a retention campaign on the P&L.

#### Block 3: Customer Acquisition & Online Marketing (Slides 29–56)
- **Slides 30–33 — Marketing Funnel & 5 Data Levers**: Awareness $\rightarrow$ Interest $\rightarrow$ Consideration $\rightarrow$ Action $\rightarrow$ Loyalty; funnel metrics (**CPM, CTR, CPC, CPL, CVR, CAC, LTV**); and how 5 data interventions double LTV/CAC from `1.35` to `2.70`.
- **Slides 34–39 — Web Tracking, Google Tag Manager (GTM) & Marketing Data Mart**:
  - GA4 event schema (`session_start`, `view_item`, `add_to_cart`, `begin_checkout`, `purchase`) and BigQuery raw export (`events_YYYYMMDD`).
  - Client-side vs Server-side tagging, Consent Management Platforms (CMP), and cookie loss.
  - **Identity Resolution (Slide 36)**: Stitching 9 identifiers (`fbclid`, `gclid`, `client_id`, `anonymous_id`, `user_id`, `customer_id`, `email_hash`, `phone`, `loyalty_card`) into a single `customer_key`.
  - **Marketing Data Mart Schema (Slide 37)** and the 6-stage journey of a click event from browser `dataLayer` to Reverse ETL activation (Slides 38–39).
- **Slides 40–44 — Acquisition Use Cases & End-to-End Case: Value-Based Bidding (`CAC → pLTV`)**:
  - Predicting 12-month customer LTV (`pLTV`) within 1 hour of first purchase using a **LightGBM regressor with quantile/Tweedie loss** (Slide 43) and pushing `pLTV` back to Google Ads / Meta Conversions API (CAPI) so ad auctions bid for value rather than volume.
- **Slides 45–47 — Acquisition Channels & Real-Time Ad Auctions**: What ad platform APIs expose vs hide; how second-price/VCG ad auctions rank $\text{Bid} \times P(\text{Click}) \times P(\text{Convert})$; funnel unit math.
- **Slides 48–52 — Marketing Attribution: Whose Sale Is It?**:
  - Multi-touch journey complexity and UTM/click-ID tracking.
  - **Slide 52 — Master Comparison of 4 Attribution Methods**:
    1. *Deterministic Rules* (Last-click / First-click / Linear)
    2. *Data-Driven Multi-Touch Attribution (MTA)* (Shapley values, Markov chains)
    3. *Marketing Mix Modelling (MMM)* (Bayesian regression with Adstock decay & Hill saturation curves)
    4. *Incrementality Testing* (Geo-holdout experiments & Difference-in-Differences)
- **Slide 53 — LLMs in Customer Acquisition**: Creative generation, search intent clustering, conversational lead qualification, review mining, Answer Engine Optimisation (AEO).
- **Slides 54–56 — Marketing Dashboards & Sector Funnel Comparison**: Monday 9:00 acquisition dashboard, 9-month cohort retention triangle, and B2C vs B2B funnel comparison.

#### Block 4: Ecommerce (Slides 57–77)
- **Slide 58 — Ecommerce P&L Waterfall**: $\text{Revenue} = \text{Traffic} \times \text{Conversion} \times \text{Basket} \times \text{Frequency}$; Zalando-style fashion P&L (returns, shipping, warehouse pick/pack, payment fees, markdowns).
- **Slides 59–60 — Ecommerce Systems Map & Core Tables**: Storefront (Shopify/SFCC), PIM, OMS, PSP/Fraud, Search/Reco, WMS/3PL, CDP, CRM; schema for `customers`, `orders`, `order_lines`, `products`, `events`, `returns`, `transactions`.
- **Slides 61–63 — Customer Data Platform (CDP)**: How a CDP collects events, resolves identity, builds real-time traits, and activates audiences (Warehouse vs CDP vs CRM comparison + cookware retail media case).
- **Slides 64–65 — Automated CRM Flows & Ecommerce Use-Case Portfolio**: 5 lifecycle flows (Welcome, Browse abandon, Cart abandon, Post-purchase, Win-back) and P&L impact of 7 core ML models.
- **Slides 66–70 — End-to-End Case: RFM $\rightarrow$ LTV $\rightarrow$ Differentiated Action**:
  - SQL `NTILE(5)` construction of Recency, Frequency, Monetary quintiles and R×F segmentation grid (Slide 67).
  - Probabilistic **BG/NBD + Gamma-Gamma** (`lifetimes`) vs **LightGBM** 12-month LTV prediction + **Uplift Modelling** (targeting *Persuadables* while suppressing *Sure Things* and *Sleeping Dogs*) (Slides 68–70).
- **Slides 71–73 — Lookalike Audiences (External & Internal)**: Platform lookalike seed uploads vs building an internal propensity/lookalike classifier in-house (worked Omega-3 subscription case study).
- **Slide 74 — How a Recommender System Works**: Collaborative filtering matrix factorization, **Two-Tower Neural Architecture** (User tower + Item tower $\rightarrow$ dot-product cosine similarity), 50ms ANN retrieval (`Faiss`/`pgvector`) + business rule re-ranking.
- **Slides 75–77 — Ecommerce Executive Dashboards & LLMs in Ecommerce**: CEO Monday dashboard, category performance matrix, semantic search, catalogue enrichment, and agentic shopping assistants.

---

### Deck 5: [Session 05 - BussinesCast-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session%2005%20-%20BussinesCast-Part_2.pdf)
*From Data Systems to Positive Impact on the Company's P&L — Part 2 (44 Pages)*

#### Block 2 (Cont.): Key Performance Indicators (KPIs) (Slides 3–7)
- **Slide 4 — Metric vs KPI**: A KPI has a Target, Owner, Frequency, Single Source of Truth, and Pre-committed Action; **Leading vs Lagging** indicators; decomposing a North-Star KPI into a **KPI Tree**.
- **Slide 5 — Sector KPI Matrix**: Financial, Customer, Operational, and Signature KPIs across 7 industries.
- **Slide 6 — Commercial KPIs (Formulas, SQL & Red Flags)**: Conversion Rate, Average Order Value (AOV), 90-day Repeat Rate, CAC by Channel, Monthly Churn, 12-month Realised Cohort LTV.
- **Slide 7 — Operational & Financial KPIs (Formulas, SQL & Red Flags)**: Industrial **OEE** ($\text{Availability} \times \text{Performance} \times \text{Quality}$), Logistics **On-Time Delivery (OTD)**, **Cost per Stop**, Banking **Cost of Risk (bps)**, Retail **Inventory Days (DIO)**, Banking **Cost-to-Income Ratio**.

#### Block 5: Banking (Slides 8–16)
- **Slide 9 — How a Bank Makes and Loses Money**: Net Interest Margin (NIM), Fee Income, Operating Costs (Cost-to-Income), and Provision for Loan Losses (**Cost of Risk**).
- **Slides 10–11 — Banking Systems Map & Core Tables**: Two operational speeds — **150ms real-time card fraud scoring** vs **seconds + nightly batch credit origination** across Core Banking (COBOL/Temenos), Bureau APIs, and Lakehouse; core tables (`customers`, `contracts`, `transactions`, `applications`, `bureau_data`, `collections`).
- **Slides 12–15 — Banking Use Cases & End-to-End Case: Credit Scoring (`PD, LGD, EAD`)**:
  - Expected Loss formula: $\text{EL} = \text{PD} \times \text{LGD} \times \text{EAD}$.
  - Regulated model spec: **Logistic Regression Scorecard with Weight of Evidence (WoE) binning** and **Monotonic Gradient Boosting**, adverse action reason codes, vintage default tracking, and **Population Stability Index (PSI)** monitoring under Basel III / IFRS 9 / EU AI Act.
- **Slide 16 — LLMs in Banking**: Why LLMs cannot make autonomous credit decisions (EU AI Act High-Risk Annex III), and where they deliver value (KYC/mortgage document extraction, policy RAG, call centre summarisation, transaction merchant enrichment).

#### Block 8: Media & Video on Demand (Slides 17–27)
- **Slides 18–19 — Streaming/Media P&L & Systems Map**: Hybrid subscription + ad-supported revenue vs content amortisation (~45% of revenue); MAM/CDN, OTT player, Zuora billing, Ad Server/SSP, CDP.
- **Slide 20 — Player Heartbeat Events**: Extracting 6 families of behavioural signals from `playback_events` (emitted every 60–90s) to power recommendations and early churn detection.
- **Slides 21–24 — Subscriber RFM, Core Tables, Ad Yield & Hybrid ARPU Economics**:
  - **Subscriber RFM** where $M = \text{Magnitude (hours watched)}$, not money (Slide 21).
  - Ad monetisation math ($\text{Impressions} \times \text{CPM}$) and hybrid tier unit economics ($\text{ARPU}_{\text{total}} = \text{ARPU}_{\text{sub}} + \text{ARPU}_{\text{ads}}$) (Slides 23–24).
- **Slides 25–26 — End-to-End Case: Subscription Churn Reduction**:
  - Combining a **LightGBM 30-day voluntary churn classifier** with an **Uplift model** (Persuadables vs Do-Not-Disturb) and separating involuntary payment churn (handled via card dunning retries).
- **Slide 27 — Full Media Data Science Portfolio**: Thumbnail/artwork personalisation, content greenlighting/valuation, dynamic paywalls, audience measurement.

#### Block 6: Industrial Controlling (Slides 28–34)
- **Slides 29–30 — Industrial Data Sources & SCADA (OT) vs SAP (IT)**:
  - Integrating 9 plant sources (SAP CO/PP/PM, MES, SCADA/PLC historian tags, energy meters, CMMS, LIMS, timesheets, electricity spot prices).
  - How a single 22-minute hydraulic press stop is recorded at millisecond frequency in SCADA/PLC vs month-end financial postings in SAP, bridged by the **MES (Manufacturing Execution System)**.
- **Slides 31–34 — Standard Cost Stack, OEE KPI Tree & Weekly Variance Bridge**:
  - 5 layers of unit cost (Direct Material, Direct Labour, Energy, Variable Overhead, Fixed Overhead Absorbed).
  - Decomposing standard-to-actual cost gaps into **Price Variance**, **Usage/Scrap Variance**, **Efficiency Variance**, and **Volume Variance** for Monday plant review.

#### Block 7: Logistics (Slides 35–43)
- **Slides 36–39 — Logistics P&L, Systems Map, TMS Workflow & Tables**:
  - Thin ~5% EBIT margin economics driven by drop density, first-attempt delivery rate, and fleet utilisation.
  - How a **Transportation Management System (TMS)** operates across 6 steps (`Order → Plan → Tender → Execute → Freight Audit → Analyse`) alongside WMS and GPS telematics (`shipments`, `routes`, `stops`, `gps_pings`, `warehouse_moves`, `carrier_rates`, `claims`).
- **Slides 40–42 — End-to-End Case: ETA & Failed-Delivery Prediction**:
  - Dual model per delivery stop: **LightGBM Quantile Regression** (`p10 / p50 / p90` arrival time window) + **Failed-Delivery Classifier** ($P(\text{recipient absent}) > 0.38 \Rightarrow$ proactive SMS to divert parcel to a nearby locker/pickup point, saving €4.80 re-delivery cost).
- **Slide 43 — LLMs in Logistics**: Customs/CMR bill-of-lading OCR extraction, messy address normalisation, driver/customer WhatsApp bots, control-tower planner copilot.

---

### Deck 6: [Session_6_Data_Engineering-Part_1.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Session_6_Data_Engineering-Part_1.pdf)
*Data Engineering — Part 1: Architecture, Cloud, Generation & Ingestion (80 Pages)*

- **Slides 1–5 — Introduction & Lifecycle**: Why data engineering determines model success; the 7 lifecycle stages and 4 data states (In Motion, Raw, Curated, Consumption).
- **Slides 6–22 — Running Case: ShopCo (Online Fashion Retailer) & Ana's Black Friday Evening**:
  - Tracing 8 customer moments (19:58 Instagram ad $\rightarrow$ 20:01 browsing $\rightarrow$ 20:04 cart add $\rightarrow$ 20:06 abandonment $\rightarrow$ 20:37 push coupon $\rightarrow$ 20:41 checkout $\rightarrow$ 02:00 nightly ETL $\rightarrow$ 08:00 CEO dashboard).
  - Polyglot persistence: Product catalogue in **MongoDB** (flexible nested attributes) vs Orders/Customers in **PostgreSQL** (ACID transactions) (Slide 8).
  - Common JSON event envelope (Slide 9) and **Lambda/Kappa dual-path architecture**: **Hot path** (`Kafka → Flink → Redis`) for sub-second / 30-min triggers vs **Cold path** (`S3 → Spark → Redshift`) for analytics & ML training (Slides 10–22).
- **Slides 23–27 — Before the Cloud: The Distribution Paradigm**:
  - **Scale Up (Vertical)** vs **Scale Out (Horizontal)** (Slide 23).
  - **Trick 1 — Distributed Storage**: Splitting files into fixed blocks replicated across nodes (HDFS/S3) and why changing the partition key triggers an expensive network **shuffle** (Slides 24–25).
  - **Trick 2 — Distributed Compute**: Moving code to the data (MapReduce/Spark) and the classic **"averaging averages" bug** (why you must pass `(sum, count)` tuples instead of partial means) (Slides 26–27).
- **Slides 28–40 — Block 01: Where It Runs — On-Premise vs Cloud (AWS Deep Dive)**:
  - On-Premise vs Cloud economics (CAPEX vs OPEX) and service models (**On-Prem vs IaaS vs PaaS/Managed vs Serverless**) (Slides 28–30).
  - Cloud provider rosetta stone: **AWS vs Azure vs GCP** equivalents across every pipeline stage (Slide 31).
  - **Amazon S3 Deep Dive**: Object storage structure, storage tiers (`Standard`, `Intelligent-Tiering`, `Glacier`), pricing, and `aws s3` / `boto3` snippets (Slide 33).
  - **AWS Serverless & Compute**: API Gateway, Lambda, DynamoDB, S3 Event Notifications, SQS Dead-Letter Queues, Firehose, Athena, EventBridge, Step Functions, Glue; choosing between **Lambda, ECS+Fargate, AWS Glue, and EMR** (Slides 34–35).
  - **Queues vs Streams on AWS**: Comparing **SQS** (task queue), **SNS** (pub/sub fanout), **Kinesis Data Streams**, and **Amazon MSK (Managed Kafka)** (Slides 36–37).
  - Hands-on Python Lambda function triggered by S3 upload + ShopCo Black Friday auto-scaling buffer architecture (Slides 38–40).
- **Slides 41–51 — Block 02: Stage 1 Generate — Where Data Is Born**:
  - 4 source families: **Operational Databases**, **REST APIs**, **Event Streams**, **Files/Documents** (Slides 41–42).
  - **Database Extraction Patterns (Slide 43)**:
    1. *Full Load* (`SELECT *` — simple, small tables only)
    2. *Incremental / Watermark* (`WHERE updated_at > :last_run` — misses hard deletes)
    3. *Change Data Capture (CDC)* (reading the DB transaction log / WAL — captures inserts, updates, and deletes in real time without querying the table)
  - **REST API Extraction (Slide 44)**: Handling auth, cursor/offset pagination, exponential backoff on HTTP `429`, and Python `requests` implementation.
  - **Event Streams & Kafka Basics (Slides 45–51)**: How collector endpoints validate and publish JSON events to Kafka partitions by `hash(user_id) % N`, CLI inspection (`kafka-topics.sh`, `kcat`, `kafka-consumer-groups.sh`), and Python `confluent_kafka` Producer code.
- **Slides 52–79 — Block 03: Stage 2 Ingest — Moving Data, Unchanged**:
  - **Batch vs Streaming Ingestion** trade-offs (latency, cost, complexity) and the 3 write patterns: **Command** (sync DB), **Task** (SQS queue), **Fact** (immutable Kafka log) (Slides 52–56).
  - **Apache Kafka Deep Dive (Slides 57–67)**: Brokers, Topics, Partitions, Offsets, Consumer Groups (horizontal scaling & partition assignment), Key-based ordering guarantees, Log retention vs Log Compaction, and code examples for **Python Consumer**, **Flink SQL**, **Spark Structured Streaming**, and **Kafka Connect S3 Sink**.
  - **Amazon Kinesis** (`boto3` producer & Firehose S3 delivery) and the **Full Ingestion Toolbox Matrix** (Sqoop, DMS, Airbyte/Fivetran, Glue vs Kafka Connect, Firehose, Debezium, MQTT) (Slides 68–69).
  - **Apache NiFi (Slides 70–72)**: Visual dataflow routing, FlowFiles (content + attributes), Processors, Back-pressure queues, Data Provenance, and ShopCo 3-source NiFi canvas.
  - **Orchestration with Apache Airflow (Slides 73–74)**: Why `cron` fails at scale; DAGs, Operators, Tasks, retries, backfills, and a complete Python Airflow DAG example.
  - **Landing Zone Best Practices (Slide 75)**: Hive-style date partitioning (`s3://bucket/raw/events/dt=2026-11-27/`), idempotency, avoiding the small-files problem, and handling schema drift.
  - **Debezium CDC Deep Dive (Slides 76–78)**: Tailing PostgreSQL's Write-Ahead Log (WAL) into Kafka envelope messages (`before`, `after`, `op: c/u/d`, `ts_ms`) with zero impact on production queries.

---

### Deck 7: [Sessions_07.Data_Engineering-Part_2.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_07.Data_Engineering-Part_2.pdf)
*Data Engineering — Part 2: Storage, Transformation, Spark, Databases, Streaming & Governance (100 Pages)*

#### Block 04: Stage 3 Store — Raw Storage, File Formats & Lakehouse (Slides 3–19)
- **Slides 3–4 — Amazon S3 Object Storage**: Immutability, flat key-value namespace, `boto3` upload/download.
- **Slides 5–13 — File Formats Deep Dive (`CSV`, `JSON Lines`, `Avro`, `Parquet`, `ORC`)**:
  - **Row-Oriented (`CSV`, `JSONL`, `Avro`)** vs **Columnar (`Parquet`, `ORC`)** physical disk layouts (Slides 6–9).
  - **Why Parquet Is 5–10x Smaller & Faster (Slides 10–11)**: Schema stored once in the footer, native binary types, Row Groups + Column Chunks, Min/Max statistics for predicate pushdown, and column-specific encodings (**Dictionary encoding**, **Run-Length Encoding (RLE)**, **Bit-packing**, **Delta encoding** + Snappy/ZSTD compression).
  - **Avro & Schema Evolution (Slide 13)**: Row-based binary format with embedded JSON schema ideal for Kafka streaming and backward/forward schema evolution (`fastavro`).
- **Slide 14 — Parquet Hands-On (`pandas` & `PyArrow`)**: Reading specific columns (`columns=[...]`) and partitioned directories (`filters=[...]`).
- **Slides 15–18 — Data Lake vs Data Warehouse vs Lakehouse & Medallion Architecture**:
  - Schema-on-read (Lake) vs Schema-on-write (Warehouse).
  - **Apache Iceberg (Slide 16)**: Bringing ACID transactions, schema evolution, time-travel snapshots, and row-level GDPR `DELETE`/`MERGE` to S3 Parquet files.
  - **Medallion Architecture (Slides 17–18)**: Raw (**Bronze**) $\rightarrow$ Filtered/Cleaned (**Silver**) $\rightarrow$ Business Aggregates (**Gold**).

#### Block 05: Stage 4 Transform — Data Curation & Quality (Slides 20–29)
- **Slides 20–21 — Single-Node (`pandas`, `Polars`, `DuckDB`) vs Distributed (`Spark`)**: Choosing the right engine for the data volume.
- **Slides 22–25 — The 5 Data Curation Steps (with `pandas` code)**:
  1. **Deduplication** (`drop_duplicates` keeping latest timestamp per event/order ID).
  2. **String Normalisation** (Unicode NFKD accent stripping, lowercasing, regex mapping).
  3. **Type & Nested Structure Conversion** (ISO timestamps to UTC, flattening JSON with `json_normalize` and `explode`).
  4. **Missing Value Imputation** (Drop, constant, group median, forward-fill/model imputation + always adding a boolean `is_imputed` indicator column).
  5. **Outlier Treatment** (Tukey $1.5 \times \text{IQR}$ rule, Z-score, Isolation Forest, domain clipping + adding an `is_outlier` flag).
- **Slide 26 — Automated Data Quality Tests (`dbt`)**: Testing **Uniqueness**, **Completeness (`not_null`)**, **Validity (`accepted_values` / ranges)**, and **Freshness** in `schema.yml`.
- **Slides 27–28 — AWS Glue PySpark Job & ShopCo Identity Resolution**: Serverless ETL script and deterministic/probabilistic stitching of Ana's 5 identifiers into a single `customer_key`.

#### Block 06: Scalability — HDFS, MapReduce & Apache Spark (Slides 30–47)
- **Slides 30–32 — When Do You Need a Cluster?**: Benchmarks comparing `pandas` (<1 GB), `Polars` (1–50 GB), `DuckDB` (1–100 GB), and `PySpark` (100 GB – PB+).
- **Slides 33–35 — HDFS & MapReduce**: HDFS NameNode/DataNodes (128 MB blocks, 3x replication) and step-by-step trace of `Split → Map → Shuffle & Sort → Reduce`.
- **Slides 36–38 — Apache Spark Architecture**: Why Spark beats MapReduce (in-memory DAG execution); evolution from RDDs to DataFrames/Catalyst; **Driver** (`SparkSession`), **Cluster Manager**, **Executors**, **Job $\rightarrow$ Stage $\rightarrow$ Task $\rightarrow$ Partition**.
- **Slides 39–44 — `pandas` to `PySpark` Cheat Sheet & Lazy Evaluation**:
  - Side-by-side syntax comparison (`filter`, `withColumn`, `groupBy().agg()`, window functions, SQL).
  - **Transformations (Lazy)** vs **Actions (Eager: `count`, `collect`, `write`)** and how the **Catalyst Optimiser** reorders predicates and prunes columns before execution.
- **Slide 45 — What Is Expensive in Spark (and How to Fix It)**:
  - **Narrow Transformations** (`select`, `filter`, `withColumn` — zero network traffic) vs **Wide Transformations** (`groupBy`, `join`, `orderBy`, `distinct` — require a network **Shuffle**).
  - **3 Fixes for Slow Spark Jobs**: 1. Broadcast small lookup tables (`F.broadcast(small_df)`), 2. Enable Adaptive Query Execution (AQE) / tune `spark.sql.shuffle.partitions`, 3. Filter early and select only required columns.
- **Slide 46 — ShopCo Case**: PySpark self-join to compute "Frequently Bought Together" product pairs.

#### Block 07: Stages 5–6 Persist & Exploit — Choosing the Right Database (Slides 48–80)
- **Slides 48–54 — OLTP vs OLAP Storage Internals**:
  - How **PostgreSQL** writes (WAL append + 8 KB B-Tree heap page update) and reads (B-Tree index point lookup in ~1 ms).
  - How **Amazon Redshift** writes (columnar 1 MB blocks across MPP slices via bulk `COPY`) and reads (**Zone Maps** min/max block skipping + column pruning + SIMD vectorised scan).
- **Slides 55–75 — Deep Dive into the 7 Database Families (with Architecture & Hands-On Code)**:
  1. **Relational (OLTP) — PostgreSQL (Slides 55–56)**: ACID transactions, foreign keys, B-Tree indexes (`psycopg2` order transaction).
  2. **Key-Value — Redis & DynamoDB (Slides 58–59)**: In-memory $O(1)$ hash table lookup, sub-millisecond latency, TTL expiration (`redis-py` shopping cart state).
  3. **Document — MongoDB (Slides 60–61)**: Self-contained BSON/JSON documents, polymorphic attributes, secondary indexes (`pymongo` product catalogue).
  4. **Wide-Column — Apache Cassandra & HBase (Slides 62–64, 66–67)**: Masterless consistent-hashing ring, **Partition Key** (node placement) + **Clustering Key** (on-disk sort order), LSM-Tree append-only writes, query-first schema design; detailed comparisons of **Cassandra vs Redshift** (Slide 66) and **PostgreSQL vs Cassandra** (Slide 67).
  5. **Columnar MPP Warehouse — Amazon Redshift, Hive, Athena/Trino (Slides 65, 74–75)**: Star schemas, distribution styles (`KEY`, `EVEN`, `ALL`), sort keys, federated SQL over S3 Parquet via Athena.
  6. **Time-Series — TimescaleDB, InfluxDB, AWS Timestream (Slides 68–69)**: Time-partitioned hypertables/chunks, `time_bucket()` aggregations, automated downsampling & retention policies.
  7. **Search Engine — Elasticsearch / OpenSearch (Slides 70–71)**: Tokenisation, stemming, **Inverted Index** (term $\rightarrow$ posting list of doc IDs), BM25 scoring, Levenshtein fuzzy typo tolerance, Kibana log analytics.
  8. **Vector Databases — `pgvector`, Pinecone, Qdrant, Milvus, FAISS (Slides 72–73)**: Dense embeddings, cosine/L2 distance, **Approximate Nearest Neighbour (ANN)** indexes (**FLAT, IVF, PQ, HNSW** multi-layer navigable graphs), and hybrid RAG retrieval.
- **Slides 76–80 — Master Database Comparison & Decision Guide**:
  - **Slide 76**: Complete comparison table of all 7 database families (Data model, On-disk structure, Latency, Scale pattern, CAP theorem trade-off, Best use case, Anti-pattern).
  - **Slide 77**: Step-by-step architectural decision tree ("Which database should I pick?") + BI/Consumption tools overview (Jupyter, Power BI, Superset, Kibana, Athena).

#### Block 08: End-to-End Streaming (Slides 81–90)
- **Slides 81–87 — The 5 Pillars of a Streaming Pipeline**:
  1. **Event & Producer**: **Event Time** (when the click happened) vs **Processing Time** (when the server saw it); Schema Registry.
  2. **Broker**: Kafka/Kinesis partitioned log.
  3. **Stateful Stream Processor (Apache Flink / Spark Structured Streaming)**:
     - **Window Types (Slide 85)**: **Tumbling Window** (fixed, non-overlapping), **Sliding/Hopping Window** (fixed length, overlapping step), **Session Window** (dynamic length, closes after $N$ minutes of inactivity).
     - **Watermarks (Slide 86)**: Handling late-arriving out-of-order events (`WATERMARK FOR event_time AS event_time - INTERVAL '2' MINUTE`).
  4. **Delivery Guarantees (Slide 87)**: **At-most-once** (fire & forget), **At-least-once** (retry + idempotent sink upsert — industry standard), **Exactly-once** (distributed 2-phase commit checkpoints).
  5. **Low-Latency Serving Sink**: Redis / Kafka action topic.
- **Slides 88–90 — Batch vs Streaming Architecture & ShopCo Abandoned Cart Detector**: Flink SQL `SESSION(event_time, INTERVAL '30' MINUTE)` query detecting Ana's abandoned cart in 31 minutes.

#### Block 09 & 11: Data Governance & WP2 Mapping (Slides 91–99)
- **Slides 91–96 — Data Governance Pillars**: **Data Catalogue** (Glue/Unity Catalog/DataHub), **Data Lineage** (OpenLineage/dbt column-level DAG), **Data Dictionary & Data Contracts** (schema, SLAs, PII masking), and GDPR consent enforcement.
- **Slides 97–99 — Full Pipeline Recap & WP2 Assignment Mapping**: Exact mapping of WP2 deliverables to the slides in Sessions 06 and 07.

---

### Deck 8: [Sessions_08.Healthcare.pdf](file:///Users/luigizheng/Desktop/data analysis/Slides/Sessions_08.Healthcare.pdf)
*Data Science & Data Engineering in Healthcare (83 PDF Pages / 78 Numbered Slides)*
*(Note: Because 5 unnumbered/duplicate-numbered slides exist in the deck, both the **PDF Page** and **Slide Footer Number** are given below.)*

- **PDF pp. 1–3 (Slides 1–3) — Why Healthcare Data Is Unique**: ~80% of clinical information lives in unstructured free text, >20 disparate hospital systems, 30% of global data volume but <5% reused; collected for primary patient care (not research), fragmented across care settings, multimodal, and strictly regulated (GDPR Art. 9, EHDS, EU AI Act).

#### Block 01: Clinical Data Systems, Standards & Modalities (PDF pp. 4–27 / Slides 4–26)
- **PDF p. 5 (Slide 5) — Hospital Information Ecosystem**: Core **HIS** (admissions/ADT), **EHR/EMR** (clinical notes/orders), **LIS** (laboratory), **RIS/PACS** (radiology & DICOM images), **Pharmacy** (e-prescribing/dispensing), **ICU/Bedside Monitors** (waveforms), **Pathology**, **Genomics/Biobank**, **Coding/Billing (CMBD/DRG)**, and **Primary Care EHR**.
- **PDF pp. 6–10 (Slides 6–9) — How Hospital Systems Communicate**:
  - **Integration Engine (Mirth/Rhapsody)** routing **HL7 v2** pipe-delimited messages: `ADT^A01` (admission), `ORM^O01` (order), `ORU^R01` (lab/radiology result), `MDM^T02` (clinical document).
  - **DICOM workflow**: Modality Worklist (`MWL`), Performed Procedure Step (`MPPS`), and `C-STORE` to PACS.
  - Tracing a breast cancer patient's journey from HL7 messages into relational HIS tables (`PATIENT`, `ORDERS`, `RESULTS`, `MEDICATION`, `NOTES`, `IMAGING`).
- **PDF pp. 11–17 (Slides 10–16) — EHR Anatomy, Longitudinal Trajectory & Volume**:
  - Structure of an EHR, how clinical notes (CLOBs) and DICOM hierarchy (`Patient → Study → Series → Instance`) are stored, the 12 data sources outside the hospital walls, the 7 stages of a 10-year breast cancer pathway, and structured (~20%) vs unstructured (~80%) data volume in a 500-bed hospital.
- **PDF pp. 18–24 (Slides 17–23) — The 6 Clinical Data Modalities & Multimodal Fusion**:
  1. **Structured EHR** (p. 18): Demographics, ICD diagnoses, LOINC labs, ATC drugs; selection bias & upcoding pitfalls.
  2. **Clinical Free Text** (p. 19): Discharge summaries, oncology/pathology notes; abbreviations, spelling errors, and ~40% negated/hypothetical mentions.
  3. **Medical Imaging** (pp. 20–21): DICOM headers + pixel matrices (CT, MRI, Mammography, WSI Digital Pathology) and the 6-ID traceability chain (`MRN → OrderID → AccessionNumber → StudyInstanceUID → SeriesInstanceUID → SOPInstanceUID`).
  4. **Physiological Signals & Waveforms** (p. 22): High-frequency ICU/ECG streams (100–500 Hz), motion artefacts, sepsis/arrhythmia early warning.
  5. **Omics Data** (p. 23): Bioinformatics pipeline (`FASTQ → BAM → VCF → Annotated Variant` with HGVS, ClinVar, HPO).
  6. **Multimodal Fusion Architectures** (p. 24): **Early Fusion** (concatenating features/embeddings), **Late Fusion** (ensemble of modality-specific models), and **Joint / Intermediate Cross-Attention Fusion**.
- **PDF pp. 25–27 (Slides 24–26) — Heterogeneity, Interoperability Standards & Secondary Use**:
  - **5 Faces of Heterogeneity** (Syntactic, Semantic, Temporal, Quality, Legal — illustrated by 5 ways hospitals record HER2-positive status).
  - **Primary Care Exchange Standards** (**HL7 v2, HL7 FHIR, DICOM, CDA**) vs **Secondary Research Data Models** (**OMOP CDM, i2b2, openEHR, European Health Data Space / EHDS**).
  - The regulated circuit from Hospital HIS $\rightarrow$ Pseudonymisation $\rightarrow$ OMOP CDM $\rightarrow$ Trusted Research Environment (TRE).

#### Block 02: Clinical Use Cases & The Analytics Ladder (PDF pp. 28–39 / Slides 27–38)
- **PDF pp. 29–36 (Slides 28–35) — The 5-Rung Clinical Analytics Ladder (Breast Cancer Case)**:
  1. **Descriptive ("What happened?")** (p. 32): Cohort characterization & OMOP SQL query.
  2. **Diagnostic ("Why did it happen?")** (p. 33): Root-cause drill-down into why diagnosis-to-chemotherapy delay rose from 28 to 41 days (biopsy pathology bottleneck).
  3. **Predictive ("What will happen?")** (p. 34): Gradient boosting classifier predicting Pathological Complete Response ($P(\text{pCR}) = 0.61$, ROC AUC = `0.82`) with SHAP patient explanation.
  4. **Causal ("What if we intervene?")** (p. 35): Why correlation $\neq$ causation (**confounding by indication**), Causal DAGs, **Propensity Score Matching / IPW**, and the 5-step **Target Trial Emulation** framework.
  5. **Prescriptive ("What is the best action?")** (p. 36): Combining predicted benefit, cardiotoxicity risk, clinical contraindicating rules (LVEF < 50%), and patient utility to recommend a regimen.
- **PDF pp. 37–39 (Slides 36–38) — Bedside vs Operational Use Cases & Why 90% of Clinical Models Fail**:
  - Bedside CDSS vs Research/Operations portfolio, and the 4 deployment barriers (**Dataset shift / lack of external validation**, **Workflow friction / alert fatigue**, **Medical Device Regulation MDR / SaMD / AI Act**, **Lack of prospective clinical impact trials**).

#### Block 03: Ontologies, UMLS & Vector Knowledge (PDF pp. 40–50 / Slides 39–48)
- **PDF pp. 41–44 (Slides 40–43) — Clinical Vocabularies, SNOMED CT & UMLS**:
  - **Classification** (ICD-10 for billing) vs **Terminology** (LOINC, RxNorm) vs **Ontology** (SNOMED CT polyhierarchy with formal description-logic relationships).
  - **SNOMED CT Structure** (p. 43): Concepts, Descriptions (FSN + Synonyms), `Is-A` and attribute relationships (`Finding site`, `Associated morphology`).
  - **UMLS (Unified Medical Language System)** (p. 44): **Metathesaurus** grouping synonymous terms from >200 vocabularies under a single **CUI (Concept Unique Identifier)** (e.g., `C0006142` = Malignant neoplasm of breast), **Semantic Network** (127 semantic types), and **SPECIALIST Lexicon**.
- **PDF p. 45 (Slide 44) — Concept Normalisation Pipeline**: Mapping raw text mentions $\rightarrow$ UMLS CUI $\rightarrow$ OMOP Standard `concept_id` via OHDSI Athena (`Maps to` relationship), comparing classic NLP tools (**MetaMap, Apache cTAKES, QuickUMLS, scispaCy, MedCAT**) with LLMs.
- **PDF pp. 46–50 (Slides 45–48) — Medical Embeddings, Foundation Models & Neurosymbolic AI**:
  - Evolution of biomedical embeddings: Static (`word2vec`, `cui2vec`) $\rightarrow$ Contextual transformers (`BioBERT`, `ClinicalBERT`, `bsc-bio-ehr-es`) $\rightarrow$ Ontology-aligned contrastive encoders (**`SapBERT`**, **`BioLORD`**, **`CODER`**) $\rightarrow$ Graph embeddings (`snomed2vec`) & Multimodal foundation models (`RETFound`, `ECG-FM`).
  - Vector similarity search in PostgreSQL (`pgvector` `<=>` cosine distance) and **Neurosymbolic AI / Clinical Knowledge Graphs** (combining neural representation with symbolic ontology traversal and GraphRAG).

#### Block 04: LLMs in Medicine & Clinical NLP (PDF pp. 51–59 / Slides 49–57)
- **PDF pp. 52–53 (Slides 50–51) — Evolution & 8 Families of Clinical NLP**: From 1990s RegEx/NegEx $\rightarrow$ 2010s BiLSTM-CRF $\rightarrow$ 2018 BERT $\rightarrow$ 2023+ Generative LLMs across 4 Understanding tasks and 4 Generation tasks.
- **PDF pp. 54–57 (Slides 52–55) — The 4 Core Clinical Information Extraction Tasks**:
  1. **Task 1: Named Entity Recognition (NER)** (p. 54) — Extracting problem, test, treatment, and anatomy spans via schema-constrained JSON prompts.
  2. **Task 2: Concept Normalisation / Entity Linking** (p. 55) — **Retrieve-then-Rerank pattern**: Extract span $\rightarrow$ Expand abbreviations $\rightarrow$ Retrieve top-K candidates from UMLS/SNOMED via lexical + `SapBERT` vector search $\rightarrow$ LLM selects best candidate. *(Golden Rule: Never ask an LLM to generate SNOMED/ICD codes from memory!)*
  3. **Task 3: Polarity / Assertion Status** (p. 56) — Classifying mentions as `PRESENT`, `ABSENT` (negated — ~40% of clinical mentions), `POSSIBLE`, `CONDITIONAL`, `HYPOTHETICAL`, `FAMILY_HISTORY`, or `HISTORICAL`.
  4. **Task 4: Temporality** (p. 57) — Resolving relative expressions (`"3 months ago"`) against document anchor date $t_0$ into ISO-8601 dates and `BEFORE / OVERLAP / AFTER` timeline relations.
- **PDF pp. 58–59 (Slides 56–57) — Adaptation Ladder, Evaluation & Clinical Risks**:
  - Prompting $\rightarrow$ Few-shot $\rightarrow$ Constrained decoding $\rightarrow$ LoRA fine-tuning $\rightarrow$ Distilling a fast on-prem encoder.
  - Gold-standard annotation protocol (**dual clinician annotation + Cohen's $\kappa > 0.80$**), stratified evaluation, and mitigating hallucinations, bias, privacy (on-prem open-weights models), and regulatory constraints.

#### Block 05: Medical RAG (PDF pp. 60–65 / Slides 58–63)
- **PDF pp. 61–62 (Slides 59–60) — Document RAG Architecture**: Chunking clinical guidelines / SmPC drug labels / PubMed articles, hybrid dense (`BioLORD`) + sparse (`BM25`) retrieval, cross-encoder re-ranking, and inline sentence-level citations.
- **PDF pp. 63–64 (Slides 61–62) — Real-World-Evidence (RWE) RAG over OMOP CDM**:
  - Using an LLM agent with **Model Context Protocol (MCP) tools** (`search_concept`, `build_cohort`, `execute_aggregate_sql`) to translate a clinician's natural-language question into validated SQL over OMOP tables (`PERSON`, `CONDITION_OCCURRENCE`, `DRUG_EXPOSURE`, `MEASUREMENT`, `NOTE_NLP`, `CONCEPT_ANCESTOR`), returning only privacy-safe cohort aggregates ($N \ge 10$).
- **PDF p. 65 (Slide 63) — Decision Matrix**: When to choose **Document RAG** vs **RWE (OMOP) RAG** vs **LoRA Fine-Tuning**.

#### Block 06: Practical Cases — OMOP with ELADAIS & Clinical NLP to `NOTE_NLP` (PDF pp. 66–83 / Slides 64–78)
- **PDF pp. 67–76 (Slides 65–72) — Case A: OMOP CDM & The ELADAIS Platform (CTB-UPM)**:
  - **OMOP Common Data Model (pp. 69–71)**: Patient-centric star schema around `PERSON`, standardized clinical tables, standardized vocabularies, and the **OHDSI ecosystem** (`ATLAS`, `Achilles`, `DataQualityDashboard / DQD`, `HADES`).
  - **ELADAIS Architecture (pp. 72–74)**: 5-stage regulated ETL pipeline enforcing 5 integrity rules, 100% bidirectional lineage (`trace_id`), idempotency, semantic mapping, and >3,300 automated DQD checks.
  - **Federated Learning / Federated Analysis (pp. 75–76)**: *"The code travels to the data; patient data never leaves the hospital"* — illustrated with a real 15,000-patient multicentre HIV cohort study across 3 Madrid hospitals.
- **PDF pp. 77–81 (Slides 73–77) — Case B: End-to-End Clinical Note Extraction into OMOP `NOTE_NLP`**:
  - Step-by-step walkthrough transforming an unstructured oncology note (`"IDC grade 3, ER+ 90%, PR+ 70%, HER2-, no distant metastases"`) into standardized `NOTE_NLP` rows (`note_nlp_concept_id`, `lexical_variant`, `term_exists='Y'/'N'`, `term_temporal`, `term_modifiers`) and running a unified SQL query joining `CONDITION_OCCURRENCE`, `MEASUREMENT`, and `NOTE_NLP`.
- **PDF p. 82 (Slide 78) — Seven Takeaways for Healthcare Data Science**.

---

### Deck 9 & Project Files: Team Project & WP1 (NY SPARCS Early Discharge Planning)

1. **[Dataset_Proposal_SPARCS.pdf](file:///Users/luigizheng/Desktop/data analysis/project/Dataset_Proposal_SPARCS.pdf) (1 Page)**:
   - **Dataset**: New York State SPARCS Hospital Inpatient Discharges (de-identified public use file, ~2.1M discharges/year, 34 columns).
   - **Decision & Owner**: Director of Patient Flow & Head of Case Management — deciding at admission (Day 1) which patients receive proactive multidisciplinary discharge planning.
   - **Primary KPI**: Excess bed-days per 100 admissions (days above the 75th percentile LOS for the same `APR-DRG × APR Severity of Illness` cell).

2. **[SPARCS_Data_Extract_Scope_and_Rationale_WP1.pdf](file:///Users/luigizheng/Desktop/data analysis/WP1/SPARCS_Data_Extract_Scope_and_Rationale_WP1.pdf) (10 Pages)**:
   - **Pages 1–2**: Schema-first Socrata API extraction design; temporal split rationale (**2017** = fixed pre-COVID P75 benchmark ruler & training anchor; **2018–2019** = temporal validation; **2020–2022** = excluded due to COVID distortion; **2023** = current WP1 baseline & test cohort).
   - **Pages 3–4**: Geographic scope across NY's 8 Health Service Areas, selecting **Finger Lakes (17 hospitals, ~117k adult stays/yr)** as the primary health system for the Board Business Case.
   - **Pages 4–5**: Cohort inclusion/exclusion funnel (filtering out newborn/obstetric MDC 14/15, deaths, left against medical advice, rehabilitative/psychiatric DRGs, and extreme administrative outliers).
   - **Pages 5–7**: Column classification into **Admission-Known Features** (safe for Day 1 prediction: age group, admission type, ED indicator, CCSR diagnosis, APR-DRG, severity/mortality subclasses, payer) vs **Discharge-Only / Target Variables** (strictly excluded from Day 1 predictors to prevent data leakage: `Length of Stay`, `Patient Disposition`, `Total Costs`, `Total Charges`, `CCS Procedure`).
   - **Pages 7–10**: Output Parquet/CSV files generated by [download_sparcs.py](file:///Users/luigizheng/Desktop/data analysis/WP1/download_sparcs.py), known public-data limitations (censored `120+` LOS, lack of patient longitudinal ID, APR-DRG grouping timing), and references.

3. **[WP1 – Early Discharge Planning Business Case.pptx](file:///Users/luigizheng/Desktop/data analysis/WP1/WP1%20%E2%80%93%20Early%20Discharge%20Planning%20Business%20Case.pptx) (10 Slides)**:
   - **Slide 1**: Title — *Earlier planning, more free beds* (Finger Lakes Health System, 17 hospitals, Rochester, NY).
   - **Slide 2**: Case & Context — DRG fixed payment per admission means every excess bed-day earns \$0 while costing nursing/drugs and blocking ED/surgical admissions.
   - **Slide 3**: The Operational Decision — Shift from reactive case management to a **Day-1 ranked worklist at admission**.
   - **Slide 4**: KPI & 2023 Baseline — **192.8 excess bed-days per 100 admissions** (`24.4%` of stays prolonged above the 2017 APR-DRG × Severity P75 benchmark).
   - **Slide 5**: Executive EDA (Trend) — Excess bed-days grew **+78% from 2017 to 2023**, the steepest deterioration in New York State.
   - **Slide 6**: Executive EDA (Bottleneck) — **3 in 4 excess bed-days (74%)** occur in patients awaiting post-acute placement (Skilled Nursing Facility / Home Health Care).
   - **Slide 7**: Executive EDA (Day-1 Signal) — Admission-known features (Severity 3–4, Emergency admission, Medicare/Medicaid, older age) already separate high-risk stays on Day 1.
   - **Slide 8**: Expected Financial Value — **\$17.5M net annual value** (combining \$375 variable cash cost saved per avoided bed-day + backfill contribution margin from unlocking blocked surgical/ED capacity, minus case-management program costs).
   - **Slide 9**: Data Sources & Hypotheses — Public NY SPARCS (`6.2M` adult stays) proves the business case; production deployment in WP2 connects to the hospital EHR (HL7 ADT/FHIR).
   - **Slide 10**: Decision Delivery & Lifecycle — Overnight batch scoring from EHR intake $\rightarrow$ 07:00 ranked worklist in the Case Management EHR module, tracked monthly against the excess bed-day KPI.
