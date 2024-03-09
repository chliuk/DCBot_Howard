import mysql.connector

#查詢歷史勝率最高前十名
def historywinhighest():
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute('SELECT U1.* FROM `history_table` U1 LEFT JOIN ( SELECT DISTINCT `user_id`,`winning_percentage` FROM `history_table`) U2  ON U1.`winning_percentage`< U2.`winning_percentage` WHERE `history_total_game` >= 15 GROUP BY `user_id`,`winning_percentage` ORDER BY `winning_percentage` DESC,`history_total_game` DESC LIMIT 10;', multi=True)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()
    connection.close()
    return records
#查詢歷史勝率最低前三名
def historywinlowest():
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute('SELECT U1.* FROM `history_table` U1 LEFT JOIN ( SELECT DISTINCT `user_id`,`winning_percentage` FROM `history_table`) U2 ON U1.`winning_percentage`> U2.`winning_percentage` WHERE `history_total_game` >= 15 GROUP BY `user_id`,`winning_percentage` ORDER BY `winning_percentage`,`history_total_game` ASC LIMIT 3;', multi=True)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()
    connection.close()
    return records
#查詢每月勝率最高前十名
def monthlywinhighest():
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute('SELECT U1.* FROM `monthly_table` U1 LEFT JOIN ( SELECT DISTINCT `user_id`,`monthly_percentage` FROM `monthly_table`) U2  ON U1.`monthly_percentage`< U2.`monthly_percentage` WHERE `monthly_total_game` >= 15 GROUP BY `user_id`,`monthly_percentage` ORDER BY `monthly_percentage` DESC,`monthly_total_game` DESC LIMIT 10;', multi=True)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()
    connection.close()
    return records
#查詢每月勝率最低前三名
def monthlywinlowest():
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute('SELECT U1.* FROM `monthly_table` U1 LEFT JOIN ( SELECT DISTINCT `user_id`,`monthly_percentage` FROM `monthly_table`) U2 ON U1.`monthly_percentage`> U2.`monthly_percentage` WHERE `monthly_total_game` >= 15 GROUP BY `user_id`,`monthly_percentage` ORDER BY `monthly_percentage`,`monthly_total_game` ASC LIMIT 3;', multi=True)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()
    connection.close()
    return records
#查詢歷史場數最高前十名
def historynumhighest():
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute('SELECT U1.* FROM `history_table` U1 LEFT JOIN ( SELECT DISTINCT `user_id`,`history_total_game` FROM `history_table`) U2 ON U1.`history_total_game`< U2.`history_total_game` GROUP BY `user_id`,`history_total_game` HAVING COUNT(1)<10 ORDER BY `history_total_game` DESC;', multi=True)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()
    connection.close()
    return records
#查詢每月場數最高前十名
def monthlynumhighest():
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute('SELECT U1.* FROM `monthly_table` U1 LEFT JOIN ( SELECT DISTINCT `user_id`,`monthly_total_game` FROM `monthly_table`) U2 ON U1.`monthly_total_game`< U2.`monthly_total_game` GROUP BY `user_id`,`monthly_total_game` HAVING COUNT(1)<10 ORDER BY `monthly_total_game` DESC;', multi=True)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()
    connection.close()
    return records
#查詢個人歷史戰績
def historyper(id):
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM `history_table` WHERE `user_id`={id};', multi=True)

    records = cursor.fetchall()
    
    for r in records:
        print(r)

    cursor.close()
    connection.close()
    return records
#查詢個人每月戰績
def monthlyper( id ):
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM `monthly_table` WHERE `user_id`={id};', multi=True)

    records = cursor.fetchall()
    for r in records:
        print(r)

    cursor.close()
    connection.close()
    return records



