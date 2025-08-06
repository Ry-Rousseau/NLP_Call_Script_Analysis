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
| MONTH | Date when the survey response was collected |
| CONNECTION_TIME | Customer satisfaction rating for connection time (scale 0-10) |
| SALES_PERSON_SAT | Customer satisfaction rating for sales person interaction (scale 0-10) |
| SALES_FRIENDLY_SAT | Customer satisfaction rating for sales person friendliness (scale 0-10) |
| COMMINICATION_SAT | Customer satisfaction rating for communication quality (scale 0-10) |
| FIRST_BILL_SAT | Customer satisfaction rating for first bill experience (scale 0-10) |
| AGENT_KNOWLEDGE | Customer satisfaction rating for agent knowledge (scale 0-10) |
| VOLT_FLAG_BINARY | Binary encoding of VOLT_FLAG where 1 = 'yes' (has Volt package), 0 = no Volt package |
| TREATMENT_BINARY | Binary encoding of GROUP where 1 = 'pilot' (treatment group), 0 = 'control' group |
| LTR_COMMENT_CLEAN | Preprocessed version of LTR_COMMENT with encoding issues fixed, very short/non-informative responses removed, and normalized spacing |
| SENTIMENT_SCORE | Google Cloud Natural Language API sentiment score ranging from -1.0 (negative) to 1.0 (positive), indicating overall emotional leaning of the text |
| SENTIMENT_MAGNITUDE | Google Cloud Natural Language API sentiment magnitude from 0.0 to +inf, indicating overall strength of emotion regardless of polarity |
| topics_assigned | List of specific topic IDs assigned to each comment through BERTopic and rule-based classification (e.g., ['1_customer_service_good_excellent']) |
| substantive_topics | List of human-readable topic labels corresponding to topics_assigned (e.g., ['Overall Customer Service Quality']) |
| num_topics_assigned | Integer count of how many topics were assigned to each comment, ranging from 0 to multiple topics |

## Data Types and Summary Statistics

### Dataset Overview
- **Total observations**: 582 entries
- **Total variables**: 21 columns (original 15 + 6 derived variables)

### Data Types
- **Object (text)**: 8 variables (GROUP, VOLT_FLAG, SURVEY_ID, LTR_COMMENT, PRIMARY_REASON, LTR_COMMENT_CLEAN, topics_assigned, substantive_topics)
- **Integer**: 4 variables (SCORE, VOLT_FLAG_BINARY, TREATMENT_BINARY, num_topics_assigned)
- **Float**: 8 variables (satisfaction ratings, SENTIMENT_SCORE, SENTIMENT_MAGNITUDE)
- **Datetime**: 1 variable (MONTH)

### Missing Values by Variable
- **GROUP**: 0 missing (100% complete)
- **VOLT_FLAG**: 341 missing (41.4% complete)
- **SURVEY_ID**: 0 missing (100% complete)
- **SCORE**: 0 missing (100% complete)
- **LTR_COMMENT**: 152 missing (73.9% complete)
- **LTR_COMMENT_CLEAN**: 152 missing (73.9% complete) - matches LTR_COMMENT after preprocessing
- **PRIMARY_REASON**: 256 missing (56.0% complete)
- **MONTH**: 0 missing (100% complete)
- **CONNECTION_TIME**: 17 missing (97.1% complete)
- **SALES_PERSON_SAT**: 48 missing (91.7% complete)
- **SALES_FRIENDLY_SAT**: 24 missing (95.9% complete)
- **COMMINICATION_SAT**: 20 missing (96.6% complete)
- **FIRST_BILL_SAT**: 20 missing (96.6% complete)
- **AGENT_KNOWLEDGE**: 14 missing (97.6% complete)
- **VOLT_FLAG_BINARY**: 0 missing (100% complete)
- **TREATMENT_BINARY**: 0 missing (100% complete)
- **SENTIMENT_SCORE**: 152 missing (73.9% complete) - only calculated for non-missing comments
- **SENTIMENT_MAGNITUDE**: 152 missing (73.9% complete) - only calculated for non-missing comments
- **topics_assigned**: 0 missing (100% complete) - empty lists for comments without topics
- **substantive_topics**: 0 missing (100% complete) - empty lists for comments without topics
- **num_topics_assigned**: 0 missing (100% complete) - defaults to 0 for comments without topics

### Key Variable Ranges and Statistics

#### SCORE (Net Promoter Score)
- **Range**: 0-10
- **Mean**: 8.20
- **Standard Deviation**: 3.03
- **Distribution**: 25th percentile = 8, 50th percentile = 10, 75th percentile = 10

#### Satisfaction Ratings (0-10 scale)
- **CONNECTION_TIME**: Mean = 8.56, SD = 2.69, Range = 0-10
- **SALES_PERSON_SAT**: Mean = 7.96, SD = 3.81, Range = 0-10
- **SALES_FRIENDLY_SAT**: Mean = 8.13, SD = 2.88, Range = 0-10
- **COMMINICATION_SAT**: Mean = 8.58, SD = 2.64, Range = 0-10
- **FIRST_BILL_SAT**: Mean = 8.84, SD = 2.40, Range = 0-10
- **AGENT_KNOWLEDGE**: Mean = 8.25, SD = 2.68, Range = 0-10

#### Binary Variables
- **VOLT_FLAG_BINARY**: 241 customers with Volt packages (41.4%), 341 without (58.6%)
- **TREATMENT_BINARY**: Pilot and control group distribution maintained proportionally

#### Date Range
- **Survey Period**: March 2023 to June 2023 (4 months, February data removed)

#### Sentiment Analysis Variables
- **SENTIMENT_SCORE**: Mean = 0.52, SD = 0.54, Range = -0.70 to 0.90
- **SENTIMENT_MAGNITUDE**: Mean = 1.18, SD = 0.95, Range = 0.0 to 3.5

#### Topic Modeling Variables
- **num_topics_assigned**: Mean = 0.74, Range = 0-3 topics per comment
- **Topic Coverage**: Approximately 43% of comments assigned at least one topic
- **Most Common Topics**: Overall Customer Service Quality, Staff Helpfulness and Communication, Professional Service Standards

### Notes
- All satisfaction ratings use a 0-10 scale where higher scores indicate better satisfaction
- The VOLT_FLAG missing values represent customers without Volt packages
- PRIMARY_REASON contains comma-separated categorical tags for customer feedback themes
- Survey responses span the experimental period testing new call scripts against control scripts
- February 2023 data has been removed from the dataset for analysis purposes
- Sentiment analysis performed using Google Cloud Natural Language API
- Topic modeling performed using BERTopic with custom rule-based classification
- LTR_COMMENT_CLEAN removes very short responses, fixes encoding issues, and normalizes spacing