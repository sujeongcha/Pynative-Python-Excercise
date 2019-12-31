#Print All Toyota Cars details

#My Solution
df[df.company == 'toyota']

#Given Solution
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
toyotaDf
