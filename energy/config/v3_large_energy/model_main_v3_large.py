import subprocess
import init_value

command = 'python '
command += '/home/dev/detect/energy/config/v3_large_energy/model_main_v3_large.py'
command += ' ' + '--pipeline_config_path=' + '/home/dev/detect/energy/config/v3_large_energy/pipeline.config'
command += ' ' + '--model_dir=' + init_value.project_dir + '/energy/output/ckpt/v3_large_energy'
command += ' ' + '--num_train_steps=100000'
command += ' ' + '--sample_1_of_n_eval_examples=1'
command += ' ' + '--alsologtostderr'
subprocess.check_output(command, shell=True)


#python /home/dev/models/research/object_detection/model_main.py --pipeline_config_path=/home/dev/detect/pet_faces/config/v3_large_pets/pipeline.config --model_dir=/home/dev/detect/pet_faces/output/ckpt/v3_large_pet --sample_1_of_n_eval_examples=1 --alsologtostderr
