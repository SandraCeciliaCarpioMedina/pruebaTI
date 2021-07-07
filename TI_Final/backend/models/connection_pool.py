# pip install mysql-connector-python
import time
import mysql.connector.pooling

dbconfig = {
    "host":"127.0.0.1",
    "port":"3306",
    "user":"root",
    "password":"admi",
    "database":"proyecto",
}

class MySQLPool(object):
    """
    crea un grupo cuando se conecta mysql,lo que disminuirá el tiempo empleado en
    solicitar conexión, crear conexión y cerrar conexión.
    """
    def __init__(self):             
        self.pool = self.create_pool(pool_name='task_pool', pool_size=3)

    def create_pool(self, pool_name, pool_size):
        """
        Cree un grupo de conexiones, después de creado, la solicitud de conexión
        MySQL podría obtener una conexión de este grupo en lugar de una solicitud a
        crear una conexión.
        :param pool_name: the name of pool, default is "mypool"
        :param pool_size: the size of pool, default is 3
        :return: connection pool
        """
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **dbconfig)
        return pool

    def close(self, conn, cursor):
        """
        A method used to close connection of mysql.
        :param conn: 
        :param cursor: 
        :return: 
        """
        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
        """
        Ejecute un sql, podría ser con argumentos y sin argumentos. El uso es
        similar con la función execute () en el módulo pymysql.
        :param sql: sql clause
        :param args: args need by sql clause
        :param commit: whether to commit
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return cursor
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res

    def executemany(self, sql, args, commit=False):
        """
        Ejecutar con muchos argumentos. Similar con la función executemany () en pymysql.
        Los argumentos deben ser una secuencia.
        :param sql: sql clause
        :param args: args
        :param commit: commit or not.
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res


if __name__ == "__main__":
    mysql_pool = MySQLPool()
    sql = "select * from task"
        
    while True:
        t0 = time.time()
        for i in range(10):
            mysql_pool.execute(sql)
            print (i)
        print ("time cousumed:", time.time() - t0)