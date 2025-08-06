# NLP Call Script Analysis

This project analyzes customer feedback from a telecommunications company's experimental study testing new call scripts against control scripts as a field experiemtn. The analysis examines how the new treatment script affect customer sentiment, satisfaction, and the topics customers discuss in their feedback. It was centered around the aim of simplifying decisions, building trust, and reducing decision regret.

## Research Questions

1. How do customers define 'good' service, and how does the new script shift those definitions?
2. What aspects of service (clarity, empathy, agent personality) drive variance in sentiment?
3. Does the new script systematically change perceptions or emotional tone, particularly for high-value segments like VOLT customers?

## Analysis Pipeline

The analysis follows a structured pipeline across five Jupyter notebooks:

### 1. Data Preprocessing (`data_preprocessing.ipynb`)
- Merges control and pilot datasets from Excel source
- Handles missing values and data type conversions
- Creates binary treatment and VOLT flag variables
- Removes February 2023 data for analysis consistency
- Outputs: `cleaned_call_script_data.csv` and `.pkl`

### 2. Comment Preprocessing (`comment_preprocessing.ipynb`)
- Cleans customer feedback text for NLP analysis
- Fixes character encoding issues and Unicode artifacts
- Removes non-informative responses and normalizes spacing
- Preserves emotional content and natural language patterns
- Outputs: Enhanced dataset with `LTR_COMMENT_CLEAN` variable

### 3. Sentiment Analysis (`sentiment_analysis_modelling.ipynb`)
- Applies Google Cloud Natural Language API for sentiment scoring
- Generates sentiment scores (-1.0 to 1.0) and magnitude measures (0.0+)
- Analyzes sentiment distribution by treatment group and VOLT status
- Outputs: `data_with_sentiment.pkl` with sentiment variables

### 4. Topic Modeling (`topic_theme_modelling.ipynb`)
- Implements BERTopic for unsupervised topic extraction
- Applies rule-based classification for substantive topic categorization
- Identifies key themes: customer service quality, agent performance, technical issues
- Analyzes topic distribution differences between treatment groups
- Outputs: Final dataset with topic assignments and counts

### 5. Modeling and Interpretation (`modelling_and_interpretation.ipynb`)
- Statistical analysis of treatment effects on sentiment and satisfaction
- Segmented analysis by VOLT status and other customer characteristics
- Visualization of key findings and effect sizes
- Interpretation of business implications

## Methods

**Sentiment Analysis**: Google Cloud Natural Language API provides robust sentiment scoring that handles informal language, typos, and emotional expressions common in customer feedback.

**Topic Modeling**: BERTopic leverages transformer-based embeddings to identify semantic similarity between customer comments, supplemented by rule-based classification for business-relevant topic categorization.

**Statistical Analysis**: Comparative analysis between treatment and control groups using appropriate statistical tests, with segmentation by customer value (VOLT status) and other relevant characteristics.

## Data

The final dataset (`data_with_sentiment_and_topics.csv`) contains 582 customer survey responses from March-June 2023, with 21 variables including original survey data, derived binary flags, cleaned text, sentiment scores, and topic assignments.

## Key Findings

Results and interpretation are detailed in the modeling and interpretation notebook, focusing on treatment effects on customer perceptions and the differential impact on high-value customer segments.