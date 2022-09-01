sukupuoli = input("Anna sukupuoli: ")
if sukupuoli == "mies":
    hemoglobiinim = int(input("Anna hemoglobiini arvosi: "))
    if hemoglobiinim <= 134:
     print("Hemoglobiinisi on alhainen.")
    if hemoglobiinim >= 195:
        print("Hemoglobiinisi on korkea.")
        if hemoglobiinim >=134 and hemoglobiinim <195:
            print("Hemoglobiinisi on normaali.")
if sukupuoli == "nainen":
    hemoglobiinin = int(input("Anna hemoglobiini arvosi: "))
if hemoglobiinin <= 117:
    print("Hemoglobiinisi on alhainen.")
if hemoglobiinin >= 175:
    print("Hemoglobiinisi on korkea.")
if hemoglobiinin >=117 and hemoglobiinin <175:
    print("Hemoglobiinisi on normaali.")