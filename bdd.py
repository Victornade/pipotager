
import psycopg2
from pymongo import MongoClient

#MongoConfig
#MONGO_URL='mongodb://localhost:27017/'
MONGO_URL='mongodb://pipotager:mcs1aptesb1f@cluster0-shard-00-00-uzi15.mongodb.net:27017,cluster0-shard-00-01-uzi15.mongodb.net:27017,cluster0-shard-00-02-uzi15.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'

#PostgresConfig
HOST='localhost'
DBNAME='pipotager'
SCHEMA='pi'
PASSWORD='mcs1aptesb1f'
PORT='5432'

def getConnection2(host, dbname, schema, password, port): 
    # Connect to an existing database
    return psycopg2.connect("dbname='"+str(dbname)+"' user="+str(schema)+" host="+str(host)+"  port='"+str(port)+"' password="+str(password)+" ")

def getConnection():
	return  MongoClient(MONGO_URL).pipotager
	
def closeConnection(conn):
    conn.commit()
    conn.close()
    

def insertDatas2(temp, humidite, pression, lumiere, air, hum1,hum2,hum3,hum4, hum5, hum6):
	db=getConnection2(HOST, DBNAME, SCHEMA, PASSWORD, PORT)
	cur=db.cursor()
	cur.execute("""INSERT INTO data.data (date,temperature,humidite_air,humidite_1, humidite_2,humidite_3,humidite_4, humidite_5, humidite_6, air, pression, lux)
			values(NOW(), %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s, %s, %s, %s)""",
			(temp, humidite, hum1,hum2,hum3,hum4, hum5, hum6, air, pression, lumiere))
	cur.close()
	closeConnection(db)

def insertDatas(temp, humidite, pression, lumiere, air, hum1,hum2,hum3,hum4, hum5, hum6, date):
	db=getConnection()
	data={
		'lux': lumiere,
		'pression': pression,
		'humidite_1': hum1,
                'humidite_2': hum2,
                'humidite_3': hum3,
                'humidite_4': hum4,
                'humidite_5': hum5,
                'humidite_6': hum6,
		'temperature':temp,
		'humidite_air':humidite,
		'air': air,
		'date':date
	}
	print data
	db.datas.insert_one(data)

if __name__ == '__main__':
	print 'ok'	
	postgres=getConnection2(HOST, DBNAME, SCHEMA, PASSWORD, PORT)
	mongo=getConnection();
	print mongo
	cur=postgres.cursor()
	cur.execute("select date,temperature,humidite_air,humidite_1, humidite_2,humidite_3,humidite_4, humidite_5, humidite_6, air, pression, lux from data.data")
	rows = cur.fetchall()
	for row in rows:
		print row
 		insertDatas(row[1],row[2],row[10],row[11],row[9],row[3],row[4],row[5],row[6],row[7],row[8],row[0])
	closeConnection(postgres)
