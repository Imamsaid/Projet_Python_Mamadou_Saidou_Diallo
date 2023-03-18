
# **Table des matieres**
[Definition](#duckdb)  
[Whay](#why)   
[Installation](#installation)  
[Serie](#série)
[DataFrame](#dataframe)  
[MultiIndex](#multiindex)  
[Conclusion](#conclusion-)  
[References](#references)  


![test](images/newlogo.PNG)


# Duckdb 
[Duckdb](https://duckdb.org/docs/) is an embedded database management system designed to be used in applications that require high-performance analytical processing. It is written in C++ and can be embedded in Python applications using the DuckDB Python module.  
# **Why:** 
DuckDB is a popular open-source analytical SQL database management system that is gaining popularity in the data science and analytics community. There are several reasons why someone might choose to use DuckDB:  
- Performance: DuckDB is designed to be highly performant and efficient, with a focus on analytical workloads. It has been benchmarked to be significantly faster than other popular database systems for certain types of queries.  
- Lightweight: DuckDB is lightweight and easy to install, making it an ideal choice for developers who want a database that can be quickly set up and used on a local machine.  
- Flexibility: DuckDB supports a wide range of SQL features, including complex queries, subqueries, and window functions, making it well-suited to a variety of use cases.  
- Compatibility: DuckDB is compatible with several popular programming languages, including Python, R, and Julia, which makes it easy to integrate into existing data analysis workflows.  
- Open-Source: DuckDB is an open-source project, which means that it is free to use and users can contribute to its development.  
Overall, DuckDB is a powerful tool for data analysis and management that offers high performance and flexibility, making it an ideal choice for many data scientists and developers.  
# **Installation:**
To use DuckDB in Python, you need to install the DuckDB Python module, which can be done using pip:  
![test](images/install.PNG)

## **Serie,DataFrame,MultiIndex:**  
DuckDB is an embedded SQL OLAP database management system that is designed to be highly efficient and scalable for analytics and data processing tasks. It provides support for storing and manipulating data in the form of Series and DataFrames, which are similar to those in the pandas library.  
## [Série:](https://duckdb.org/docs/dataframe/timeseries)
In DuckDB, a Series is a one-dimensional labeled array that can hold any data type. It can be created by passing a list, tuple, or dictionary to the Series constructor. Series objects can be used for data manipulation, aggregation, and filtering.  
## [DataFrame:](https://duckdb.org/docs/dataframe/introduction.)
A DataFrame is a two-dimensional labeled data structure in DuckDB that consists of rows and columns. It can be created from a variety of data sources, including CSV files, SQL queries, or Python data structures. DataFrames are commonly used for data cleaning, exploration, and analysis.  
## [MultiIndex:](https://duckdb.org/docs/dataframe/introduction.)
A MultiIndex is a way of representing data with multiple levels of indexing in DuckDB. It allows for data to be grouped and aggregated along different dimensions or levels, which can be useful for complex data analysis tasks. MultiIndex can be used with both Series and DataFrame objects.  
To connect DuckDB to Python and create tables, you can use the duckdb Python module.   
**A pratical exemple:**  
# Add a line in the database
![test](images/pratique1.PNG)  
Here's some sample code to get you started:  
![test](images/Caspratique1.PNG)  
In this example, we first created a connection to DuckDB using duckdb.connect(). Then we created a table called example with two columns: integer id and string name. We then added two records to the table using INSERT INTO. Finally, we executed a SQL query to retrieve all the records in the table using SELECT * FROM, and displayed the results.  
Here is an example of code to create a table, insert data and modify it using DuckDB and Python :  
![test](images/insertupdate.PNG)  
In this example, we created a table called example_table with three columns: id, name and age. We then added three records to the table using the INSERT INTO command. Finally, we displayed all the data in the table using the SELECT * FROM command and updated Alice's age to 30 using the UPDATE command.  
You can also delete records from the table using the DELETE FROM command. For example, to delete the record with id equal to 2, you can use the DELETE FROM example_table WHERE id = 2 command.  
Here is an example of using the DuckDB Python library functions to interact with a DuckDB database:  

![test](images/fonction1.PNG)  

![test](images\fonction2.png)   
In this example, we created a
DuckDB database in memory, created a table with data, fetched the data into a cursor, created a Pandas dataframe and registered the dataframe to the database, loaded data from a CSV file, updated and deleted data in the table, then closed the connection.  
This example shows how to use the duckdb.connect(), duckdb.Cursor.execute(), duckdb.Cursor.fetchall(), duckdb.Connection.register(), duckdb.Connection.copy_into(), duckdb.Cursor.execute() functions to perform basic operations on a DuckDB database using Python. 
# Fonctions
First, you can create a DuckDB database using the Python module :  
import duckdb

** 1.Create Database in memory**
con = duckdb.connect(':memory:')
** 2.Then you can load the data into the database using the register function:**
# Charger The data  from file CSV
con.register('ventes', 'data/ventes.csv')  
** 3.To find the best selling products in terms of sales, you can use an SQL query with a join and an aggregation :**  
 ** 4.Perform an SQL query to find the best selling products in terms of sales:**  
query = """
SELECT produit, SUM(quantite_vendue * prix_unitaire) AS chiffre_affaires
FROM ventes
GROUP BY produit
ORDER BY chiffre_affaires DESC
LIMIT 10
"""
result = con.execute(query)

# Afficher les résultats
for row in result:
    print(row)





[# Potential Alternative of Duckdb:]()  
**There are several potential alternatives to DuckDB for in-memory relational databases:**

**SQLite:** SQLite is a lightweight and popular in-memory relational database. It is open-source, widely used, and supports a large number of programming languages, including Python.

**Apache Arrow:** Arrow is an in-memory data processing platform that supports multiple programming languages. It is optimized for parallel and in-memory data processing, and can be used as an alternative to an in-memory database.

**PostgreSQL:** PostgreSQL is an open-source and robust relational database, which supports replication, ACID transactions, indexing, views, triggers, and other advanced features. It is heavier than the previous alternatives but can handle larger data volumes and more complex use cases.

**InfluxDB:** InfluxDB is an in-memory time-series database, optimized for storing and querying time-based data. It is often used to store and analyze sensor, machine, and other IoT data.

**Redis:** Redis is an open-source in-memory database, optimized for performance and scalability. It supports multiple data structures, including strings, lists, sets, maps, and sorted sets.
# Conclusion:
In conclusion,Duckdb isIn conclusion, DuckDB is a lightweight, fast, and easy-to-use solution for database tasks, which can be especially useful 
for projects that require rapid manipulation of relational data.
It is also easily integrated into existing Python applications and offers advanced features for data analysis. However, for more complex projects or projects requiring high availability, other more robust database solutions may be preferable.

# References
https://duckdb.org/
https://duckdb.org/docs/
https://github.com/cwida/duckdb
https://github.com/cwida/duckdb/wiki
https://duckdb.org/docs/sql/sql-features/
https://duckdb.org/docs/api/python/
https://duckdb.org/docs/api/r/
https://duckdb.org/docs/api/jdbc/
https://en.wikipedia.org/wiki/DuckDB

