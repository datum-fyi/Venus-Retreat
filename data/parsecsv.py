import csv
import json

# csvfile = open('2016csv.csv', 'r')
# jsonfile = open('spi_2016.json', 'w')

# fieldnames = ("Country","Country Code","Social Progress Index","Basic Human Needs","Foundations of Wellbeing","Opportunity","Nutrition and Basic Medical Care","Water and Sanitation","Shelter","Personal Safety","Access to Basic Knowledge","Access to Information and Communications","Health and Wellness","Environmental Quality","Personal Rights","Personal Freedom and Choice","Tolerance and Inclusion","Access to Advanced Education","Undernourishment","Depth of food deficit","Maternal mortality rate","Child mortality rate","Deaths from infectious diseases","Access to piped water","Rural access to improved water source","Access to improved sanitation facilities","Availability of affordable housing","Access to electricity","Quality of electricity supply","Household air pollution attributable deaths","Homicide rate","Level of violent crime","Perceived criminality","Political terror","Traffic deaths","Adult literacy rate","Primary school enrollment","Lower secondary school enrollment","Upper secondary school enrollment","Gender parity in secondary enrollment","Mobile telephone subscriptions","Internet users","Press Freedom Index","Life expectancy at 60","Premature deaths from non-communicable diseases","Obesity rate","Suicide rate","Outdoor air pollution attributable deaths","Wastewater treatment","Biodiversity and habitat","Greenhouse gas emissions","Political rights","Freedom of speech","Freedom of assembly/association","Freedom of movement","Private property rights","Freedom over life choices","Freedom of religion","Early marriage","Satisfied demand for contraception","Corruption","Tolerance for immigrants","Tolerance for homosexuals","Discrimination and violence against minorities","Religious tolerance","Community safety net","Years of tertiary schooling","Women's average years in school","Inequality in the attainment of education","Globally ranked universities","Percentage of tertiary students enrolled in globally ranked universities","Depth of food deficit - capped","Adult literacy rate - capped","Lower secondary school enrollment - capped","Upper secondary school enrollment - capped","Gender parity in secondary enrollment - difference from parity","Mobile telephone subscriptions - capped","Greenhouse gas emissions - capped","Globally ranked universities - bucketed","Percentage of tertiary students enrolled in globally ranked universities - bucketed")
# reader = csv.DictReader( csvfile, fieldnames)
# jsonfile.write('[')
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write(',')
#     jsonfile.write('\n')
# jsonfile.write(']')

jsonfile = open('spi_2016.json', 'r')
spi_data = json.load(jsonfile)
jsonfile.close()

jsonfile = open('wo_ju.json', 'r')
woju_data = json.load(jsonfile)
jsonfile.close()


new_data = {}

for country in spi_data["data"]:
	new_data[country['Country Code']] = {}
	new_data[country['Country Code']]['spi_data'] = {}
	for key in country:
		if key != "Nutrition and Basic Medical Care" and key != "Country Code" and key != "Country" :	
			pass
		else:
			new_data[country['Country Code']]['spi_data'][key] = country[key]	

for country in new_data:
	if country in woju_data and woju_data[country]["Country Low Percentage"] != "null":
		new_data[country]["In Wo_Ju Data"] = True
	else:
		new_data[country]["In Wo_Ju Data"] = False				

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
					


jsonfile = open("nut_well.json", "w+")
jsonfile.write(json.dumps(new_data))
jsonfile.close()			


