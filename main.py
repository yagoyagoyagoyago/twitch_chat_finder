import requests
from termcolor import colored
nm = input("Twitch Channel: ").lower().strip()
super_db = []
def following(pessoa):
    headers1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
                "Accept": "*/*", "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
                "Authorization": "OAuth z0xwee1uwt1to4mh94rjyquibzqaxj"}
    data = '[{"operationName":"ChatViewers","variables":{"channelLogin":"yyy123yyy"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"e0761ef5444ee3acccee5cfc5b834cbfd7dc220133aa5fbefe1b66120f506250"}}}]'.replace(
        "yyy123yyy", pessoa.lower())
    url = "https://gql.twitch.tv/gql"
    try:
        json = requests.post(url, data=data, headers=headers1).json()
        user_id = json[0]["data"]["channel"]["id"]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101",
                   "Accept": "application/vnd.twitchtv.v5+json", "Client-ID": "ff0597he55udf9sevbouqrpliumwnr"}
        st = "https://api.twitch.tv/kraken/users/" + user_id + "/follows/channels?limit=100&sortby=last_broadcast"
        rslt = requests.get(st, headers=headers).json()
        for c in rslt["follows"]:
            if super_db.count(c["channel"]["display_name"]) == 0:
               super_db.append(c["channel"]["display_name"])
    except:
        print("O_o")
def chatlist(chan):
    try:
        users = []
        headers2 = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
                   "Accept":"*/*", "Client-Id":"kimne78kx3ncx6brgo4mv6wki5h1ko",
                   "Authorization":"OAuth z0xwee1uwt1to4mh94rjyquibzqaxj"}
        data2 = '[{"operationName":"ChatViewers","variables":{"channelLogin":"yyy123yyy"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"e0761ef5444ee3acccee5cfc5b834cbfd7dc220133aa5fbefe1b66120f506250"}}}]'.replace("yyy123yyy", chan)
        url2 = "https://gql.twitch.tv/gql"
        json1 = requests.post(url2, data=data2, headers=headers2).json()
        viewers = json1[0]["data"]["channel"]["chatters"]["viewers"]
        vips = json1[0]["data"]["channel"]["chatters"]["vips"]
        mods = json1[0]["data"]["channel"]["chatters"]["moderators"]
        for mod in mods:
            users.append(mod["login"])
        for vip in vips:
            users.append(vip["login"])
        for viewer in viewers:
            users.append(viewer["login"])
        return users
    except:
        print("O_o")
following(nm)
try:
    for usuario in super_db:
        list = chatlist(str(usuario).lower())
        if nm in list:
            print("{}{}{}{}".format(colored("Encontrado, o ", "green"), colored(nm, "yellow"), colored(" está no chat do ", "green"),colored(usuario, "red")))
        else:
            print("{}".format(colored("Ainda não foi encontrado :(", "cyan")))
except:
    print("{}".format(colored("Ainda não foi encontrado :(", "cyan")))