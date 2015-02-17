import threading
import time

class SampleThread(Thread):
	def __init__(self, name, interval):
		super(SampleThread, self).__init__()
		self.daemon = True
		self.count = 0
		self.interval = interval
		self.name = name

	def run(salf):
		for _ in range(5):
				time.sleep(self.interval)
				self.count += 1
				print '%s: %d' % (self.name, self.count, )

if __name__ == '__main__':
	t1 = SampleThread('t1', 1)
	t2 = SampleThread('t2', 2)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
