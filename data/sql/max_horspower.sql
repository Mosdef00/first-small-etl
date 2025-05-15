SELECT c."Car Model", c.horsepower_hp
FROM cars c
WHERE c.horsepower_hp = (SELECT MAX(c.horsepower_hp) FROM cars c);