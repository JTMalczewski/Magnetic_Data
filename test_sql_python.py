import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mysql.agh.edu.pl',
                             user='jtbmalcz',
                             password='6mviFHNt8Yj7hwzc',
                             database='jtbmalcz',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `tablica_testowa` (`id`) VALUES (%s)"
        cursor.execute(sql, (6))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `tablica_testowa`  WHERE `id` = %s"
        cursor.execute(sql,(6))
        result = cursor.fetchone()
        print(result)
