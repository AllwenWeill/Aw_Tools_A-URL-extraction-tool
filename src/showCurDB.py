#获取当前数据库内容
import sqlite3
import time
DB = sqlite3.connect("E:/gotUrl.db")
#DB = sqlite3.connect(":memory:")
cursorObj = DB.cursor()
while 1:
    cursorObj.execute("SELECT * FROM URLs")
    DB.commit()
    print(cursorObj.fetchall())
    time.sleep(5)
