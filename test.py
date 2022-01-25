import difflib
import re
d = open("AnimeImages.csv", "r")
animes = {}
i = 0
while i < 83:
    temp = d.readline().strip()
    temp2 = temp.split(",")
    try:
        animes[temp2[0]] = temp2[1]
    except:
        pass
    i+=1
search = 'titan'
temp = difflib.get_close_matches(search, animes, n=10, cutoff=0.4)
for anime in animes:
    temp2 = re.findall(r"[\w']+|[.,!?;]", anime)
    a = list((map(lambda x: x.lower(), temp2)))
    if(search.lower() in a):
        temp.append(anime)
temp = list(dict.fromkeys(temp))
print(temp)


