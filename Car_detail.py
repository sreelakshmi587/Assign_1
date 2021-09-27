import sqlite3
con=sqlite3.connect('Cardirectory.db')
cur=con.cursor()

# car_detail="""
#     CREATE TABLE Cars(
#         car_name TEXT NOT NULL,
#         owner_name TEXT NOT NULL)"""
# cur.execute(car_detail)

car_detail = "INSERT INTO Cars(Car_name,Owner_name) VALUES(?,?)"
cur.execute(car_detail,('Mahindra Thar','Sreelakshmi'))
cur.execute(car_detail,('Hyundai Creta','Sunny'))
cur.execute(car_detail,('Tata Nexon','George'))
cur.execute(car_detail,('Toyota Fortuner','Sima'))
cur.execute(car_detail,('Maruti Brezza','Raj'))
cur.execute(car_detail,('Hyundai Venue','Kyle'))
cur.execute(car_detail,('Maruti Ertiga','Soman'))
cur.execute(car_detail,('Tata Altroz' ,'Sathi'))
cur.execute(car_detail,('Skoda Rapid','Villy'))
cur.execute(car_detail,('Maruti Suzuki Alto','Ganga'))

cur.execute("SELECT * FROM Cars")
Car_name,Owner_name="Car_name","Owner_name"
format=[f"{Car_name:<35}{Owner_name:<35}" for Car_name,Owner_name in cur.fetchall()]
print('\n'.join([f"{Car_name:<35}{Owner_name:<35}"] + format))
con.commit()
con.close()



