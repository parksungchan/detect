import subprocess
import init_value

command = 'python '
command += init_value.research_dir + '/' + 'object_detection/builders/model_builder_test.py '
subprocess.check_output(command, shell=True)




