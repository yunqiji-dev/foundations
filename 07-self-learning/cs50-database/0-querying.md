# 0.Introduction
---
## Database
A collection of data organized for creating, reading, updating and deleting.

## Database management system
software via which you can interact with a database.

## SQL (Structured Query Language)
A language via which you can create, read, update and delete data in a database.


# 1.Keyword (Uppercase)
---
## SELECT
**SELECT**  is a way to select some rows in a table inside of the database.

- **star operator** ( * ): select everything
- **Semicolon** ( ; ): end my query
- **comma** ( , ) 
## FROM
**FROM** tells SQL which is the table to get to select rows from

#### Good Habit
Column/Table Names: Double Quotes""  
String: Single Quotes''

*For example*:
SELECT "title" , "author" FROM "longlist";    

## LIMIT
**LIMIT** restrict the number of rows returned by a query

*For example*:  
SELECT "title" FROM "longlist" LIMIT 5;    

## WHERE
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

## NULL
**NULL** means "no value"  
IS NULL  
IS NOT NULL  

## LIKE
**LIKE** is used when I want to roughly match any number of unknown characters around a string, while "=" is used for exact matching

- **The percent sign** ( % ) can match any character 
- **underscore** ( _ ) can match any single character

*For example*:
- SELECT "title" FROM "longlist" WHERE "title" LIKE '%love%';
- SELECT "title" FROM "longlist" WHERE "title" LIKE 'l_ve';

**BETWEEN..AND...**
*For example*:  
SELECT "title" FROM "longlist" WHERE "year" BETWEEN 2023 AND 2025;

## ORDER BY
**ORDER BY** is used to sort the query results

- ORDER BY ...ASC (default)
- ORDER BY ...DESC

*For example*:  
- SELCET "title", "rating" FROM "longlist"  
  ORDER BY "rating" DESC LIMIT 10;

### Aggregate functions

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

