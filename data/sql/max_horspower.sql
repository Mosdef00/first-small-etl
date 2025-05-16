SELECT c.car_model, c.horsepower_hp
FROM cars c
WHERE c.horsepower_hp = (SELECT MAX(c.horsepower_hp) FROM cars c);