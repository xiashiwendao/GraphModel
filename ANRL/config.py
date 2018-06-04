# Configure parameters

class Config(object):
    def __init__(self):
        ## hyperparameter
        self.struct = [None, 1000, 500, None]
        self.reg = 1
        self.alpha = 1
        
        ## parameters for training
        self.batch_size = 512
        self.num_sampled = 20
        self.max_iters = 20000
        self.sg_learning_rate = 1e-6
        self.ae_learning_rate = 1e-6