from database.DB_connect import DBConnect
from model.stati import Stato

class DAO():
    @staticmethod
    def anni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year (s.`datetime`) as anni
                    from sighting s 
                    where year(s.`datetime`)>= 1910 and  year(s.`datetime`)<= 2014
                    order by anni desc"""

        cursor.execute(query)

        for row in cursor:
            result.append(row['anni'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def forme():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct s.shape as f
                    from sighting s 
                    order by f asc """

        cursor.execute(query)

        for row in cursor:
            result.append(row['f'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state s  """

        cursor.execute(query)

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def archi(forma,anno,s1,s2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as pes
                    from sighting s 
                    where  s.shape =%s and year(s.`datetime`)=%s  and (s.state =%s  or s.state =%s )
                    group by s.state 
                    """

        cursor.execute(query,(forma,anno,s1,s2,))

        for row in cursor:
            result.append(row['pes'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def soloarchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select n.state1 as s1,n.state2 as s2
from neighbor n
    """

        cursor.execute(query)

        for row in cursor:
            result.append((row['s1'], row['s2']))

        cursor.close()
        conn.close()
        return result



