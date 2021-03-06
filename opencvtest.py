﻿# -*- coding: utf-8 -*-
import numpy as np
import cv2

# 対応付けされた特徴点同士を線で結ぶ
def drawMatches(im1, kp1, im2, kp2, matches):
	rows1 = im1.shape[0]
	cols1 = im1.shape[1]
	rows2 = im2.shape[0]
	cols2 = im2.shape[1]
	out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')
	out[:rows1,:cols1,:] = np.dstack([im1, im1, im1])
	out[:rows2,cols1:cols1+cols2,:] = np.dstack([im2, im2, im2])
	for mat in matches:
		im1_idx = mat.queryIdx
		im2_idx = mat.trainIdx
		(x1,y1) = kp1[im1_idx].pt
		(x2,y2) = kp2[im2_idx].pt
		cv2.circle(out, (int(x1),int(y1)), 4, (0, 0, 255), 1)
		cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (0, 0, 255), 1)
		cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (0, 0, 255), 3)

	return out

# メイン関数
def main():
	im1 = cv2.imread("hoge.jpg",0)# 画像1の取得
	im2 = cv2.imread("piyo.jpg",0)# 画像2の取得
	# 特徴点の抽出・特徴量の記述
	star = cv2.FeatureDetector_create("STAR")
	brief = cv2.DescriptorExtractor_create("BRIEF")
	kp1 = star.detect(im1,None)
	kp1, des1 = brief.compute(im1,kp1)
	kp2 = star.detect(im2,None)
	kp2, des2 = brief.compute(im2,kp2)
	##特徴点マッチング
	bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
	matches = bf.match(des1,des2)
	matches = sorted(matches, key = lambda x:x.distance)
	im3 = drawMatches(im1,kp1,im2,kp2,matches[:10])
	cv2.imwrite("BRIEFmatch.png",im3)

if __name__ == '__main__':
	main()
