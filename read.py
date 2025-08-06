# below code is used to detect a ball in a video using OpenCV, not in use for now


# import cv2
# import numpy as np

# # Load the video
# cap = cv2.VideoCapture('/Users/lilahu/Desktop/Code/open-cv-practice/Videos/fanZhenDong.mp4')

# # Get video properties
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280, 720))

# # Read initial frames
# ret, frame1 = cap.read()
# ret, frame2 = cap.read()

# while cap.isOpened() and ret:
#     # Colour filtering (for white ball)
#     hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv, (0, 0, 180), (180, 50, 255))  # Adjust if ball is orange
#     filtered = cv2.bitwise_and(frame1, frame1, mask=mask)

#     # Motion detection
#     diff = cv2.absdiff(frame1, frame2)
#     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     _, thresh = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)
#     dilated = cv2.dilate(thresh, None, iterations=2)
#     contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     # Loop over contours to find small fast-moving objects
#     for contour in contours:
#         area = cv2.contourArea(contour)
#         if 5 < area < 300:  # Adjust area range for ball size
#             x, y, w, h = cv2.boundingRect(contour)
#             cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     # Optional: Circle detection (HoughCircles)
#     gray_filtered = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
#     circles = cv2.HoughCircles(gray_filtered, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
#                                param1=50, param2=15, minRadius=2, maxRadius=10)

#     if circles is not None:
#         circles = np.uint16(np.around(circles))
#         for (x, y, r) in circles[0, :]:
#             cv2.circle(frame1, (x, y), r, (255, 0, 0), 2)
#             cv2.putText(frame1, "Detected Ball", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
#                         0.5, (255, 0, 0), 1)

#     # Output frame
#     resized = cv2.resize(frame1, (1280, 720))
#     out.write(resized)
#     cv2.imshow("Ball Tracker", frame1)

#     # Prepare next frame
#     frame1 = frame2
#     ret, frame2 = cap.read()

#     if cv2.waitKey(30) & 0xFF == 27:
#         break

# # Cleanup
# cap.release()
# out.release()
# cv2.destroyAllWindows()
