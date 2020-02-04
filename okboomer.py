boomer_years = list(range(1946, 1965))
genx_years = list(range(1965, 1981))
millennial_years = list(range(1981, 1997))
genz_years = (list(range(1997, 2010)))
genalpha_years = (list(range(2011, 2026)))
allyears = (list(range(1946, 2026)))

year = (int(input("What year were you born? ")))
if year in boomer_years:
    print("Okay, boomer.")
elif year in genx_years:
    print ("I literally don't know anything about Gen X so I don't know what to put here lol")
elif year in millennial_years:
    print("What industry are you ruining now?")
elif year in genz_years:
    print("So you're responsible for \"Okay, boomer\"?")
elif year in genalpha_years:
    print("[insert something negative about gen alpha here]")
else:
    print("uh idk lol")

    # this is a random comment
    