CREATE TABLE for_tests(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    id_user VARCHAR(20) COMMENT 'login of user',
    stat_sus INT(1) COMMENT 'status of point',
    create_time DATETIME COMMENT 'Create Time',
    update_time DATETIME COMMENT 'Update Time',
    longitude FLOAT(9,6) COMMENT 'real longitude of point',
    latitude FLOAT(9,6) COMMENT 'real latitude of point',
    longitude_user FLOAT(7,5) COMMENT 'longitude of point mesured by user',
    latitude_user FLOAT(7,5) COMMENT 'latitude of point mesured by user',
    mean_vertical FLOAT(7,5) COMMENT 'mean value of vertical B vector',
    std_dev_vertical FLOAT(7,5) COMMENT 'standard deviation of vertical B vector',
    mean_horizontal FLOAT(7,5) COMMENT 'mean value of horizontal B vector',
    std_dev_horizontal FLOAT(7,5) COMMENT 'standard deviation of horizontal B vector'
) DEFAULT CHARSET UTF8 COMMENT 'yeah!';