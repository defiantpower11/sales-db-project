
# sales-db-project

Sales data analysis project using Python and SQL, focused on reporting and relational database design.

This project demonstrates how to design a relational database, populate it with sample sales data, and generate analytical reports using SQL views and Python. It simulates a real-world workflow between a PostgreSQL database and a data analysis layer.

## Tech Stack
 Python
 PostgreSQL
 SQL (DDL, DML, Views)
 pandas
 SQLAlchemy
 Git & GitHub

## Project Structure
sales-db-project/
├── python/
│   └── sales_analysis.py
├── sql/
│   ├── schema.sql
│   ├── data.sql
│   └── views.sql
├── output/
│   └── sales_report.csv
├── README.md
├── .gitignore
└── requirements.txt

## How to Run
1. Create and activate a virtual environment  
   python -m venv venv  
   venv\Scripts\activate  

2. Install dependencies  
   pip install -r requirements.txt  

3. Run SQL scripts in PostgreSQL (in order)  
    schema.sql  
    data.sql  
    views.sql  

4. Run the Python analysis  
   python python/sales_analysis.py  

The script generates a CSV report in the output folder.

## Output
 sales_report.csv: total amount spent per customer.

## Skills Demonstrated
 Relational database design
 SQL joins and views
 Python data analysis with pandas
 Database connectivity using SQLAlchemy
 Version control with Git
