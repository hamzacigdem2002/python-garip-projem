print("Penis boyu hesaplama programına hoşgeldiniz")

while True:
    print("\nLütfen yapmak istediğiniz işlemi seçin:")
    print("1. Kilo, ayak numarası ve boy ile hesaplama")
    print("2. İşaret parmak boyu ile hesaplama")
    print("3. Çıkış")

    secim = input("Seçiminiz (1/2/3): ")

    if secim == '1':
        # 1.işlem
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
            
        

    elif secim == '2':
        # 2.işlem
        isaret_parmak_boyu = int(input("İşaret Parmağınızın uzunluğunu giriniz: "))

        dick_size = isaret_parmak_boyu + ( isaret_parmak_boyu / 2 )

        print(f"Yarrağınızın boyu: {dick_size}")


        if dick_size < 10:
            print(f"Penisiniz küçük: {dick_size} ")

        elif 11 <= dick_size < 15:
            print(f"Penisiniz ortalama seviyede: {dick_size}")
            
        elif 16 <= dick_size < 20:
            print(f"Penisiniz büyük: {dick_size}")

        elif 21 <= dick_size < 30:
            print(f"Penisiniz zenci siki gibi: {dick_size}")
            
        

    elif secim == '3':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")





   

