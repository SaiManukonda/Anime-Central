import wikipedia
import csv
from image import *
import difflib
import re
import json

categories = ["action", "adventure", "comedy", "cooking", "drama", "fantasy", "harem", "hentai", "horror", "mecha", "mystery", "romance", "science", "slice", "sports", "yaoi", "yuri"]

#given an anime title, it will find its genre and returns it in a list
def getGenre(AnimeTitle):
    genres = []
    temp1 = wikipedia.WikipediaPage(AnimeTitle).categories
    for item in temp1:
     for category in categories:
        temp = item.split()
        a = (map(lambda x: x.lower(), temp))
        b = list(a)
        if category in b:
            if category == "science":
                genres.append("science fiction")
            elif category == "slice":
                genres.append("slice of life")
            else:
                genres.append(category) 
    return list(dict.fromkeys(genres))

#given an anime title, it will get its poster and returns it, if no image was found it will return "No image"
def getMainImage(AnimeTitle):
    try:
     temp = wikipedia.WikipediaPage(AnimeTitle).images
     for img in temp:
                if(getHeight(img) < 500 and getHeight(img) > 300 and getWidth(img) > 200 and getWidth(img) < 300):
                  return img
     return "No image"
    except:
        return "No image"

def search(AnimeTitle):
    animes = dict()
    d = open("AnimeImages2.csv", "r")
    i = 0
    while i < 3900:
     temp = d.readline().strip()
     temp2 = temp.split(",https")
     try:
        animes[temp2[0]] = "https"+temp2[1]
     except:
        pass
     i+=1
    if(AnimeTitle == "None"):
        return animes
    temp = difflib.get_close_matches(AnimeTitle, animes, n=10, cutoff=0.4)
    for anime in animes:
     temp2 = re.findall(r"[\w']+|[.,!?;]", anime)
     a = list((map(lambda x: x.lower(), temp2)))
     if(AnimeTitle.lower() in a):
        temp.append(anime)
    temp = list(dict.fromkeys(temp))
    animez = {}
    for anime in animes:
        if anime in temp:
            animez[anime] = animes[anime]
    return animez

def getImages(link):
 temp = wikipedia.WikipediaPage(link).links
 with open('AnimeImages2.csv', 'a') as f:
  writer = csv.writer(f)
  for item in temp:
     temp2 = getMainImage(item)
     if(not temp2 == 'No image'):
         writer.writerow([item,temp2])

def Genres():
    dict = {}
    d = open("AnimeImages2.csv", "r")
    i = 0
    while i < 3900:
     temp = d.readline().strip()
     temp2 = temp.split(",https")
     try:
        dict[temp2[0]] = {}
        dict[temp2[0]]['image_url'] = "https"+temp2[1]
        dict[temp2[0]]['genres'] = getGenre(temp2[0])
     except:
        pass
     i+=1
    with open("AnimeInfo.json", "w") as outfile:
     json.dump(dict, outfile)

def getAnimeByGenre(Genre):
    if not Genre in categories:
        return None
    with open("AnimeInfo.json") as json_file:
     data = json.load(json_file)
    print(data)

