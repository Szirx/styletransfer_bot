import tensorflow as tf
import tensorflow_hub as hub


# Загрузка изображений
def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img


def style_transfer(photo, style_photo, user_id):
    content_image = load_image(str(user_id) + '/image.jpg')
    style_image = load_image(str(user_id) + '/style.jpg')

    model_path = 'saved_model/'
    model = hub.load(model_path)

    stylized_image1 = model(tf.constant(content_image), tf.constant(style_image))[0]
    tf.keras.utils.save_img(str(user_id) + '/stylized_image.jpg', tf.squeeze(stylized_image1))
