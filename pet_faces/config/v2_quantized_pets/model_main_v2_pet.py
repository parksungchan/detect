import subprocess
import init_value

command = 'python '
command += init_value.research_dir + '/' + 'object_detection/model_main.py'
command += ' ' + '--pipeline_config_path=' + init_value.project_dir + '/pet_faces/config/v2_quantized_pets/pipeline.config'
command += ' ' + '--model_dir=' + init_value.project_dir + '/pet_faces/output/ckpt/v2_quantized_pet'
command += ' ' + '--num_train_steps=50000'
command += ' ' + '--sample_1_of_n_eval_examples=1'
command += ' ' + '--alsologtostderr'
subprocess.check_output(command, shell=True)


