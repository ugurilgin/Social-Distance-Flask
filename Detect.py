from SocialDistanceDetector import SocialDistance
class Main:
    def __init__(self):
        #socialdistance=SocialDistance( "https://livestream.ibb.gov.tr/cam_sehir/cam_sultanbeyli_meydan.stream/playlist.m3u8")
        socialdistance=SocialDistance( "https://livestream.ibb.gov.tr/cam_sehir/cam_zeytin_burnu.stream/playlist.m3u8")

        socialdistance.Detect()
        socialdistance.save()
if __name__ == "__main__":
    Main()