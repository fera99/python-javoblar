lugat = {
    'boolean':"mantiqiy qiymat",
    'float':'o\'nlik son',
    'if':'shartlarni tekshirish operatori',
    'for':'sikl',
    'integer':'butun son'

}
for k, q in sorted(lugat.items()):
    print(f"{k.title()}-{q.title()}")

davlatlar = {
    'Uzbekiston':'Toshkent',
    'Rossiya':'Moskva',
    'AQSH':'Washington',
    'Koreya':'Seul',
    'Eron':'Tehron',
    'Italiya':'Rim',
    'Germaniya':'Berlin'
}
print("Dunyo davlatlari:")
for dav in sorted(davlatlar):
    print (dav.upper())

print("\nDunyo poytaxtlari")
for poy in sorted(davlatlar.values()):
    print(poy.title())

davlat = input("Qaysi davlatning poytaxtini bilishni xohlaysiz? ")
poytaxt = davlatlar.get(davlat)
if poytaxt ==None:
    print("Kechirasiz bizda bu haqida ma\'lumot yo\'q.")
else:
    print(f"{davlat.upper()}ning poytaxti bu {poytaxt.title()} shahri.")

menu = {
    'osh':15000,
    'manti':10000,
    'non':3000,
    'baliq':25000,
    'somsa':5000,
    'salat':14000
}
print("3 ta taom buyurtma bering")
buyurtmalar =[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so\'m.")
    else:
        print(f"Bizda {buyurtma} yo\'q")