import sqlite3

## Connect to database
conn = sqlite3.connect('connor.db')
c = conn.cursor()

## Data to be inserted into ModelNoTable
c.execute("INSERT INTO ModelNoTable VALUES(null, 5, 4, 'saloon')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 4, 4, 'saloon')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 2, 2, 'saloon')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 5, 3, 'saloon')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 3, 4, 'saloon')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 4, 4, 'hatchback')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 5, 4, 'hatchback')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 4, 2, 'hatchback')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 2, 2, 'convertible')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 4, 4, 'convertible')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 5, 5, 'suv')")
c.execute("INSERT INTO ModelNoTable VALUES(null, 7, 5, 'suv')")
conn.commit()


## Data to be inserted into MechanicalDataTable
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 1.6, 'manual', 'right', 'diesel')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 2.0, 'automatic', 'right', 'petrol')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 2.4, 'manual', 'right', 'petrol')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 1.9, 'manual', 'right', 'diesel')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 3.0, 'automatic', 'right', 'diesel')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 2.2, 'manual', 'right', 'diesel')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 1.4, 'automatic', 'left', 'petrol')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 3.2, 'manual', 'right', 'diesel')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 3.2, 'manual', 'left', 'hybrid')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 2.0, 'manual', 'right', 'diesel')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 2.0, 'manual', 'left', 'diesel')")
c.execute("INSERT INTO MechanicalDataTable VALUES(null, 2.6, 'manual', 'right', 'diesel')")
conn.commit()


## Data to be inserted into AffordabilityTable
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 12', '74 mpg', 30)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 14', '44 mpg', 130)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 07', '52 mpg', 110)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 11', '72 mpg', 150)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 15', '32 mpg', 105)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 3', '80 mpg', 125)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 5', '52 mpg', 132)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 8', '50 mpg', 190)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 11', '64 mpg', 105)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 8', '46 mpg', 90)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 15', '74 mpg', 30)")
c.execute("INSERT INTO AffordabilityTable VALUES(null, 'group 22', '28 mpg', 70)")
conn.commit()




## Data to be inserted into StatisticalDataTable
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 10.8, '99g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 9.8, '105/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 15.5, '102g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 12.9, '120g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 11.9, '85g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 17.4, '79g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 8.2, '104g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 11.9, '122g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 10.1, '89g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 15.3, '85g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 11.2, '90g/km')")
c.execute("INSERT INTO StatisticalDataTable VALUES(null, 17.0, '99g/km')")
conn.commit()



## Data to be inserted into DealerTable
c.execute("INSERT INTO DealerTable VALUES(null, 'marcin', 'sorokosz', 'claremont avenue', 6, 'garden city', 'ch5 4kj', 'marcin@gmail.com', 07849203399, '0')")
c.execute("INSERT INTO DealerTable VALUES(null, 'tom', 'smith', 'dee road', 26, 'queensferry', 'ch5 9no', 'tom@smith.com', 012445784211, '1')")
c.execute("INSERT INTO DealerTable VALUES(null, 'bradley', 'merino', 'cestrian avenue', 15, 'chester', 'k32 98kj', 'bradley@merino.com', 001478532147, '0')")
c.execute("INSERT INTO DealerTable VALUES(null, 'jacob', 'barton', 'marching road', 11, 'liverpool', 'fkc 1ol', 'jacob@barton.com', 012254778451, '0')")
c.execute("INSERT INTO DealerTable VALUES(null, 'david', 'edwards', 'diamond street', 9, 'wrexham', 'st4 5km', 'david@edwards.com', 078451114254, '1')")
c.execute("INSERT INTO DealerTable VALUES(null, 'joseph', 'branson', 'davies court', 72, 'liverpool', 'xdl 28k', 'joseph@banson.com', 036659985214, '1')")
c.execute("INSERT INTO DealerTable VALUES(null, 'christy', 'mouse', 'holly road', 138, 'manchester', 'llo1 32d', 'christy@mouse.com', 075487114422, '0')")
c.execute("INSERT INTO DealerTable VALUES(null, 'emilia', 'walker', 'uploads street', 122, 'london', 'kl4 29j', 'emilia@walker.com', 316985244124, '1')")
c.execute("INSERT INTO DealerTable VALUES(null, 'richard', 'davies', 'moving avenue', 4, 'birmingham', 'ch51 9lo', 'richard@davies.com', 07347812244, '0')")
c.execute("INSERT INTO DealerTable VALUES(null, 'aaron', 'cronshaw', 'princess street', 12, 'shotton', 'ch2 4aj', 'aaron@cronshaw.com', 0783214567711, '0')")
conn.commit()


## Data to be inserted into CarTable
c.execute("INSERT INTO CarTable VALUES('fa11 hxz', 'volvo', 's40', 'r-design', 8500, 2010, 'silver', 1, 1, 1, 1, 1)")
c.execute("INSERT INTO CarTable VALUES('db12 dbo', 'bmw', '3 series', '320', 6500, 2012, 'green', 2, 2, 2, 2, 2)")
c.execute("INSERT INTO CarTable VALUES('op14 pas', 'audi', 'rs7', 'c5', 28200, 2014, 'black', 4, 3, 3, 3, 7)")
c.execute("INSERT INTO CarTable VALUES('ll05 kxz', 'chevrolet', 'cruse', 't300', 8200, 2005, 'dark blue', 2, 4, 4, 4, 3)")
c.execute("INSERT INTO CarTable VALUES('xd11 qaz', 'audi', 'a5', 'b7', 8500, 2011, 'dark blue', 3, 5, 5, 5, 1)")
c.execute("INSERT INTO CarTable VALUES('rt17 aaz', 'volvo', 's60', 'luxury', 7500, 2017, 'black', 2, 6, 6, 6, 4)")
c.execute("INSERT INTO CarTable VALUES('ts18 cca', 'fiat', 'punto', 'premium', 10500, 2018, 'pearl', 8, 7, 7, 7, 3)")
c.execute("INSERT INTO CarTable VALUES('ft05 dta', 'mercedes', 'cls', 'stand', 12340, 2005, 'white', 9, 8, 8, 8, 2)")
c.execute("INSERT INTO CarTable VALUES('xz02 pol', 'bmw', 'm5', 'open', 2560, 2002, 'silver', 5, 9, 9, 9, 8)")
c.execute("INSERT INTO CarTable VALUES('mm09 ang', 'toyota', 'yaris', 'timex', 2500, 2009, 'grey', 3, 10, 10, 1, 5)")
c.execute("INSERT INTO CarTable VALUES('lz08 uks', 'peugeot', '206', 'c66', 3500, 2008, 'red', 4, 11, 11, 11, 7)")
c.execute("INSERT INTO CarTable VALUES('po12 rss', 'seat', 'ibiza', 'l3', 5500, 2012, 'black', 10, 12, 12, 12, 8)")
conn.commit()
