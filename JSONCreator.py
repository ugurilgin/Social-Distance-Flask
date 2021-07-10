import json
mobese={}
mobese['Sultanbeyli']={
'id':'1',
'name':'Sultanbeyli',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_sultanbeyli_meydan.stream/playlist.m3u8',
'img':'#'
}

mobese['Esenler']={
'id':'2',
'name':'Esenler',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_esenler_meydan.stream/playlist.m3u8',
'img':'#'
}
mobese['Uskudar']={
'id':'3',
'name':'Üsküdar',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_uskudar.stream/playlist.m3u8',
'img':'#'
}
mobese['Zeytinburnu']={
'id':'4',
'name':'Zeytinburnu',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_uskudar.stream/playlist.m3u8',
'img':'#'
}
mobese['Kucukcekmece']={
'id':'5',
'name':'Küçükçekmece',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_kucukcekmece.stream/playlist.m3u8',
'img':'#'
}
mobese['Ortakoy']={
'id':'6',
'name':'Ortaköy',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_ortakoy.stream/playlist.m3u8',
'img':'#'
}

data=json.dumps(mobese)
with open ("mobese.json","w") as file:
    file.write(data)