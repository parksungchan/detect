import subprocess
import init_value

command = 'python '
command += init_value.research_dir + '/' + 'object_detection/export_tflite_ssd_graph.py'
command += ' ' + '--pipeline_config_path=' + init_value.project_dir + '/pet_faces/config/v1_pets/ssd_mobilenet_v1_pets.config'
command += ' ' + '--trained_checkpoint_prefix=' + init_value.project_dir + '/pet_faces/output/ckpt/v1_pets/model.ckpt-2300'
command += ' ' + '--output_directory=' + init_value.project_dir + '/pet_faces/output/pb/v1_pets'
command += ' ' + '--add_postprocessing_op=true'
subprocess.check_output(command, shell=True)




