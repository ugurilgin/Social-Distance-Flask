import json
mobese={}
mobese['SultanBeyli']={
'id':'1',
'name':'SultanBeyli',
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
'name':'Uskudar',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_uskudar.stream/playlist.m3u8',
'img':'#'
}
mobese['ZeytinBurnu']={
'id':'4',
'name':'ZeytinBurnu',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_uskudar.stream/playlist.m3u8',
'img':'#'
}
mobese['KucukCekmece']={
'id':'5',
'name':'Kucuk Cekmece',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_kucukcekmece.stream/playlist.m3u8',
'img':'#'
}
mobese['Ortakoy']={
'id':'6',
'name':'Ortakoy',
'link':'https://livestream.ibb.gov.tr/cam_sehir/cam_ortakoy.stream/playlist.m3u8',
'img':'#'
}

data=json.dumps(mobese)
with open ("mobese.json","w") as file:
    file.write(data)