import subprocess
import init_value

# command = 'python '
# command += '/home/dev/tensorflow/tensorflow/lite/python/tflite_convert.py'
# command += ' ' + '--graph_def_file=' + init_value.project_dir + '/pet_faces/output/pb/v2_quantized_pets/tflite_graph.pb'
# command += ' ' + '--output_file=' + init_value.project_dir + '/pet_faces/output/tflite/v2_quantized_pet/detect_v2_pet.tflite'
# command += ' ' + '--output_format=TFLITE'
# command += ' ' + '--input_shapes=1,300,300,3'
# command += ' ' + '--input_arrays=normalized_input_image_tensor'
# command += ' ' + "--output_arrays='TFLite_Detection_PostProcess','TFLite_Detection_PostProcess:1','TFLite_Detection_PostProcess:2','TFLite_Detection_PostProcess:3'"
# command += ' ' + '--inference_type=QUANTIZED_UINT8'
# command += ' ' + '--mean_values=128'
# command += ' ' + '--std_dev_values=127'
# command += ' ' + '--change_concat_input_ranges=false'
# command += ' ' + '--allow_custom_ops'
#
# subprocess.check_output(command, shell=True)


# tflite_convert --graph_def_file=/home/dev/detect/pet_faces/output/pb/v2_quantized_pet/tflite_graph.pb --output_file=/home/dev/detect/pet_faces/output/tflite/v2_quantized_pet/detect_v2_pet.tflite --output_format=TFLITE --input_shapes=1,300,300,3 --input_arrays=normalized_input_image_tensor --output_arrays='TFLite_Detection_PostProcess','TFLite_Detection_PostProcess:1','TFLite_Detection_PostProcess:2','TFLite_Detection_PostProcess:3' --inference_type=QUANTIZED_UINT8 --mean_values=128 --std_dev_values=127 --change_concat_input_ranges=false --allow_custom_ops




