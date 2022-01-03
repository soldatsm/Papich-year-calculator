print("Hello this is a si,ple program to convert current year to Papich year")
year = int(input("Please enter current year: "))
calulus = 2015 + 30
papich_year = 0
year_leng = len(range(2016, year + 1))
if year <= 2014:
    print("Year error, Year should be more the 2014")
elif year == 2015:
    print(f'Current year is {year}, Papich year is {calulus}')
else:
    papich_year = calulus + year_leng * 31
    print(f'Current year is {year}, Papich year is {papich_year}')
