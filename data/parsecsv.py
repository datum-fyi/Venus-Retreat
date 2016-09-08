import csv
import json

# csvfile = open('edu_net_enrol.csv', 'r')
# jsonfile = open('edu_net_original.json', 'w')

# fieldnames = ("Country Name","Country Code","Indicator Name","Indicator Code","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015")
# reader = csv.DictReader( csvfile, fieldnames)
# jsonfile.write('[')
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write(',')
#     jsonfile.write('\n')
# jsonfile.write(']')

jsonfile = open('edu_net_original.json', 'r')
edu_data = json.load(jsonfile)
jsonfile.close()

jsonfile = open('wo_ju.json', 'r')
woju_data = json.load(jsonfile)
jsonfile.close()

# new_data = {}

# for country in gdp_data["data"]:
# 	new_data[country['Country Code']] = {}
# 	new_data[country['Country Code']]['gdp_data'] = {}
# 	for key in country:
# 		if country[key] != "" and key != "null" and key != "Indicator Code" and key != "Indicator Name":
# 			if key[0] == "2":
# 				new_data[country['Country Code']]['gdp_data'][key] = country[key]
# 			elif key[0] == "1":	
# 				pass
# 			else:	
# 				new_data[country['Country Code']][key] = country[key]	

# for country in new_data:
# 	year = woju_data[country]["Country Low Year"]
# 	if year != "null":
# 		year = str(year)
# 		print new_data[country]
# 		if year in new_data[country]['gdp_data']:
# 			new_data[country]["GDP for Wo_Ju Low"] = new_data[country]['gdp_data'][year]
# 		elif '2014' in new_data[country]['gdp_data']:	
# 			new_data[country]["GDP for Wo_Ju Low"] = new_data[country]['gdp_data']['2014']
# 		elif '2010' in new_data[country]['gdp_data']:	
# 			new_data[country]["GDP for Wo_Ju Low"] = new_data[country]['gdp_data']['2010']	


new_data = {}

for country in edu_data["data"]:
	new_data[country['Country Code']] = {}
	new_data[country['Country Code']]['edu_data'] = {}
	for key in country:
		if country[key] != "" and key != "null" and key != "Indicator Code" and key != "Indicator Name":
			if key[0] == "2":
				new_data[country['Country Code']]['edu_data'][key] = country[key]
			elif key[0] == "1":	
				pass
			else:	
				new_data[country['Country Code']][key] = country[key]	

for country in new_data:
	year = woju_data[country]["Country Low Year"]
	if year != "null":
		year = str(year)
		print new_data[country]
		if year in new_data[country]['edu_data']:
			new_data[country]["EDU for Wo_Ju Low"] = new_data[country]['edu_data'][year]
		elif '2014' in new_data[country]['edu_data']:	
			new_data[country]["EDU for Wo_Ju Low"] = new_data[country]['edu_data']['2014']
		elif '2010' in new_data[country]['edu_data']:	
			new_data[country]["EDU for Wo_Ju Low"] = new_data[country]['edu_data']['2010']	
		

# for country in data["data"]:
# 	new_data[country['Country Code']] = {}
# 	new_data[country['Country Code']]['percentage_data'] = {}
# 	for key in country:
# 		if country[key] != "" and key != "null" and key != "Indicator Code" and key != "Indicator Name":
# 			if key[0] == "2":
# 				new_data[country['Country Code']]['percentage_data'][key] = country[key]
# 			else:	
# 				new_data[country['Country Code']][key] = country[key]

# for country in new_data:
# 	result_year = 2000
# 	for result in new_data[country]['percentage_data']:
# 		current_year = int(result)
# 		print "the current year is " + str(current_year)
# 		if current_year > result_year:
# 			result_year = current_year
# 		print "the result year is "  + str(result_year)	
# 	if result_year != 2000:		
# 		new_data[country]['Country Low Year'] = result_year
# 		new_data[country]['Country Low Percentage'] = float(new_data[country]['percentage_data'][str(result_year)])
# 	else:
# 		new_data[country]['Country Low Year'] = "null"
# 		new_data[country]['Country Low Percentage'] = "null"
					


jsonfile = open("edu_net.json", "w+")
jsonfile.write(json.dumps(new_data))
jsonfile.close()			


