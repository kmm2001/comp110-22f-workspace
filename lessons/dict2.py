schools = dict[str, int]
schools = dict()
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150
print(schools)
print(f"UNC has {schools['UNC']} students")
schools.pop("Duke")
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")
print(schools)
if "Duke" in schools:
    print("found")
else:
    print("no key")