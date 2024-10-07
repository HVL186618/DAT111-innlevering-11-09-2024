# utdatert, ikke kjør dette scriptet
raise e \
    if (e:=InterruptedError("Jeg sa ikke kjør dette scriptet")) else None

csv = open("bhs.csv", "w")
csv.writelines("ID,Som en...,Ønsker jeg...,Slik at...\n")
with (open("Product Backlog.csv", "r", encoding="UTF-8") as file):
    for l in file.read().split("\n")[1:]:
        l = l.split('"')
        try: print(l[1])
        except: continue
        _ = l[1].lower() \
            .replace("som en ", "") \
            .replace("ønsker jeg ", "") \
            .replace("slik at ", "")
        csv.writelines(l[0] + _ + "\n")