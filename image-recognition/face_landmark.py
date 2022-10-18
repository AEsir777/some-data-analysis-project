import PIL.Image
import PIL.ImageDraw
import face_recognition
from pathlib import Path
from PIL import Image

param = 1

img = face_recognition.load_image_file('face2.jpg')

if param == 0:
    face_locations = face_recognition.face_locations(img, number_of_times_to_upsample=2)
    face_landmarks_list = face_recognition.face_landmarks(img, face_locations=face_locations)

    pil_image = PIL.Image.fromarray(img)

    draw = PIL.ImageDraw.Draw(pil_image, 'RGBA')

    for face_landmarks in face_landmarks_list:
        # Loop over each facial feature (eye, nose, mouth, lips, etc)
        for name, list_of_points in face_landmarks.items():
            # Print the location of each facial feature in this image
            print("The {} in this face has the following points: {}".format(name, list_of_points))
            # Let's trace out each facial feature in the image with a line!
            draw.polygon(face_landmarks["left_eyebrow"], fill=(0, 0, 0, 50), width=3)
            draw.polygon(face_landmarks["right_eyebrow"], fill=(256, 256, 256, 50), width=3)

            # Draw over the lips
            draw.polygon(face_landmarks["top_lip"], fill=(128, 0, 128, 100))
            draw.polygon(face_landmarks["bottom_lip"], fill=(128, 0, 128, 100))
    pil_image.show()
else:
    img_encoding = face_recognition.face_encodings(img)[0]

    best_face_distance = 1.0
    best_face_image = None
    best_path = ""

    for image_path in Path("../../Ex_Files_Deep_Learning_Face_Recog/Exercise Files/Ch07/people").glob("*.png"):
        unknown_image = face_recognition.load_image_file(image_path)

        unknown_encodings = face_recognition.face_encodings(unknown_image)
        face_distance = face_recognition.face_distance(img_encoding, unknown_encodings)[0]

        if face_distance < best_face_distance:
            best_face_image = unknown_image
            best_face_distance = face_distance
            best_path = image_path

    pil_image = Image.fromarray(best_face_image)
    print(best_path)
    pil_image.show()

