import tensorflow as tf
import init_value
gf = tf.GraphDef()
tflite_dir = init_value.research_dir + '/object_detection/ssd_models/models/ssd_mobilenet_v1_coco_2018_01_28/tflite'
m_file = open(tflite_dir + '/tflite_graph.pb','rb')
gf.ParseFromString(m_file.read())
for n in gf.node:
    print( n.name )