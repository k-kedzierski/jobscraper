---
title: "Machine Learning Engineering - a look at the Polish job market in 2024"
author: Adrian Kastrau, Kacper Kędzierski
date: "February 14, 2024"
output:
  html_document:
    number_sections: true
  rmarkdown::pdf_document:
    fig_caption: yes
    includes:  
      in_header: figure_placement.tex
---

# Introduction

The goal of this report is to provide an overview of the job market for machine learning engineers in 2024. We will take a look at the current state of the job market, by analyzing the job postings on popular job board: No Fluff Jobs. We will be looking at positions in Poland that not only match the title of "machine learning engineer", but also those that require a set of common technical skills - such as Python, Cloud technologies, Kubernetes and data engineering.

Due to the different expertise level of the authors and different hypotheses, the analysis have been split into two parts, based on the seniority level of the job postings. The first part will be focused on the mid-level positions, while the second part will be focused on the senior-level positions. 

Moreover, the analysis has been performed separately for contract of employment and B2B job postings.

# Data

The data was collected by scraping the No Fluff Jobs website. We have collected the job postings for two different keywords: **"machine learning engineer"** and **"data engineer"**. The data was collected on January 12, 2024.

We have also collected the job postings for the "data engineer" position, as we believe that the skills required for this position are often overlapping with the skills required for a machine learning engineer. Furthermore, the definition of "machine learning engineer" is also conventional.

## Cleaning the data

Having considered the discrepancies, additional data cleaning was necessary. This process is quite likely the most **time-consuming** and **biased** part of the analysis - afterwards we want the sample to match as closely as possible author's expected skills while also being responsibilities of a machine learning engineer.

In general, we focused on the following key factors:

- **Python**: The primary programming language must have been Python.
- **Data processing**: The job must have included data processing responsibilities and include popular big data processing stack or data platform vendor that is either the Snowflake itself or its direct or close competitor - such as Databricks, AWS (Redshift), GCP (Bigquery), Azure, or other popular big data processing frameworks that are cloud-agnostic, such as Apache Spark, Apache Flink, Apache Beam, or Apache Kafka.

Other factors were also considered:

- **Kubernetes**: We included job postings that require Kubernetes, as both of the authors closely associate this technology with the machine learning engineering role.
- **Cloud**: We included job postings that require experience with cloud technologies, such as AWS, GCP, or Azure.
- **CI/CD**: We included job postings that mention CI/CD,
- **MLOps**: We included job postings that mention MLOps or related technologies, such as MLflow, Kubeflow, or TFX.

It is mostly, however, the common sense and combination of the above factors that were used to filter the job postings.

On the other hand, we tried to separate Data Science from Machine Learning Engineering. We did not include job postings that were focused solely on machine learning or deep learning, and included only the technologies such as TensorFlow, PyTorch, or Keras.

Many of the job postings have been carefully reviewed and scanned manually to ensure that they match the criteria.

Final filtered dataset consisted of 75 job postings. Both unfiltered and filtered datasets are available in the source repository.

\pagebreak

# Results

![Boxplot of the salaries for mid and senior level positions](./docs/plots/salaries_seniority_agg.png)

Presented on the boxplot are salaries for mid and senior level positions, all together for both contract of employment and B2B job postings.

\pagebreak

## Mid-level positions

### Contract of employment

|       | Lower bound | Upper bound | Median salary |
|-------|-------------|-------------|---------------|
| Count |       14.00 |       14.00 |         14.00 |
| Mean  |    13744.86 |    20241.71 |      16993.29 |
| St. dev |    3880.07 |     5660.79 |       4670.39 |
| Min   |     8000.00 |    15000.00 |      11500.00 |
| 25%   |    12300.00 |    17000.00 |      14950.00 |
| 50%   |    13000.00 |    17685.50 |      15125.00 |
| 75%   |    15750.00 |    22750.00 |      19250.00 |
| Max   |    23389.00 |    33413.00 |      28401.00 |

Considering the range and interval-like nature of the salary data, descriptive statistics are presented for lower and upper bounds, as well as median salary (often refered as *expected value* in literature), where median salary is calculated as the average of lower and upper bounds for each job posting.

There are 14 mid-level job postings for contract of employment total. The "median" salary range is between 13 000 and 17 685 PLN, with the actual median salary being 15 125 PLN.

\pagebreak

![Boxplot of the salaries for mid-level positions](./docs/plots/boxplot_mid_uop.png)

Boxplot of the salaries for mid-level positions is presented above. The boxplot shows the distribution of the salaries for mid-level positions. The median salary is represented by the line inside the box, while the box itself represents the interquartile range (IQR). The whiskers represent the range of the data, excluding the outliers.

\pagebreak

![Salary ranges (lower and upper bounds) for mid-level positions](./docs/plots/ranges_mid_uop.png)

