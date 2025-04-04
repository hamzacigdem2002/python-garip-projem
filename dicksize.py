print("Penis boyu hesaplama programına hoşgeldiniz")

kilo = float(input("kilonuzu giriniz: "))
ayakno = int(input("ayak numaranızı giriniz: "))
boy = float(input("boyunuzu giriniz: "))

penis_boyu = ( kilo * ayakno ) / boy

print(f"Penis boyunuz: {penis_boyu}") 

if penis_boyu < 10:
    print(f"Penisiniz küçük: {penis_boyu} ")

elif 11 <= penis_boyu < 15:
    print(f"Penisiniz ortalama seviyede: {penis_boyu}")
    
elif 16 <= penis_boyu < 20:
    print(f"Penisiniz büyük: {penis_boyu}")

elif 21 <= penis_boyu < 30:
    print(f"Penisiniz zenci siki gibi: {penis_boyu}")
    
else:
    print("Yanlış değer girdiniz")
    

   

