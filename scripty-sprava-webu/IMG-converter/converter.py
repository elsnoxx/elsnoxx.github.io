import os



# Zadejte cestu k dané složce
path = 'C:\\Users\\admin\\Documents\\GitHub\\elsnoxx.github.io\\img'

# Rekurzivní procházení všech podsložek a souborů
for root, dirs, files in os.walk(path):
    print(f"Složka: {root}")
    print("Soubory:")
    for file in files:
        print(os.path.join(root, file))
