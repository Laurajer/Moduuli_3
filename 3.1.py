# 3.1
# Alle 37cm heitä pois
kuha = float(input("Kuhan pituus senttimetreinä: "))
if kuha < 37:
    alijaama = 37 - kuha
    print(f"Kuha on alamittainen. Jää {alijaama: .2f}cm vajaaksi sallitusta pyyntimitasta. Vapauta kala takaisin järveen.")
