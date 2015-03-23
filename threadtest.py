import threading
##import numpy as np


class ImageProcessing(threading.Thread):
	def __init__(self, windowname):
		threading.Thread.__init__(self)
		threading.Thread.daemon = True
		self.windowname = windowname
		self.capture = cv2.VideoCapture(-1)

	def run(self):
			while True:
				ret, frame = self.capture.read()
				cv2.imshow(self.windowname, frame)

if __name__ == "__main__":

	windowname = "ImageProcessing"
	cv2.namedWindow(windowname)

	ip = ImageProcessing(windowname)
	ip.start()

	while True:
		if cv2.waitKey(10) == 27: # ESC
			break