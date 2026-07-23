# Predicting Developer Salaries

An end-to-end data science project investigating the relative importance of formal education, professional experience, and technical specialization in predicting developer salaries.

The analysis uses responses from the **2025 Stack Overflow Developer Survey** and follows a structured data science workflow from exploratory data analysis to predictive modeling.

---

## Research Question

> **What is the relative importance of formal education, experience, and professional specialization in predicting developer salaries?**

---

## Objectives

- Investigate factors associated with developer salaries.
- Evaluate the predictive value of formal education.
- Compare the influence of professional experience and coding experience.
- Assess whether technical specialization explains salary differences.
- Build an interpretable machine learning model for salary prediction.

---

## Dataset

**Source**

- Stack Overflow Developer Survey 2025

The dataset contains responses from developers worldwide covering:

- Education
- Employment
- Developer roles
- Professional experience
- Compensation
- Technology usage
- Industry
- Demographics

---

## Methodology

The project follows the CRISP-DM framework.

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Exploratory Data Analysis
5. Feature Engineering
6. Model Development
7. Model Evaluation
8. Interpretation

---


# Study Population

This analysis was restricted to respondents who identified themselves as developers by profession, as the objective of the study is to identify factors associated with developer salaries. Respondents who coded only as part of another profession, were learning to code, coded as a hobby, or no longer worked as professional developers were excluded from the analysis.

---

## Project Structure

```text
developer-salary-predictors/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_exploratory_data_analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── visualization.py
│   └── utils.py
│
├── figures/
│
├── requirements.txt
│
└── README.md
```

---

## Features Used

Current variables include:

- `MainBranch`
- `Age`
- `EdLevel`
- `Employment`
- `WorkExp`
- `YearsCode`
- `DevType`
- `Industry`
- `ToolCountWork`
- `ToolCountPersonal`

### Target Variable

- `ConvertedCompYearly`

---

## Current Progress

- [x] Research question defined
- [x] Dataset review
- [x] Feature selection
- [x] Univariate exploratory data analysis
- [ ] Data cleaning
- [ ] Bivariate analysis
- [ ] Feature engineering
- [ ] Modeling
- [ ] Evaluation
- [ ] Final report

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
