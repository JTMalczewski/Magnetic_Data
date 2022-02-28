SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'measurements'

INSERT INTO measurements (latitude, longitude)
VALUES (); 
ALTER TABLE measurements
DROP COLUMN create_time;