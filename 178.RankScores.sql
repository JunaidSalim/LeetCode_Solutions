-- Write your PostgreSQL query statement below
SELECT score,
(SELECT count(DISTINCT score) FROM scores s2 WHERE s1.score<=s2.score ) AS rank
FROM scores s1
ORDER BY score DESC;