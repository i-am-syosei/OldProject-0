#　データベースからURLを取り出して画像を表示させる
import os
import math
import mysql.connector
import random
import glob
import shutil
import datetime
def conn_db():
      conn = mysql.connector.connect(
              host = ###,
              port=###,
              user = ###,
              passwd = ###,
              db = ###
      )
      return conn

# 重複なし乱数をa~bの間でk個生成
def rand_nodup(a, b, k):
    r = set()
    while len(r) < k:
        r.add(random.randint(a, b))
    return r


# 神経衰弱に使用するカードを入れておくimagesフォルダを指定
dir = "./static/images/"
# imagesフォルダごと削除
shutil.rmtree(dir)
# imagesフォルダがなければ./static/imagesを作成する

if not os.path.exists(dir): # ディレクトリが存在するか確認
        os.makedirs(dir) # ディレクトリ作成

dir_path = "./static/cards/" #cardsフォルダを格納

file_list = os.listdir(dir_path) #cards内のファイル総数を格納
id_last = int(len(file_list) / 2) #ファイル総数を2で割ってid_lastに格納

# ランダムでimagesの中から16この画像をcardsにコピー

# 生成したい乱数の数
g_num = 16
# データ格納先
rows = list()

rand_num = list(rand_nodup(1, id_last, g_num))
try:
        conn = conn_db()              #ここでDBに接続
        cursor = conn.cursor()       #カーソルを取得
        for i in range(0,16):
                sql = ('''SELECT path1,path2,theme_name FROM CARD WHERE card_id = '{}';'''.format(rand_num[i]))
                cursor.execute(sql)             #selectを投げる
                rows.append(list(cursor.fetchone()))      #selectの結果を格納
except(mysql.connector.errors.ProgrammingError) as e:
        print('エラーだぜ')
        print(e)


print(rows[0])
print(rows[1])
print(rows[2])
# print(glob.glob(rows[1],  recursive=True))
# cardsからimagesへ画像をコピー
t =""
u =""
dt_now = datetime.datetime.now()
try:
        conn = conn_db()              #ここでDBに接続
        cursor = conn.cursor()       #カーソルを取得
        sql = ('''DROP TABLE IMAGE''')
        cursor.execute(sql)
        conn.commit()
        sql = ('''CREATE TABLE IMAGE( card_id INT(6) AUTO_INCREMENT NOT NULL PRIMARY KEY, path1 varchar(100) NOT NULL UNIQUE, path2 varchar(100) NOT NULL UNIQUE, theme_name varchar(20) NOT NULL);''')
        cursor.execute(sql)
        conn.commit()
        # rows = cursor.fetchall()      #selectの結果を全件タプルに格納
except(mysql.connector.errors.ProgrammingError) as e:
        print('エラーだぜ')
        print(e)
for i in range(0,16):
        for j in range(2):
                r = rows[i][j]
                s = r[16:]
                if j == 1:
                        t = "./static/images/" + "d" + str(i+1) + ".png"
                        shutil.copyfile(rows[i][j],t)
                else:
                        u = "./static/images/" + "s" + str(i+1) + ".png"
                        shutil.copyfile(rows[i][j],u)
        try:
                conn = conn_db()              #ここでDBに接続
                cursor = conn.cursor()       #カーソルを取得
                sql = ('''INSERT INTO IMAGE (path1,path2,theme_name) VALUES('{}','{}','{}');'''.format(t,u,rows[i][2]))
                cursor.execute(sql)
                conn.commit()
                # rows = cursor.fetchall()      #selectの結果を全件タプルに格納
        except(mysql.connector.errors.ProgrammingError) as e:
                print('エラーだぜ')
                print(e)
                
                
