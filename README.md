# PSSA Database Analysis: Examining the Relationship Between School Funding, Class Sizes, and Student Success

This project investigates the relationship between school funding, class sizes, and student success using various datasets. The analysis is implemented using Django, with Python and Pandas handling data manipulation and statistical analysis.

## Table of Contents
- [Research Question](#research-question)
- [Datasets Used](#datasets-used)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis](#analysis)
- [Contributing](#contributing)
- [License](#license)

## Research Question

- Is school size correlated to school performance?
- Is socioeconomic status correlated with school performance?
- What is the relationship between school size, student socioeconomic status, and school performance?

## Datasets Used

1. **School Fast Facts:** Used to determine schools and regions of interest.
2. **District Fast Facts:** Used to determine districts and regions of interest.
3. **Low Income Data for Public Schools:** Percentage of economically disadvantaged students per school and the number of students per school.
4. **PSSA Exam:** Percentage proficient in English, math, and science.
5. **Keystone Exam:** Percentage proficient in algebra, literature, and biology.

## Database Schema

- **School:** Contains attributes such as school name, school number, AUN (Administrative Unit Number), and school type (high school, middle school, elementary school).
- **District:** Contains attributes such as district name, county ID, and AUN.
- **County:** Contains the county ID.
- **Enrollment:** Contains attributes like year, number of students, number of low-income students, and percentage of low-income students.
- **Keystone Exam:** Contains attributes related to student proficiency percentages in literature, algebra, and biology.
- **PSSA Exam:** Contains attributes related to student proficiency percentages in English, science, and math.

## Usage

To use the application, follow these steps:

### Access the web application:

1. Open a web browser and go to `http://127.0.0.1:8000`.

### Navigate through the pages:

- Use the homepage to explore the data.
- Use the analysis pages to view statistical results and visualizations.
- Utilize the interactive elements to filter and visualize the data dynamically.

## Analysis

The project includes the following analyses:

- **Hypothesis Testing:** To determine if there is a statistically significant relationship between school performance and factors like enrollment size and socioeconomic status.
- **Regression Analysis:** To quantify the relationship between the dependent variable (school performance) and independent variables (enrollment size and socioeconomic status).
- **Data Visualization:** Using Chart.js and jQuery for interactive graphs and charts.



