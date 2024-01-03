from Cars import bmw, audi, nissan

user = input("Enter a BMW model:")
start = int(input("Enter the Starting year:"))
end = int(input("Enter the Ending year:"))

bmw_car = bmw.BMW(user, start, end)
print(bmw_car.start())
print(bmw_car.stop())

user = input("Enter an AUDI model:")
start = int(input("Enter the Starting year:"))
end = int(input("Enter the Ending year:"))

audi_car = audi.AUDI(user, start, end)
print(audi_car.start())
print(audi_car.stop())

user = input("Enter a NISSAN model:")
start = int(input("Enter the Starting year:"))
end = int(input("Enter the Ending year:"))

nissan_car = nissan.NISSAN(user, start, end)
print(nissan_car.start())
print(nissan_car.stop())
