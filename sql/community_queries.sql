SELECT community, diabetes_rate
FROM community_health 
WHERE diabetes_rate >= 12
ORDER BY diabetes_rate DESC;

SELECT AVG(diabetes_rate) AS average_diabetes_rate
FROM community_health;