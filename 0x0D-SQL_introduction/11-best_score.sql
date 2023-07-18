-- lists all records in table second_table with a score >= 10
-- records are in descending order of score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
