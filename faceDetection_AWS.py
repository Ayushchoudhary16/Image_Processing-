import boto3
import cv2
from cv2.data import haarcascades

rekognition = boto3.client('rekognition')

images= './mi.jpeg'
with open(images, 'rb') as image_file:
    image_bytes = image_file.read()

response = rekognition.recognize_celebrities(Image={'Bytes': image_bytes})

image = cv2.imread(images)
h, w, _ = image.shape

for celeb in response['CelebrityFaces']:
    box = celeb['Face']['BoundingBox'] 
    left = int(box['Left'] * w)
    top = int(box['Top'] * h)
    width = int(box['Width'] * w)
    height = int(box['Height'] * h)

    cv2.rectangle(image, (left, top), (left + width, top + height), (0, 255, 0), 2)

    name_position = (left, top -5)  
    cv2.putText(image, celeb['Name'], name_position,
                cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 255), 1)

cv2.imshow("Celebrity Detection", image)
cv2.waitKey(0)==ord('q')
