import face_recognition
from PIL import Image, ImageDraw

known_faces = []
known_face_names = []


def add_to_Dataset():
    print("Enter image name")
    global known_faces
    global known_face_names
    img_location = input()
    img = face_recognition.load_image_file(img_location)
    print("Enter names of people from left to right")
    for i in (face_recognition.face_encodings(img)):
        known_faces = known_faces + [i]
        s = input()
        known_face_names = known_face_names + [s]

    print("Thank you!")


def recognize_faces():
    print("Enter image")
    global known_faces
    global known_face_names
    img_location = input()
    img = face_recognition.load_image_file(img_location)
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)

    pilimg = Image.fromarray(img)
    draw = ImageDraw.Draw(pilimg)
    matches = ""
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    # Remove the drawing library from memory as per the Pillow docs
    del draw

    # Display the resulting image
    pilimg.show()


add_to_Dataset()
recognize_faces()







