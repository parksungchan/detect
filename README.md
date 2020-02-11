# tensorflow import 
git clone https://github.com/tensorflow/models.git


# model & config down 
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md 


# label map
research/object_detection/data/pet_label_map.pbtxt


# From tensorflow/models/research/
python setup.py install


wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
unzip protobuf.zip
./bin/protoc object_detection/protos/*.proto --python_out=.


vi ~/.bashrc
export PYTHONPATH=$PYTHONPATH=/home/dev/models/research:/home/dev/models/research/slim
source ~/.bashrc


Pycharm Project Interpreter Add 
File -> Settings -> Project:models -> Project Interpreter -> setting icon click
->show all -> Right last icon click -> + -> /home/dev/models/research/slim


pip install pycocotools


test 
python object_detection/builders/model_builder_test.py


dataset down
wget http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
wget http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz
tar -xvf images.tar.gz
tar -xvf annotations.tar.gz
python object_detection/dataset_tools/create_pet_tf_record.py --label_map_path=object_detection/data/pet_label_map.pbtxt --data_dir=object_detection/ssd_models/data/pet_faces --output_dir=object_detection/ssd_models/data/pet_faces/record


config 수정
fine_tune_checkpoint: "/home/dev/models/research/object_detection/ssd_model/ssd_mobilenet/ssd_mobilenet_v1_coco_2018_01_28/model.ckpt"
train_input_reader: {
  tf_record_input_reader {
    input_path: "/home/dev/models/research/object_detection/ssd_models/data/pet_faces/pet_faces_train.record-?????-of-00010"
  }
  label_map_path: "/home/theresa/project/models/research/object_detection/ssd_models/data/pet_faces/pet_label_map.pbtxt"
}

eval_input_reader: {
tf_record_input_reader {
    input_path: "/home/theresa/project/models/research/object_detection/ssd_models/data/pet_faces/record/pet_faces_val.record-?????-of-00010"
  }
  label_map_path: "/home/theresa/project/models/research/object_detection/ssd_models/data/pet_faces/pet_label_map.pbtxt"
  shuffle: false
  num_readers: 1
}


pycharm
project_dir = '/home/dev/models'
model_dir = project_dir + '/research/object_detection/ssd_model/ssd_mobilenet/ssd_mobilenet_v1_coco_2018_01_28'
FLAGS.model_dir = model_dir + '/output_model'
FLAGS.pipeline_config_path = model_dir + '/ssd_mobilenet_v1_pets.config'
FLAGS.num_train_steps = 50000

terminal
# From the project/tf-models/research/ directory
export PROJECT_DIR=/home/dev
export TF_RESEARCH_MODEL_DIR=$PROJECT_DIR/models/research
export MODEL_DIR=$PROJECT_DIR/models/research/object_detection/ssd_models/models/ssd_mobilenet_v1_coco_2018_01_28/output
export PIPELINE_CONFIG_PATH=$MODEL_DIR/ssd_mobilenet_v1_pets.config
export NUM_TRAIN_STEPS=50000
export SAMPLE_1_OF_N_EVAL_EXAMPLES=1

python object_detection/model_main.py --pipeline_config_path=${PIPELINE_CONFIG_PATH} --model_dir=${MODEL_DIR} --num_train_steps=${NUM_TRAIN_STEPS} --sample_1_of_n_eval_examples=$SAMPLE_1_OF_N_EVAL_EXAMPLES --alsologtostderr
===================================================================================
graph.pb, graph.pbtxt 만들기
https://medium.com/@teyou21/convert-a-tensorflow-frozen-graph-to-a-tflite-file-part-3-1ccdb3874c4a
===================================================================================




