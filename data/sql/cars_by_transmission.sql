SELECT c."Transmission", COUNT(*) AS car_count
FROM cars c
GROUP BY c."Transmission";