
# 0-Querying
---
## 1.Introduction

### Database
A collection of data organized for creating, reading, updating and deleting.

### Database management system
software via which you can interact with a database.

### SQL (Structured Query Language)
A language via which you can create, read, update and delete data in a database.




## 2.Keyword (Uppercase)

### SELECT
**SELECT**  is a way to select some rows in a table inside of the database.

- **star operator** ( * ): select everything
- **Semicolon** ( ; ): end my query
- **comma** ( , ) 
### FROM
**FROM** tells SQL which is the table to get to select rows from

#### Good Habit
Column/Table Names: Double Quotes""  
String: Single Quotes''

*For example*:
SELECT "title" , "author" FROM "longlist";    

### LIMIT
**LIMIT** restrict the number of rows returned by a query

*For example*:  
SELECT "title" FROM "longlist" LIMIT 5;    

### WHERE
**WHERE** makes sure to get back some rows, where that condition is true

*For example*:  
SELECT "title" FROM "longlist" WHERE "year" = 2025;

**=**    **!=**    **<>**    **NOT**

*For example*: `'B' 'C' in "A"     get 'B'`
- SELECT "title" FROM "longlist" WHERE "A" = 'B';
- SELECT "title" FROM "longlist" WHERE "A" != 'C';
- SELECT "title" FROM "longlist" WHERE "A" <> 'C';
- SELECT "title" FROM "longlist" WHERE NOT "A" = 'C';

**AND**    **OR**    **( )**

*For example*:  
SELECT "title" FROM "longlist" WHERE ("year" = 2025 OR "year" = 2026)  
AND "A" != 'C'

### NULL
**NULL** means "no value"  
IS NULL  
IS NOT NULL  

### LIKE
**LIKE** is used when I want to roughly match any number of unknown characters around a string, while "=" is used for exact matching

- **The percent sign** ( % ) can match any character 
- **underscore** ( _ ) can match any single character

*For example*:
- SELECT "title" FROM "longlist" WHERE "title" LIKE '%love%';
- SELECT "title" FROM "longlist" WHERE "title" LIKE 'l_ve';

**BETWEEN..AND...**
*For example*:  
SELECT "title" FROM "longlist" WHERE "year" BETWEEN 2023 AND 2025;

### ORDER BY
**ORDER BY** is used to sort the query results

- ORDER BY ...ASC (default)
- ORDER BY ...DESC

*For example*:  
- SELCET "title", "rating" FROM "longlist"  
  ORDER BY "rating" DESC LIMIT 10;

#### Aggregate functions

**COUNT**    **AVG**    **MIN**    **MAX**    **SUM**      


*For example*:  
- SELCET ROUND(AVG("rating"), 2) AS "average rating" FROM "longlist"; 
- SELCET MAX("rating") FROM "longlist";
- SELCET MIN("rating") FROM "longlist";
- SELCET SUM("votes") FROM "longlist";
- SELCET COUNT(DISTINCT "publisher") FROM "longlist";

**ROUND** is used to round a number
**AS** is used to give a column or table a temporary name
**DISTINCT** is used to remove duplicate rows 

---



# 1-Relating
---
## 1.Relating

One-to-one
One-to-many
Many-to-many

## 2.ER Diagrams

### Entity Relationship Diagrams

*For example*:

Author ------|-- Book

**Explain:** An author wrote one book (in this case, read this left to  right)


Author ------|<--Book

**Explain:** An author can write at least one book, but they could write many books

## 3.Key

**Primary Key**
unique  identifier

**Foreign Key**
A foreign key is simply taking a primary key from one table

## 4.Subqueries

*for example:* 

SELECT "title" FROM "book" WHERE  "publisher_id" = (
    SELECT "id" FROM the "publishers"
    WHERE the "publisher" = 'MacLehose Press'
);

SELECT AVG("rating") FROM "ratings" WHERE "book_id"(
    SELECT "id" FROM "books" WHERE "title" = 'In Memory of memory'
);


SELECT "name" FROM "authors" WHERE "id" = (
    SELECT "author_id" FROM "authored" WHERE "book_id" = (
        SELECT "id" FROM "books"
         WHERE "title" = 'The Birthday Party'
    )
);

### IN

*for example:* 

SELECT "title" FROM "books" WHERE "id" IN(
    SELECT "book_id" FROM the "authored" 
    WHERE the "author_id" = (
        SELECT "id" FROM "authors" WHERE "name" = 'Fernanda Melchor'
    ) 
);

only one id "="
more than one "IN"

## 5. Joins

*for example:* 

SELECT * FROM "sea_lions"
JOIN "migrations" ON "migrations"."id" = "sea_lions"."id";

### INNER JOIN


### OUTER JOIN
**"LEFT JOIN"    "RIGHT JOIN"    "FULL JOIN"**

### NATURAL JOIN

*for example:* 

SELECT * FROM "sea_lions"
NATURAL JOIN "migrations";

## 6.Sets

#### UNION (𝐴∪𝐵)

*for example:* 
SELECT 'authors' AS "profession", "name" FROM "authors"
UNION
SELECT 'translator' AS "profession", "name" FROM "translators" ;

#### INTERSECT（𝐴∩𝐵）

*for example:* 
SELECT "name" FROM "authors"
INTERSECT
SELECT "name" FROM "translators" ;

#### EXCEPT
*for example:* 
SELECT "name" FROM "authors"
EXCEPT
SELECT "name" FROM "translators" ;

## 7.Groups

SELECT "book_id", AVG("rating") AS "average rating"
FROM "ratings"
GROUP BY "book_id";

**HAVING**
SELECT "book_id", ROUND(AVG("rating"),2 ) AS "average rating"
FROM "ratings"
GROUP BY "book_id"
HAVING "average rating" > 4.0
ORDER BY "average rating" DESC;