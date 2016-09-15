import csv
import json

# csvfile = open('continents.csv', 'r')
# jsonfile = open('continents.json', 'w')

# fieldnames = ("name","alpha-2","alpha-3","country-code","iso_3166-2","region","sub-region","region-code","sub-region-code")
# reader = csv.DictReader( csvfile, fieldnames)
# jsonfile.write('[')
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write(',')
#     jsonfile.write('\n')
# jsonfile.write(']')

# jsonfile = open('wo_ju.json', 'r')
# woju_data = json.load(jsonfile)
# jsonfile.close()

# jsonfile = open('edu_net.json', 'r')
# edu_data = json.load(jsonfile)
# jsonfile.close()

# jsonfile = open('gdp_cap.json', 'r')
# gdp_data = json.load(jsonfile)
# jsonfile.close()

# jsonfile = open('nut_well.json', 'r')
# nut_data = json.load(jsonfile)
# jsonfile.close()

# jsonfile = open('marriage_nice.json', 'r')
# mar_data = json.load(jsonfile)
# jsonfile.close()

# jsonfile = open('con_nice.json', 'r')
# con_data = json.load(jsonfile)
# jsonfile.close()

# jsonfile = open('d3_ready_nice.json', 'r')
# agg_data = json.load(jsonfile)
# jsonfile.close()


# for country in agg_data:
# 	country["Region"] = con_data[country["Country Code"]]


jsonfile = open('d3_ready_con.json', 'r')
ready_data = json.load(jsonfile)
jsonfile.close()

jsonfile = open('world_countries.json', 'r')
world_data = json.load(jsonfile)
jsonfile.close()


for country in ready_data:
	code = country['Country Code']
	for country_w in world_data['features']:
		if country_w['id'] == code:
			country_w['ex_data'] = country



jsonfile = open("world_countries_ready.json", "w+")
jsonfile.write(json.dumps(world_data))
jsonfile.close()			





# new_data = {}

# for country in woju_data:
# 	if woju_data[country]["Country Low Percentage"] != "null":
# 		new_data[woju_data[country]['Country Code']] = {}
# 		new_data[woju_data[country]['Country Code']]["Country Name"] = woju_data[country]["Country Name"]
# 		new_data[woju_data[country]['Country Code']]["Country Code"] = woju_data[country]["Country Code"]
# 		new_data[woju_data[country]['Country Code']]["Justification Percentage"] = float(woju_data[country]["Country Low Percentage"])

# for country in edu_data:
# 	if "EDU for Wo_Ju Low" in edu_data[country]:
# 		new_data[edu_data[country]['Country Code']]["Education Percentage"] = float(edu_data[country]["EDU for Wo_Ju Low"])

# for country in gdp_data:
# 	if "GDP for Wo_Ju Low" in gdp_data[country]:
# 		new_data[gdp_data[country]['Country Code']]["GDP Capita"] = float(gdp_data[country]["GDP for Wo_Ju Low"])

# for country in nut_data:
# 	if nut_data[country]["In Wo_Ju Data"] == True and nut_data[country]['spi_data']["Nutrition and Basic Medical Care"] != "":
# 		new_data[nut_data[country]['spi_data']['Country Code']]["NutWell Score"] = float(nut_data[country]['spi_data']["Nutrition and Basic Medical Care"])					
# 	if nut_data[country]["In Wo_Ju Data"] == True and nut_data[country]['spi_data']["Nutrition and Basic Medical Care"] == "":
# 		new_data[nut_data[country]['spi_data']['Country Code']]["NutWell Score"] = "null"

# for country in mar_data:
# 	if mar_data[country]['spi_data']["Early marriage"] != "" and country in new_data:
# 		print "yay"
# 		new_data[mar_data[country]['spi_data']['Country Code']]["Marriage Score"] = float(mar_data[country]['spi_data']["Early marriage"])					
# 	if mar_data[country]['spi_data']["Early marriage"] == "" and country in new_data:
# 		new_data[mar_data[country]['spi_data']['Country Code']]["Marriage Score"] = "null"		

# new_data = {}

# for country in spi_data["data"]:
# 	new_data[country['Country Code']] = {}
# 	new_data[country['Country Code']]['spi_data'] = {}
# 	for key in country:
# 		if key != "Early marriage" and key != "Country Code" and key != "Country" :	
# 			pass
# 		else:
# 			new_data[country['Country Code']]['spi_data'][key] = country[key]	

# for country in new_data:
# 	if country in woju_data and woju_data[country]["Country Low Percentage"] != "null":
# 		new_data[country]["In Wo_Ju Data"] = True
# 	else:
# 		new_data[country]["In Wo_Ju Data"] = False				

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


# new_data = {}

# for country in edu_data["data"]:
# 	new_data[country['Country Code']] = {}
# 	new_data[country['Country Code']]['edu_data'] = {}
# 	for key in country:
# 		if country[key] != "" and key != "null" and key != "Indicator Code" and key != "Indicator Name":
# 			if key[0] == "2":
# 				new_data[country['Country Code']]['edu_data'][key] = country[key]
# 			elif key[0] == "1":	
# 				pass
# 			else:	
# 				new_data[country['Country Code']][key] = country[key]	

# for country in new_data:
# 	year = woju_data[country]["Country Low Year"]
# 	if year != "null":
# 		year = str(year)
# 		print new_data[country]
# 		if year in new_data[country]['edu_data']:
# 			new_data[country]["EDU for Wo_Ju Low"] = new_data[country]['edu_data'][year]
# 		elif '2014' in new_data[country]['edu_data']:	
# 			new_data[country]["EDU for Wo_Ju Low"] = new_data[country]['edu_data']['2014']
# 		elif '2010' in new_data[country]['edu_data']:	
# 			new_data[country]["EDU for Wo_Ju Low"] = new_data[country]['edu_data']['2010']	
		

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


# jsonfile = open('aggregate_nice.json', 'r')
# agg_data = json.load(jsonfile)
# jsonfile.close()

# new_data = {}
# count = 0
# for country in agg_data:
# 	print country
# 	if "Justification Percentage" in agg_data[country] and "Country Code" in agg_data[country] and "GDP Capita" in agg_data[country] and "Country Name" in agg_data[country] and "NutWell Score" in agg_data[country] and "Marriage Score" in agg_data[country] and "Education Percentage" in agg_data[country]:
# 		count += 1
# 		new_data[country] = agg_data[country]
# print count				

# jsonfile = open('aggregate_nice.json', 'r')
# agg_data = json.load(jsonfile)
# jsonfile.close()

# #emp_data = employee_parsed['employee_details']

# #open a file for writing

# aggreg = open('AggData.csv', 'w')

# # create the csv writer object

# csvwriter = csv.writer(aggreg)

# count = 0

# for country in agg_data[0]:

# 	print country
# 	if count == 0:

# 		header = agg_data[0][country].keys()

# 		csvwriter.writerow(header)

# 		count += 1
	
# 	csvwriter.writerow(agg_data[0][country].values())

# aggreg.close()
					
# jsonfile = open('aggregate_nice.json', 'r')
# agg_data = json.load(jsonfile)
# jsonfile.close()

# new_data = []

# for country in agg_data:
# 	new_data.append(agg_data[country])

# print new_data



# jsonfile = open("d3_ready.json", "w+")
# jsonfile.write(json.dumps(agg_data))
# jsonfile.close()			


