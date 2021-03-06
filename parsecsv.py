import csv
import json

# csvfile = open('women_justification.csv', 'r')
# jsonfile = open('wo_ju.json', 'w')

# fieldnames = ("Country Name","Country Code","Indicator Name","Indicator Code","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015")
# reader = csv.DictReader( csvfile, fieldnames)
# jsonfile.write('[')
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write(',')
#     jsonfile.write('\n')
# jsonfile.write(']')

jsonfile = open('wo_ju.json', 'r')
data = json.load(jsonfile)
jsonfile.close()

for country in data:
	print country
	for key in country:
		if country[key] == "":
			delete data[country][key]

jsonfile = open("wo_ju_nice.json", "w+")
jsonfile.write(json.dumps(data, indent = 3))
jsonfile.close()			


