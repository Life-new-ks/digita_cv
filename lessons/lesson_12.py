import streamlit as st

st.title("Lesson 12")

st.subheader(
"""
SQL
"""
)

st.text(
"""
SQL, or Structured Query Language, is used to store, retrieve, update and delete data in relational databases. 
Common SQL commands include `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE TABLE` and `JOIN`. 
SQL can be used with database systems such as MySQL, PostgreSQL, Oracle and SQL Server.
"""
)


st.subheader(
"""
Star Schema vs. Snowflake Schema
"""
)

st.text(
    """
A star schema contains one central fact table connected directly to denormalized dimension tables. It is simple, requires fewer joins and usually provides faster queries, but it can contain more duplicated data. 
A snowflake schema normalizes the dimension tables into smaller related tables, reducing redundancy but increasing query and design complexity.
    """
)


st.subheader(
    """
Database Normalization
"""
)

st.text(
    """
Database normalization is the process of organizing data into related tables to reduce duplication and prevent inconsistent data. Large tables are divided into smaller tables that are connected using primary and foreign keys. This improves data integrity, although highly normalized databases may require more joins when retrieving information.
    """
)

st.subheader(
    """
Slowly Changing Dimensions
"""
)

st.text(
    """
Slowly Changing Dimensions, or SCDs, are techniques used in data warehouses to manage changes in dimension data over time. Type 1 replaces the previous value and does not preserve history, while Type 2 creates a new row for every change and keeps the full history. Type 3 stores the previous value in an additional column, providing only limited historical information.
    """
)


st.subheader(
    """
Normal Forms
"""
)

st.text(
    """
The main normalization levels are First Normal Form, Second Normal Form and Third Normal Form. First Normal Form removes repeating groups and requires atomic values, Second Normal Form removes partial dependencies, and Third Normal Form removes transitive dependencies. More advanced levels include BCNF, 4NF and 5NF, which address more complex data dependencies.
    """
)


st.subheader(
    """
Relationships in SQL
"""
)

st.text(
    """
A one-to-one relationship means that one record is connected to only one record in another table. In a one-to-many relationship, one record can be connected to several records, while each of those records belongs to only one parent. A many-to-many relationship is implemented using an intermediate or junction table containing foreign keys from both related tables.
    """
)


st.subheader(
    """
Data Warehouse vs. Data Lake
"""
)

st.text(
    """
A data warehouse stores cleaned, structured and prepared data that can be used directly for reporting and business intelligence. A data lake stores large amounts of raw structured, semi-structured and unstructured data, usually at a lower cost. Data warehouses use a predefined schema before storing data, while data lakes can apply structure later when the data is needed.
    """
)


st.subheader(
    """
Apache Iceberg: Spark SQL vs. Spark DataFrames
"""
)

st.text(
    """
Spark SQL uses familiar SQL syntax to interact with Apache Iceberg tables and is usually easier to read for complex database operations. Spark DataFrames provide a programmatic API with more flexibility, reusable transformations and better support for interactive data processing. However, DataFrame code may be more verbose and can have a steeper learning curve for people who already know SQL.
    """
)


st.subheader(
    """
DBMS vs. RDBMS
"""
)

st.text(
    """
A DBMS is software used to create, store, manage and retrieve data from a database. An RDBMS is a type of DBMS based on the relational model, where data is stored in tables connected using keys and relationships. RDBMSs generally provide stronger data integrity, structured relationships and support for SQL
examples include MySQL, PostgreSQL, Oracle and SQL Server.
    """
)


st.subheader(
    """
OLAP vs. OLTP
"""
)

st.text(
    """
OLTP, or Online Transaction Processing, handles frequent daily operations such as purchases, payments and account updates. It uses fast and relatively simple read-and -write queries on current, normalized data. OLAP, or Online Analytical Processing, works with large amounts of historical data and complex, read-heavy queries for reporting, analysis and decision-making.
    """
)


st.page_link(
    "4_lessons.py",
    label="Back to Lessons",
    icon="⬅️",
)
