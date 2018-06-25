
def city_country(city, country, population = ''):
	if population:
		formatted = city.title() + ', ' + country.title() 
		formatted += ' - population ' + population
	else:
		formatted = city.title() + ', ' + country.title() 
	return formatted