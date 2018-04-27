import sqlite3

conn = sqlite3.connect('connor.db')

c = conn.cursor()

## Creating ModelNoTable
c.execute("""CREATE TABLE ModelNoTable (
			ModelNumber INTEGER PRIMARY KEY,
			NumberOfSeats INTEGER,
			NumberOfDoors INTEGER,
			BodyType TEXT
			)""")

## Creating MechanicalDataTable
c.execute("""CREATE TABLE MechanicalDataTable (
			MechanicalNumber INTEGER PRIMARY KEY,
			EngineSize REAL,
			GearboxType TEXT,
			Drivetrain TEXT,
			FuelType TEXT
			)""")

## Creating AffordabilityTable
c.execute("""CREATE TABLE AffordabilityTable (
			AffordabilityNumber INTEGER PRIMARY KEY,
			InsuranceGroup TEXT,
			FuelConsumption TEXT,
			AnnualTax REAL
			)""")

## Creating StatisticalDataTable
c.execute("""CREATE TABLE StatisticalDataTable (
			StatisticalDataNumber INTEGER PRIMARY KEY,
			AccelerationTime REAL,
			Co2Emissions TEXT
			)""")

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

## Creating CarTable
c.execute("""CREATE TABLE CarTable (
			RegNumber TEXT PRIMARY KEY,
			Make TEXT,
			Model TEXT,
			ModelVariant TEXT,
			Price REAL,
			YearOfManufacture INTEGER,
			Colour TEXT,
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
