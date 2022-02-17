/*query selects last names, loyalty points and email from the loyalty table filtering email addresses that are .gov or .org  while sorting them in ascending and descending order respectively*/
SELECT substring_index(name, " ", -1) as "last_name", points, email
FROM pub1.loyalty
WHERE pub1.loyalty.email LIKE "%.gov" OR pub1.loyalty.email LIKE "%.org"
ORDER BY last_name ASC, points DESC;

/*query selects a list of titles with a lenght > 12 from titles table showing first 15 characters of title sorting by titles ascending*/
SELECT DISTINCT(SUBSTRING(bktitle, 1, 15)) as titles
FROM pub1.titles
WHERE LENGTH(TRIM(bktitle)) > 12 ORDER BY titles ASC;

/*query selects the partnum, bktitle, slprice, pubdate columns from table titles published between 2012 and 2017 filtering do not have "play", "repair", or "build" in their titles*/
SELECT partnum, bktitle, slprice, pubdate
FROM pub1.titles
WHERE(lower(bktitle) NOT LIKE "%repair%" AND lower(bktitle) NOT LIKE "%play%" 
AND lower(bktitle) NOT LIKE "%build%");

/*query returns the total sold for the items with the given part number*/
SELECT SUM(qty) FROM pub1.sales WHERE partnum = "40121";
SELECT SUM(qty) FROM pub1.sales WHERE partnum = "40125";
SELECT SUM(qty) FROM pub1.sales WHERE partnum = "40325";

/*query returns a list of items by part number, quantity and customer id ranking by quantity*/
SELECT sldate, partnum, qty, custnum, RANK()
OVER (PARTITION BY MONTHNAME(sldate) ORDER BY qty DESC)
FROM pub1.sales ORDER BY quantity_rank;

/*query returns the top 20 books by sales price that have at least 3 words in title*/
SELECT partnum, bktitle, slprice, pubdateFROM pub1.titles
FROM pub1.titles
WHERE bktitle LIKE "% % %"
ORDER BY slprice DESC LIMIT 20;
