import tensorflow as tf
import sys

# check if the model path argument is provided
if len(sys.argv) != 2:
    sys.exit(1)

# get the model path from the command line argument
model_path = sys.argv[1]

model = tf.keras.models.load_model(model_path)

converter = tf.lite.TFLiteConverter.from_keras_model(model)

converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,  # enable TensorFlow Lite ops.
    tf.lite.OpsSet.SELECT_TF_OPS,  # enable TensorFlow ops.
]

# convert the model to TFLite format
tflite_model = converter.convert()

# generate the output file path based on the input model path
output_file = model_path.split("/")[-1].replace("h5", "tflite")

output_file = "./models/legacy/" + output_file

# save the converted model to a .tflite file
with open(output_file, "wb") as f:
    f.write(tflite_model)

print(f"Model conversion complete. TFLite model saved to {output_file}")
