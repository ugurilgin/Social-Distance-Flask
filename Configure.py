class Configure(object):
    def __init__(self):
        self.MODEL_PATHS="yolo-coco"
        self.MIN_CONFIDS=0.3
        self.NMS_THRESHLDS=0.3
        self.MIN_DISTANCES=50
    def MODEL_PATH(self):
        return self.MODEL_PATHS
    def MIN_CONFID(self):
        return self.MIN_CONFIDS
    def NMS_THRESHLD(self):
        return self.NMS_THRESHLDS
    def MIN_DISTANCE(self):
        return self.MIN_DISTANCES