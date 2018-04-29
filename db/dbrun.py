import sqlite3

conn = sqlite3.connect('connor.db')

c = conn.cursor()

c.execute("PRAGMA foreign_keys = on")
## Creating ModelNoTable
c.execute("""CREATE TABLE ModelNoTable (
			ModelNumber INTEGER PRIMARY KEY,
			NumberOfSeats INTEGER,
			NumberOfDoors INTEGER,
			BodyType TEXT
			)""")			
conn.commit()

## Creating MechanicalDataTable
c.execute("""CREATE TABLE MechanicalDataTable (
			MechanicalNumber INTEGER PRIMARY KEY,
			EngineSize REAL,
			GearboxType TEXT,
			Drivetrain TEXT,
			FuelType TEXT
			)""")		
conn.commit()

## Creating AffordabilityTable
c.execute("""CREATE TABLE AffordabilityTable (
			AffordabilityNumber INTEGER PRIMARY KEY,
			InsuranceGroup INTEGER,
			FuelConsumption INTEGER,
			AnnualTax REAL
			)""")			
conn.commit()

## Creating StatisticalDataTable
c.execute("""CREATE TABLE StatisticalDataTable (
			StatisticalDataNumber INTEGER PRIMARY KEY,
			AccelerationTime REAL,
			Co2Emissions INTEGER
			)""")		
conn.commit()

## Creating DealerTable
c.execute("""CREATE TABLE DealerTable (
			DealrshipNumber INTEGER PRIMARY KEY,
			FirstName TEXT,
			LastName TEXT,
			StreetName TEXT,
			HouseNameNumber TEXT,
			City TEXT,
			PostCode TEXT,
			Email TEXT,
			ContactNumber INTEGER,
			IsPrivate INTEGER
			)""")
conn.commit()

## Creating CarTable
c.execute("""CREATE TABLE CarTable (
			CarId INTEGER PRIMARY KEY,
			RegNumber TEXT,
			Make TEXT,
			Model TEXT,
			ModelVariant TEXT,
			Price REAL,
			YearOfManufacture INTEGER,
			Colour TEXT,
			Mileage INTEGER,
			ModelNumber INTEGER,
			MechanicalNumber INTEGER,
			AffordabilityNumber INTEGER,
			StatisticalDataNumber INTEGER,
			DealrshipNumber INTEGER,								
			FOREIGN KEY(ModelNumber) REFERENCES ModelNoTable(ModelNumber),
			FOREIGN KEY(MechanicalNumber) REFERENCES MechanicalDataTable(MechanicalNumber),
			FOREIGN KEY(AffordabilityNumber) REFERENCES AffordabilityTable(AffordabilityNumber),
			FOREIGN KEY(StatisticalDataNumber) REFERENCES StatisticalDataTable(StatisticalDataNumber),
			FOREIGN KEY(DealrshipNumber) REFERENCES DealerTable(DealrshipNumber)			
			)""")
				
conn.commit()
