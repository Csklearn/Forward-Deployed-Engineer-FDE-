# Database

### Database is an organized collection of data to store, update, delete.

### Operations

- GET
- POST
- PUT 
- DELETE

## Types

- Relational
    - use SQL
    - Examples MySQL , Oracle, SQLlite
- No SQL
    - Json format
    - No predefined schema
    - Example Mongo , Redis , Cassandra
- Vector
    - RAG Embeddings , vector formats
    - Advnatage of RAG can convert any unstrutred data to vector formats and stored in vector DB
    - Examples Pinecone , chroma, OpenSearch

## Create database

### My SQL
   - create database database_name;
   - create table
      use database database_name;
      create table database_name.customers {
        name VRACHAR(40),
        email VARCHAR(40)
      }
    - Insert table

    INSERT INTO TABLE_NAME(name,email) VALUES
    ("msd","msd@gmail.com"),
    ("koli","kholi@gail.com")

- retrieve data from tabel
 SELECT * from table_name;

 ### Mongo

 - use db_name;
 - db_name.createCollection('collection_name')
 - db.collection_name.insertMany/find/updateOne