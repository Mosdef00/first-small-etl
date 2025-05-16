SELECT c."cylinders", AVG(c.horsepower_hp) AS avg_horsepower
FROM cars c
GROUP BY c."cylinders";