import subprocess
import init_value

command = 'python '
command += init_value.research_dir + '/' + 'object_detection/export_tflite_ssd_graph.py'
command += ' ' + '--pipeline_config_path=' + init_value.project_dir + '/pet_faces/config/v2_quantized_pets/pipeline.config'
command += ' ' + '--trained_checkpoint_prefix=' + init_value.project_dir + '/pet_faces/output/ckpt/v2_quantized_pet/model.ckpt-1372'
command += ' ' + '--output_directory=' + init_value.project_dir + '/pet_faces/output/pb/v2_quantized_pet'
command += ' ' + '--add_postprocessing_op=true'
subprocess.check_output(command, shell=True)




