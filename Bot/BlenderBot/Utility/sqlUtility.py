import mysql.connector
from mysql.connector import errorcode

class sqlUtility:
  db = None
  def __init__(self):
    print('here')
    try:
      self.db = mysql.connector.connect(
        user='root',
        password='password',
        host='mysql',
        database='test'
      )
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
  def prepareDatabase(self):
    query = (
      "CREATE TABLE IF NOT EXISTS `servers` ("
      "  `id` int(11) NOT NULL UNIQUE,"
      "  `name` char(64) NOT NULL,"
      "  PRIMARY KEY  (`id`)"
      ");"
      "CREATE TABLE IF NOT EXISTS `terms` ("
      "  `server_id` int(11) NOT NULL,"
      "  `id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,"
      "  `num` int(11) NOT NULL,"
      "  `content` CHAR(256) NOT NULL,"
      "  FOREIGN KEY (id) REFERENCES servers(id),"
      "  PRIMARY KEY  (`id`)"
      ");"
    )
    conn = self.db.cursor()
    conn.execute(query)
    self.db.commit()
    conn.close()
