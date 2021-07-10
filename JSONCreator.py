import json
mobese={}
mobese['Sultanbeyli']={
'id':'1',
'name':'Sultanbeyli',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_sultanbeyli_meydan.stream/playlist.m3u8',
"img": "assets/images/city/sultanbeyli.png"
}

mobese['Esenler']={
'id':'2',
'name':'Esenler',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_esenler_meydan.stream/playlist.m3u8',
"img": "assets/images/city/esenler.png"
}
mobese['Uskudar']={
'id':'3',
'name':'Üskudar',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_uskudar.stream/playlist.m3u8',
"img": "assets/images/city/uskudar.jpg"
}
mobese['Zeytinburnu']={
'id':'4',
'name':'Zeytinburnu',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_uskudar.stream/playlist.m3u8',
"img": "assets/images/city/zeytinburnu.png"
}
mobese['Kcekmece']={
'id':'5',
'name':'Kcekmece',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_kucukcekmece.stream/playlist.m3u8',
"img": "assets/images/city/kucukcekmece.jpg"
}
mobese['Ortakoy']={
'id':'6',
'name':'Ortakoy',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_ortakoy.stream/playlist.m3u8',
"img": "assets/images/city/ortakoy.png"
}

data=json.dumps(mobese)
with open ("mobese.json","w") as file:
    file.write(data)