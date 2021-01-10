def bank(a, years):
    sum=a;
    for i in range(1, years):
         sum*=1.1;
    print("Через ", years, " лет вы получите ", round(sum, 2), " рублей")

a = int(input("Введите количество взятых денег: "))
years = int(input("Введите количество лет, на которое вы вкладываете: "))
bank(a, years)