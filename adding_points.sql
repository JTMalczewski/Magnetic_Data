SELECT * FROM measurements LIMIT 100;

-- BULK INSERT dfd
-- FROM '/home/john_johnson/Pulpit/Coding/Magnetic_Data/PoinsBlonia.csv'
-- WITH
-- (
--     FIRSTROW = 2, -- as 1st one is header
--     FIELDTERMINATOR = ',',  --CSV field delimiter
--     ROWTERMINATOR = '\n',   --Use to shift the control to next row
--     TABLOCK
-- )
-- BULK INSERT measurements
--     FROM 'C:\CSVData\Schools.csv'
--     WITH
--     (
--     FIRSTROW = 2,
--     FIELDTERMINATOR = ',',  --CSV field delimiter
--     ROWTERMINATOR = '\n',   --Use to shift the control to next row
--     ERRORFILE = 'C:\CSVDATA\SchoolsErrorRows.csv',
--     TABLOCK
--     )


SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'measurements'

-- INSERT INTO measurements (latitude, longitude)
-- VALUES (); 
-- ALTER TABLE measurements
-- DROP COLUMN create_time;