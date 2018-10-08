from keras.models import load_model

cascade_path = 'model/cv2/haarcascade_frontalface_alt2.xml'
model_path = 'model/keras/model/facenet_keras.h5'
facenet = load_model(model_path)