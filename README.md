# West Java Poverty Analysis Dashboard

Interactive data analysis and visualization of poverty levels across districts in **West Java, Indonesia (2019–2023)**.

This project demonstrates **data cleaning, exploratory data analysis, and dashboard development** using Python, Power BI, and Streamlit.

---

## Live Interactive Dashboard

Access the deployed Streamlit dashboard here:

**Live App:**
https://kemiskinan-jabar-dashboard.streamlit.app/

This interactive dashboard allows users to:

* Explore poverty trends from 2019–2023
* Compare poverty levels between districts
* Visualize geographic distribution across West Java

---

## Project Overview

The objective of this project is to analyze poverty trends across districts and cities in West Java using open government data.

Key analysis includes:

* Poverty trend over time
* Regional comparison between districts
* Identifying areas with the highest poverty levels
* Geographic visualization using map data

---

## Data Source

Dataset obtained from **Open Data Jawa Barat**.

The dataset includes:

* Poverty percentage by district/city
* Number of poor residents
* Yearly records from **2019 to 2023**

---

## Tools & Technologies

* Python
* Pandas
* Plotly
* Streamlit
* Power BI
* GeoJSON
* Jupyter Notebook

---

## Project Workflow

### 1. Data Collection

Datasets were downloaded from Open Data Jawa Barat and stored as CSV files.

### 2. Data Cleaning

Data preprocessing steps include:

* Handling missing values
* Standardizing column names
* Merging multiple yearly datasets
* Creating a clean dataset for analysis

Notebook file:
`project_kemiskinan.ipynb`

---

### 3. Exploratory Data Analysis

Exploratory analysis was conducted to understand:

* Yearly poverty trends
* Regional disparities
* Distribution of poverty rates across districts

---

### 4. Power BI Dashboard

A business-style dashboard was created using Power BI to visualize:

* Poverty trend (2019–2023)
* Average poverty percentage
* Regional comparison
* Geographic distribution across West Java

Dashboard file:
`project-kemiskinan jabar.pbix`

Example:

![Power BI Dashboard](dashboard%20power%20BI.png)

---

### 5. Interactive Web Dashboard

An interactive web dashboard was built using Streamlit.

Run locally:

pip install -r requirements.txt

streamlit run app.py

---

## Repository Structure

```
app.py
project_kemiskinan.ipynb
project-kemiskinan jabar.pbix
kemiskinan_clean.csv
kemiskinan_2019.csv
kemiskinan_2020.csv
kemiskinan_2021.csv
kemiskinan_2022.csv
kemiskinan_2023.csv
jabar_kabupaten.geojson
dashboard power BI.png
requirements.txt
```

---

## Key Insights

* Poverty rates fluctuated between **2019 and 2023**
* Several districts consistently show higher poverty percentages
* Geographic disparities exist across West Java regions

---

## Author

**rafly irsa sanubari**

Computer Science Graduate
Aspiring Data Analyst / Data Scientist

GitHub:
https://github.com/Raflytaks12
