# Standard data manipulation and analysis
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Statistical analysis
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Text analysis
import re
from collections import Counter

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
plt.style.use('seaborn-v0_8')

# Load pickled datasets
df = pd.read_pickle('data/processed/cleaned_call_script_data.pkl') # Main dataset, not including February data
df_volt = pd.read_pickle('data/filtered/data_volt.pkl') 
df_non_volt = pd.read_pickle('data/filtered/data_non_volt.pkl')
df_treatment = pd.read_pickle('data/filtered/data_treatment.pkl')
df_control = pd.read_pickle('data/filtered/data_control.pkl')

print(f"Main dataset loaded: {df.shape}")
print(f"VOLT customers: {df_volt.shape[0]}")
print(f"Non-VOLT customers: {df_non_volt.shape[0]}")
print(f"Treatment group: {df_treatment.shape[0]}")
print(f"Control group: {df_control.shape[0]}")