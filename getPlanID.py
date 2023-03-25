import cx_Oracle

#define a connection to DB
DBUSER = 'STC_read'
DBPASSWORD = 'prodread'
dsnStr = cx_Oracle.makedsn("db01.di01.sapp", "1521", "SAPPROD11")
connection = cx_Oracle.connect(user=DBUSER, password=DBPASSWORD, dsn=dsnStr)

#open input file and read line
with open ("input.txt","r") as f:
    for line in f:
        inputs=str(line.strip())

       #execute query and print result
        cursor=connection.cursor()
        cursor.execute("""select ps.id from saas_prod_sapphire.planpurchase pp
            join saas_prod_sapphire.plansubscription ps on ps.planpurchaseid=pp.id
            join saas_prod_sapphire.subscribernetworkid sn on sn.id=pp.subscribernetworkid
            where
            pp.sku='200011255' AND ps.status=2 AND sn.phonenumber= :nv""",nv=inputs)
        result=cursor.fetchall()
        for row in result:
            print(row[0])
        cursor.close()
#close DB connection
connection.close()
