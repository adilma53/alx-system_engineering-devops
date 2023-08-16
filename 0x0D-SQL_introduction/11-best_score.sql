-- list all scroes above 10 and from best to worst --
SELECT  score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;