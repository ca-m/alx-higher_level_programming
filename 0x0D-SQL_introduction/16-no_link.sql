-- lists all records of table second_table having a name value
-- records are in descending order of score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
