import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="GPI2020!", host="100.26.53.126", port="5432")

print("Database opened successfully")




cur = con.cursor()
cur.execute(r"COPY persons FROM '/home/ubuntu/mahavir_data/test.csv' DELIMITER ',' CSV HEADER;");

#cur.execute("COPY persons FROM 'test.csv' DELIMITER ',' CSV HEADER;");


con.commit()
print("Records inserted successfully")
con.close()