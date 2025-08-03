# NLP Call Script Analysis - Data Codebook

## Variable Descriptions

| Variable Name | Description |
|---------------|-------------|
| GROUP | Experimental group assignment indicating whether the customer was assigned to the control group or pilot group testing new call scripts |
| VOLT_FLAG | Categorical indicator showing whether the customer has a Volt package (bundled broadband and mobile service) |
| SURVEY_ID | Unique identifier for each customer survey response |
| SCORE | Net Promoter Score (NPS) - customer likelihood to recommend the service on a scale of 0-10, overall feedback rating |
| LTR_COMMENT | Open-text customer feedback explaining their likelihood to recommend score |
| PRIMARY_REASON |  The main reason/reasons a customer contacted the business, as identified by the caller |
| DATE | Date when the survey response was collected |
| CONNECTION_TIME | Customer satisfaction rating for connection time (scale 0-10) |
| SALES_PERSON_SAT | Customer satisfaction rating for sales person interaction (scale 0-10) |
| SALES_FRIENDLY_SAT | Customer satisfaction rating for sales person friendliness (scale 0-10) |
| COMMINICATION_SAT | Customer satisfaction rating for communication quality (scale 0-10) |
| FIRST_BILL_SAT | Customer satisfaction rating for first bill experience (scale 0-10) |
| AGENT_KNOWLEDGE | Customer satisfaction rating for agent knowledge (scale 0-10) |
| VOLT_FLAG_BINARY | Binary encoding of VOLT_FLAG where 1 = 'yes' (has Volt package), 0 = no Volt package |
| TREATMENT_BINARY | Binary encoding of GROUP where 1 = 'pilot' (treatment group), 0 = 'control' group |

## Data Types and Summary Statistics

### Dataset Overview
- **Total observations**: 647 entries (380 control, 267 pilot)
- **Total variables**: 15 columns

### Data Types
- **Object (text)**: 5 variables (GROUP, VOLT_FLAG, SURVEY_ID, LTR_COMMENT, PRIMARY_REASON)
- **Integer**: 3 variables (SCORE, VOLT_FLAG_BINARY, TREATMENT_BINARY)
- **Integer**: 6 variables (satisfaction ratings)
- **Datetime**: 1 variable (DATE)

### Missing Values by Variable
- **GROUP**: 0 missing (100% complete)
- **VOLT_FLAG**: 368 missing (43.1% complete)
- **SURVEY_ID**: 0 missing (100% complete)
- **SCORE**: 0 missing (100% complete)
- **LTR_COMMENT**: 165 missing (74.5% complete)
- **PRIMARY_REASON**: 286 missing (55.8% complete)
- **DATE**: 0 missing (100% complete)
- **CONNECTION_TIME**: 20 missing (96.9% complete)
- **SALES_PERSON_SAT**: 55 missing (91.5% complete)
- **SALES_FRIENDLY_SAT**: 30 missing (95.4% complete)
- **COMMINICATION_SAT**: 23 missing (96.4% complete)
- **FIRST_BILL_SAT**: 23 missing (96.4% complete)
- **AGENT_KNOWLEDGE**: 17 missing (97.4% complete)
- **VOLT_FLAG_BINARY**: 0 missing (100% complete)
- **TREATMENT_BINARY**: 0 missing (100% complete)

### Key Variable Ranges and Statistics

#### SCORE (Net Promoter Score)
- **Range**: 0-10
- **Mean**: 8.16
- **Standard Deviation**: 3.06
- **Distribution**: 25th percentile = 8, 50th percentile = 10, 75th percentile = 10

#### Satisfaction Ratings (0-10 scale)
- **CONNECTION_TIME**: Mean = 8.56, SD = 2.69, Range = 0-10
- **SALES_PERSON_SAT**: Mean = 7.89, SD = 3.85, Range = 0-10
- **SALES_FRIENDLY_SAT**: Mean = 8.14, SD = 2.85, Range = 0-10
- **COMMINICATION_SAT**: Mean = 8.59, SD = 2.62, Range = 0-10
- **FIRST_BILL_SAT**: Mean = 8.83, SD = 2.39, Range = 0-10
- **AGENT_KNOWLEDGE**: Mean = 8.26, SD = 2.66, Range = 0-10

#### Binary Variables
- **VOLT_FLAG_BINARY**: 279 customers with Volt packages (43.1%), 368 without (56.9%)
- **TREATMENT_BINARY**: 267 in pilot group (41.3%), 380 in control group (58.7%)

#### Date Range
- **Survey Period**: February, 2023 to June, 2023 (5 months)

### Notes
- All satisfaction ratings use a 0-10 scale where higher scores indicate better satisfaction
- The VOLT_FLAG missing values represent customers without Volt packages
- PRIMARY_REASON contains comma-separated categorical tags for customer feedback themes
- Survey responses span the experimental period testing new call scripts against control scripts