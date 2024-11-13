bozorlik=[
    "Kartishka",
    "Piyoz",
    "Karam"
]
bozorlik2=["Kartoshka","Piyoz", "Karam", "Bexruz", "Bexruz2"]
# bozorlik2.remove("Piyoz")
bozorlik2.append("Yunus")
bozorlik2.insert(1, "Rasul")
bozorlik2.insert(4, "Eldor")
bozorlik2.pop()
bozorlik2.pop(1)
print(bozorlik2.index("Bexruz2"))
# bozorlik2.clear()
yangibozorlik = bozorlik2.copy()
print(yangibozorlik.count("Bexruz"))
print(yangibozorlik)
yangibozorlik.extend(bozorlik)
print(yangibozorlik)