import boto3
import cv2
from cv2.data import haarcascades

rekognition = boto3.client('rekognition')

images= './fruits.jpeg'
with open(images, 'rb') as image_file:
    image_bytes = image_file.read()

response = rekognition.detect_labels(Image={'Bytes': image_bytes})

image = cv2.imread(images)
h, w, _ = image.shape

for label in response['Labels']:
    for instance in label.get('Instances', []):
        box = instance['BoundingBox']
        left = int(box['Left'] * w)
        top = int(box['Top'] * h)
        width = int(box['Width'] * w)
        height = int(box['Height'] * h)

        cv2.rectangle(image, (left, top), (left + width, top + height), (0, 255, 0), 2)

        name_position = (left, top -1)
        cv2.putText(image, label['Name'], name_position,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1)

cv2.imshow("Celebrity Detection", image)
cv2.waitKey(0)==ord('q')
