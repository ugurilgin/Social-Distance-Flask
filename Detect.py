from SocialDistanceDetector import SocialDistance
import json
class Main:
    def __init__(self):
        #socialdistance=SocialDistance( "https://livestream.ibb.gov.tr/cam_sehir/cam_sultanbeyli_meydan.stream/playlist.m3u8")
        socialdistance=SocialDistance( "https://livestream.ibb.gov.tr/cam_sehir/cam_sultanbeyli_meydan.stream/playlist.m3u8")

        socialdistance.Detect()
        socialdistance.save()
        f = open('mobese.json',)
    
        data = json.load(f)
        
        # Iterating through the json
        # list
        for i in data:
            print(i)
        
        # Closing file
        f.close()
if __name__ == "__main__":
    Main()