The plot above shows the salary ranges (lower and upper bounds) for mid-level positions. The lower bound is the minimum salary, while the upper bound is the maximum salary for a given job posting.

\pagebreak

![Median salaries for mid-level positions](./docs/plots/mediansalaries_mid_uop.png)

The plot above shows the median salaries (expected value of salaries) for mid-level positions. The median salary is calculated as the average of lower and upper bounds for each job posting.

\pagebreak

### B2B

|       | Lower bound | Upper bound | Median salary |
|-------|-------------|-------------|---------------|
| Count |       22.00 |       22.00 |         22.00 |
| Mean  |    17395.64 |    24213.00 |      20804.32 |
| St. dev |    5278.93 |     6101.19 |       5510.87 |
| Min   |     8000.00 |    14000.00 |      11000.00 |
| 25%   |    13958.00 |    19994.00 |      17055.00 |
| 50%   |    15980.00 |    24012.00 |      20076.00 |
| 75%   |    19620.00 |    27510.00 |      23295.00 |
| Max   |    28000.00 |    37000.00 |      32000.00 |

There are 22 mid-level job postings for B2B total. The "median" salary range is between 15 980 and 24 012 PLN, with the actual median salary being 20 076 PLN.

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/boxplot_mid_b2b.png}
    \caption{Boxplot of the salaries for mid-level positions}
\end{figure}

\newpage

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/ranges_mid_b2b.png}
    \caption{Salary ranges (lower and upper bounds) for mid-level positions}
\end{figure}

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/mediansalaries_mid_b2b.png}
    \caption{Median salaries for mid-level positions}
\end{figure}

\pagebreak

## Senior-level positions

### Contract of employment

|       | Lower bound | Upper bound | Median salary |
|-------|-------------|-------------|---------------|
| Count |       20.00 |       20.00 |         20.00 |
| Mean  |    19631.10 |    28046.45 |      23838.78 |
| St. dev |    4967.39 |     8486.39 |       6214.17 |
| Min   |    13500.00 |    19600.00 |      17000.00 |
| 25%   |    15825.00 |    23200.00 |      19650.00 |
| 50%   |    18250.00 |    28000.00 |      23000.00 |
| 75%   |    24000.00 |    28016.75 |      26000.00 |
| Max   |    30000.00 |    60000.00 |      45000.00 |

There are 20 senior-level job postings for contract of employment total. The "median" salary range is between 18 250 and 28 000 PLN, with the actual median salary being 23 000 PLN.

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/boxplot_senior_uop.png}
    \caption{Boxplot of the salaries for senior-level positions}
\end{figure}

\newpage

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/ranges_senior_uop.png}
    \caption{Salary ranges (lower and upper bounds) for senior-level positions}
\end{figure}

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/mediansalaries_senior_uop.png}
    \caption{Median salaries for senior-level positions}
\end{figure}

\pagebreak

### B2B

|       | Lower bound | Upper bound | Median salary |
|-------|-------------|-------------|---------------|
| Count |       37.00 |       37.00 |         37.00 |
| Mean  |    24100.73 |    31467.16 |      27783.95 |
| St. dev |    4387.74 |     5668.24 |       4731.72 |
| Min   |    12950.00 |    18500.00 |      16500.00 |
| 25%   |    21000.00 |    28067.00 |      25200.00 |
| 50%   |    25200.00 |    30240.00 |      28560.00 |
| 75%   |    26880.00 |    33600.00 |      30240.00 |
| Max   |    33000.00 |    47000.00 |      38500.00 |

There are 37 senior-level job postings for B2B total. The "median" salary range is between 25 200 and 30 240 PLN, with the actual median salary being 28 560 PLN.

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/boxplot_senior_b2b.png}
    \caption{Boxplot of the salaries for senior-level positions}
\end{figure}

\newpage

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/ranges_senior_b2b.png}
    \caption{Salary ranges (lower and upper bounds) for senior-level positions}
\end{figure}

\begin{figure}[!htb]
    \centering
    \includegraphics[width=0.8\textwidth]{./docs/plots/mediansalaries_senior_b2b.png}
    \caption{Median salaries for senior-level positions}
\end{figure}

\pagebreak

# Conclusions

There were total of 75 job postings for machine learning engineers in Poland in 2024, where:

- 35 job postings were for contract of employment,
- 59 job postings were for B2B.

The analysis of the job postings for machine learning engineers in Poland in 2024 has shown that:

- The median salary for mid-level positions is between **13 000 and 17 685 PLN** for contract of employment, and between **15 980 and 24 012 PLN** for B2B job postings.
- The median salary for senior-level positions is between **18 250 and 28 000 PLN** for contract of employment, and between **25 200 and 30 240 PLN** for B2B job postings.
