import sqlite3

from PyQt5.QtWidgets import QMessageBox


# class sqlsequence:
#     def addstudent(self):
#         name="这"
#         try:
#             self.conn = sqlite3.connect("database.db")
#             self.c = self.conn.cursor()
#             self.c.execute("INSERT INTO words (word_name,word_audio,word_image) VALUES (?,?,?)",(name, "audio/word/"+name+".mp3","image/"+name+".jpg"))
#             self.conn.commit()
#             self.c.close()
#             self.conn.close()
#             print('Successful')
#             self.close()
#         except Exception:
#             return
#
# sqls=sqlsequence()
# sqls.addstudent()

import os
import os.path
import sqlite3

# 设置路径和数据库文件名
path = "audio/vowel"
db_file = "database.db"

# 连接数据库并执行查询语句
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("SELECT vowel_no, vowel_name FROM vowel")
rows = cursor.fetchall()

# 遍历目录下的所有文件
for root, dirs, files in os.walk(path):
    for file in files:
        # 获取文件名和后缀名
        file_name, file_ext = os.path.splitext(file)
        # 遍历查询结果，查找是否有匹配的文件名
        for row in rows:
            vowel_no = row[0]
            vowel_name = row[1]
            if file_name == vowel_name:
                # 构造新的文件名
                new_file_name = f"{vowel_no}{file_ext}"
                # 重命名文件
                os.rename(os.path.join(root, file), os.path.join(root, new_file_name))
                print(f"Renamed {file} to {new_file_name}")

# 关闭数据库连接
cursor.close()
conn.close()
