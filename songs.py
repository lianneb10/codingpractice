kpopArtists = [
  {"name": "BLACKPINK", "listens": 22240411},
  {"name": "(G)I-DLE", "listens": 8897118},
  {"name": "BTS", "listens": 40343927},
  {"name": "NAYEON", "listens": 4968436},
  {"name": "Stray Kids", "listens": 8057702},
  {"name": "Jessi", "listens": 3177550},
]

def mostListens():
    topListens = 0
    artistTop = ""
    for artist in kpopArtists:
        if topListens < artist["listens"]:
            topListens = artist["listens"]
            artistTop = artist["name"]
    return (artistTop, topListens)

print(mostListens())
    # print(artist["name"], artist["listens"])

def minListens():
    bottomListens = float("inf")
    artistBottom = ""
    for artist in kpopArtists:
        if bottomListens > artist["listens"]:
            bottomListens = artist["listens"]
            artistBottom = artist["name"]
    return (artistBottom, bottomListens)

print(minListens())
