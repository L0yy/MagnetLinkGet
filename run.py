from tpblite import TPB, CATEGORIES, ORDERS
t = TPB('https://tpb.party')
namelist = []
#read you wat to down movices name
with open("MovicesList.txt","r") as f:
    namelist = f.readlines()

for name in namelist:
    try:
        #torrents = t.search(name.strip(), order=ORDERS.SEEDERS.DES, category=CATEGORIES.VIDEO.HD_MOVIES)
        torrents = t.search(name.strip(), order=ORDERS.SEEDERS.DES)
        torrent = torrents[0]
        print("[*] Get success: {}".format(torrent.title))
        #linesinfo = "{},{}\n".format(torrent.title,torrent.magnetlink)
        linesinfo = torrent.magnetlink + "\n"
        with open("MovicesMagnetlinkList.txt","a+") as f2:
            f2.write(linesinfo)
    except:
        print("{} not find".format(name.strip()))