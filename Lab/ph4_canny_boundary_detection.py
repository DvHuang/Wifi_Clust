import cv2.cv as cv
import math

im=cv.LoadImage('14_108_eae2591dbc033d9.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)

pi = math.pi #Pi value

dst = cv.CreateImage(cv.GetSize(im), 8, 1)

cv.Canny(im, dst, 200, 200)
cv.Threshold(dst, dst, 100, 255, cv.CV_THRESH_BINARY)

#---- Standard ----
color_dst_standard = cv.CreateImage(cv.GetSize(im), 8, 3)
cv.CvtColor(im, color_dst_standard, cv.CV_GRAY2BGR)#Create output image in RGB to put red lines

lines = cv.HoughLines2(dst, cv.CreateMemStorage(0), cv.CV_HOUGH_STANDARD, 1, pi / 180, 100, 0, 0)
for (rho, theta) in lines[:100]:
    a = math.cos(theta) #Calculate orientation in order to print them
    b = math.sin(theta)
    x0 = a * rho
    y0 = b * rho
    pt1 = (cv.Round(x0 + 1000*(-b)), cv.Round(y0 + 1000*(a)))
    pt2 = (cv.Round(x0 - 1000*(-b)), cv.Round(y0 - 1000*(a)))
    cv.Line(color_dst_standard, pt1, pt2, cv.CV_RGB(255, 0, 0), 2, 4) #Draw the line

#---- Probabilistic ----
color_dst_proba = cv.CreateImage(cv.GetSize(im), 8, 3)
cv.CvtColor(im, color_dst_proba, cv.CV_GRAY2BGR) # idem

rho=1
theta=pi/180
thresh = 50
minLength= 120 # Values can be changed approximately to fit your image edges
maxGap= 20

lines = cv.HoughLines2(dst, cv.CreateMemStorage(0), cv.CV_HOUGH_PROBABILISTIC, rho, theta, thresh, minLength, maxGap)
for line in lines:
    cv.Line(color_dst_proba, line[0], line[1], cv.CV_RGB(255, 0, 0), 2, 8)

cv.ShowImage('Image',im)
cv.ShowImage("Cannied", dst)
cv.ShowImage("Hough Standard", color_dst_standard)
cv.ShowImage("Hough Probabilistic", color_dst_proba)
cv.WaitKey(0)
