## A) State and Explain the components of a DBMS(Database Management System)
1. **Database Engine**:  
   - Handles data storage, retrieval, and updates.  
   - Processes queries and executes transactions.

2. **Database Schema**:  
   - Defines the logical structure of the database, including tables, relationships, and constraints.

3. **Query Processor**:  
   - Interprets and processes user queries to extract required data from the database.

4. **Transaction Management**:  
   - Ensures ACID (Atomicity, Consistency, Isolation, Durability) properties for reliable data transactions.

5. **Data Dictionary**:  
   - Metadata repository that contains information about database structure, objects, and user permissions.

6. **User Interface**:  
   - Enables users to interact with the DBMS via graphical interfaces or command-line tools.

---

## B) What is a relational database? Give 4 examples.
A relational database organizes data into tables (relations) with rows (records) and columns (attributes). Relationships between tables are established using keys.

### Examples:
- MySQL  
- PostgreSQL  
- Microsoft SQL Server  
- Oracle Database  

---

## C) State and Explain three classifications of SQL?
1. **Data Definition Language (DDL)**:  
   - Used to define and manage database schema and objects.  
   - Examples: `CREATE`, `ALTER`, `DROP`

2. **Data Manipulation Language (DML)**:  
   - Used for inserting, updating, deleting, and retrieving data.  
   - Examples: `INSERT`, `UPDATE`, `DELETE`, `SELECT`

3. **Data Control Language (DCL)**:  
   - Used to manage user access and permissions.  
   - Examples: `GRANT`, `REVOKE`

---

## D) What is the difference between a Primary Key and a Foreign Key?

| **Primary Key**                  | **Foreign Key**                     |
|-----------------------------------|-------------------------------------|
| Uniquely identifies each record in a table. | Establishes a relationship between two tables. |
| Cannot contain NULL values.       | Can contain NULL values if optional. |
| Defined within a single table.    | References a primary key in another table. |

---

## E) What is an Entity-Relationship Diagram?
An **Entity-Relationship Diagram (ERD)** is a visual representation of a database's entities, attributes, and the relationships between them. It is used in database design to illustrate data structure and logical connections.

---

## F) What are the advantages of relational databases?
1. **Data Integrity**:  
   - Enforces data consistency through constraints and rules.

2. **Flexibility**:  
   - Allows complex queries and easy data manipulation.

3. **Scalability**:  
   - Can handle increasing amounts of data efficiently.

4. **Ease of Use**:  
   - Uses a standardized query language (SQL) for operations.

5. **Security**:  
   - Provides robust mechanisms to restrict unauthorized access.

---

## G) State four types of data type used to store data in tables?
1. **Integer**:  
   - Stores whole numbers (e.g., `INT`, `SMALLINT`).

2. **Character/String**:  
   - Stores text data (e.g., `CHAR`, `VARCHAR`).

3. **Date/Time**:  
   - Stores date and time values (e.g., `DATE`, `TIMESTAMP`).

4. **Floating-Point**:  
   - Stores decimal numbers (e.g., `FLOAT`, `DOUBLE`).

---

## H) What is the purpose of a database management system (DBMS)?
The purpose of a **Database Management System (DBMS)** is to manage and organize data efficiently by enabling:  
1. **Data Storage**:  
   - Centralized and structured data storage.  

2. **Data Retrieval**:  
   - Easy access and manipulation of data.  

3. **Data Integrity**:  
   - Maintenance of accurate and consistent data.  

4. **Data Security**:  
   - Protection against unauthorized access.  

5. **Concurrency Control**:  
   - Handling simultaneous data operations.  
