SELECT c."transmission", COUNT(*) AS car_count
FROM cars c
GROUP BY c."transmission";