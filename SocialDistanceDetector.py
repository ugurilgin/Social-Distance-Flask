from Configure import Configure 
from ObjectDetection import detectPeople
from scipy.spatial import distance as dist
import numpy as np
import imutils
import cv2
import os
class SocialDistance:
	def __init__(self,filename):
		config=Configure()
		
		self.filename=filename
		self.MODEL_PATH = "yolo-coco"
		self.labelsPath =os.path.sep.join([config.MODEL_PATH(),"coco.names"])
		self.LABELS =open(self.labelsPath).read().strip().split("\n")
		self.weightsPath =os.path.sep.join([config.MODEL_PATH(),"yolov3-tiny.weights"])
		self.configPath= os.path.sep.join([config.MODEL_PATH(),"yolov3-tiny.cfg"])
		print("[INFO] loading YOLO from disk")
	def Detect(self):
		config=Configure()
		
		self.net =cv2.dnn.readNetFromDarknet(self.configPath,self.weightsPath)
		self.ln =self.net.getLayerNames()
		self.ln = [self.ln[i[0]-1]for i in self.net.getUnconnectedOutLayers()]
		print("[INFO] accesing video stream")
		self.vs =cv2.VideoCapture(self.filename)
	

		while True:
			(self.grabbed,self.frame) =self.vs.read()
			if not self.grabbed:
				break
			self.frame = imutils.resize(self.frame,width =700)
			self.results =detectPeople(self.frame,self.net,self.ln,personIdx=self.LABELS.index("person"))
			self.violate =set()
			
			if len(self.results) >=2:
				self.centroids = np.array([r[2] for r in self.results])
				self.D = dist.cdist(self.centroids,self.centroids,metric="euclidean")
				
						
				for i in range(0,self.D.shape[0]):
					for j in range(i+1,self.D.shape[1]):
						if self.D[i,j]<config.MIN_DISTANCE():
							self.violate.add(i)
							self.violate.add(j)
							
							
			for(i,(prob,bbox,centroid)) in enumerate(self.results):
				(startX,startY,endX,endY)=bbox
				(cX,cY)=centroid 
				color=(0,255,0)
				
				if i in self.violate:
					color = (0,0,255)
				cv2.rectangle(self.frame,(startX,startY),(endX,endY),color,2)
				cv2.circle(self.frame,(cX,cY),5,color,1)
			
			text ="Social Distancing Violations: {}".format(len(self.violate))
			cv2.putText(self.frame,text,(10,self.frame.shape[0]-25),cv2.FONT_HERSHEY_SIMPLEX,0.85,(0,0,255),3)
			
			
			test = cv2.imencode('.jpg', self.frame)[1].tobytes()
			yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + test + b'\r\n')
	
			
	def save(self):
		cv2.imwrite("test.png",self.frame)
  