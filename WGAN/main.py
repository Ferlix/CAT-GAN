# ---------------------------------------------------------
# Tensorflow WGAN Implementation
# Licensed under The MIT License [see LICENSE for details]
# Written by Cheng-Bin Jin
# Email: sbkim0407@gmail.com
# ---------------------------------------------------------
import os
import tensorflow as tf

from solver import Solver

FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_string('gpu_index', '0', 'gpu index, default: 0')
tf.flags.DEFINE_integer('batch_size', 64, 'batch size for one feed forwrad, default: 64')
tf.flags.DEFINE_string('dataset', 'experiment', 'dataset name for choice [celebA|mnist], default: celebA')
tf.flags.DEFINE_bool('is_train', True, 'training or inference mode, default: False')
tf.flags.DEFINE_float('learning_rate', 5e-5, 'initial learning rate, default: 0.00005')
tf.flags.DEFINE_integer('num_critic', 5, 'the number of iterations of the critic per generator iteration, default: 5')
tf.flags.DEFINE_float('clip_val', 0.01, 'clipping value for Lipschitz constrain of the WGAN')
tf.flags.DEFINE_integer('z_dim', 64, 'dimension of z vector, default: 100')
tf.flags.DEFINE_integer('iters', 15000, 'number of iterations, default: 100000')
tf.flags.DEFINE_integer('print_freq', 1500, 'print frequency for loss, default: 50')
tf.flags.DEFINE_integer('save_freq', 4999, 'save frequency for model, default: 10000')
tf.flags.DEFINE_integer('sample_freq', 1000, 'sample frequency for saving image, default: 200')
tf.flags.DEFINE_integer('sample_batch', 64, 'number of sampling images for check generator quality, default: 64')
tf.flags.DEFINE_string('load_model', None,
                       'folder of saved model that you wish to test, (e.g. 20180704-1736), default: None')


def main(_):
    os.environ['CUDA_VISIBLE_DEVICES'] = FLAGS.gpu_index

    path3 = "/data/s2936860/WGAN-RR-1"
    
    if not os.path.exists(path3):
        try:
            os.mkdir(path3)
        except:
            raise OSError("Can't create destination directory (%s)!" % (path3))  

    solver = Solver(FLAGS)
    if FLAGS.is_train:
        solver.train()
    else:
        solver.test()


if __name__ == '__main__':
    tf.app.run()