def winer_history_update(UE1_id, UE2_id):
#贏家歷史戰績更新
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()
    
    
    cursor.execute(f'SELECT * FROM `history_table` WHERE `user_id` = {UE1_id};', multi=True)

    records = cursor.fetchall()
    history_win_num = records[0][1]
    print(history_win_num)
    history_win_num +=1
    print(history_win_num)
    cursor.execute(f'UPDATE `history_table` SET `history_win_game` = {history_win_num} WHERE `user_id` = {UE1_id};', multi=True)
    history_total_num = records[0][4]
    print(history_total_num)
    history_total_num += 1
    print(history_total_num)
    new_history_win_percentage = round(history_win_num/history_total_num, 2)
    print(new_history_win_percentage)
    cursor.execute(f'UPDATE `history_table` SET `winning_percentage` = {new_history_win_percentage} WHERE `user_id` = {UE1_id};', multi=True)
    cursor.execute(f'UPDATE `history_table` SET `history_total_game` = {history_total_num} WHERE `user_id` = {UE1_id};', multi=True)
    
    print('f1')
    cursor.close()
    connection.commit()
    connection.close()

    winer_monthly_update(UE1_id, UE2_id)



def winer_monthly_update(UE1_id, UE2_id):
#贏家單月數據更新
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM `monthly_table` WHERE `user_id` = {UE1_id};', multi=True)

    records = cursor.fetchall()
    month_win_num = records[0][1]
    month_win_num +=1
    cursor.execute(f'UPDATE `monthly_table` SET `monthly_win_game` = {month_win_num} WHERE  `user_id` = {UE1_id};', multi=True)
    month_total_num = records[0][4]
    month_total_num += 1
    new_month_win_percentage = round(month_win_num/month_total_num, 2)
    cursor.execute(f'UPDATE `monthly_table` SET `monthly_percentage` = {new_month_win_percentage} WHERE  `user_id` = {UE1_id};', multi=True)
    cursor.execute(f'UPDATE `monthly_table` SET `monthly_total_game` = {month_total_num} WHERE  `user_id` = {UE1_id};', multi=True)
    
    print('f2')
    cursor.close()
    connection.commit()
    connection.close()

    loser_history_update(UE2_id)


def loser_history_update(UE2_id):
#輸家歷史戰績更新
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT * FROM `history_table` WHERE `user_id` = {UE2_id};', multi=True)

    records = cursor.fetchall()
    history_los_num = records[0][2]
    history_los_num +=1
    cursor.execute(f'UPDATE `history_table` SET `history_lose_game` = {history_los_num} WHERE  `user_id` = {UE2_id};', multi=True)
    history_total_num = records[0][4]
    history_total_num += 1
    new_history_win_percentage = round(history_los_num/history_total_num, 2)
    cursor.execute(f'UPDATE `history_table` SET `winning_percentage` = {new_history_win_percentage} WHERE  `user_id` = {UE2_id};', multi=True)
    cursor.execute(f'UPDATE `history_table` SET `history_total_game` = {history_total_num} WHERE  `user_id` = {UE2_id};', multi=True)

    cursor.close()
    connection.commit()
    connection.close()

    loser_monthly_update(UE2_id)


def loser_monthly_update(UE2_id):
#輸家單月數據更新
    connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
    print('successfully connect')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM `monthly_table` WHERE `user_id` = {UE2_id};', multi=True)

    records = cursor.fetchall()
    month_los_num = records[0][2]
    month_los_num +=1
    cursor.execute(f'UPDATE `monthly_table` SET `monthly_lose_game` = {month_los_num} WHERE  `user_id` = {UE2_id};', multi=True)
    month_total_num = records[0][4]
    month_total_num += 1
    new_month_win_percentage = round(month_los_num/month_total_num, 2)
    cursor.execute(f'UPDATE `monthly_table` SET `monthly_percentage` = {new_month_win_percentage} WHERE  `user_id` = {UE2_id};', multi=True)
    cursor.execute(f'UPDATE `monthly_table` SET `monthly_total_game` = {month_total_num} WHERE  `user_id` = {UE2_id};', multi=True)

    cursor.close()
    connection.commit()
    connection.close()
