import os
import torch

class CONFIG(object):
    def __init__(self):
        # params for train.py(or shared)
        self.learning_rate = 2e-5
        self.max_input_len = 256
        self.batch_size = 32
        self.epoch = 2 # use 2 for debugging, run with 100
        self.data_max_size = 100 # use 100 if debuging, run with 1e9

        self.pretrain_model_name = "roberta-base"
        # self.data_path = "/home/yusenzhang/input_classify_new/dataset/new_averaged_small_trainset.json"
        # self.model_path = "./checkpoints/07270039_params13.pkl"
        # self.model_path = "../input_classification/params2.pkl"
        # self.model_path = "/home/yusenzhang/input_classify/models/input_multi_classification/checkpoints/07301738_params10.pkl"
        self.model_path = "D:/TriageSQL_Data/checkpoints"
        # self.model_path = "./checkpoints/08130317_params7.pkl"
        self.use_gpu = False
        self.device = 0
        self.save = True
        self.load_model = False # remember to set this value when evaluating
        self.multi_GPU = False

        # params only for eval.py
        self.test_path = "D:/TriageSQL_Data/final_triage1.3_testset.json"
        self.train_path = "D:/TriageSQL_Data/final_triage1.3_trainset.json"
        self.dev_path = "D:/TriageSQL_Data/final_triage1.3_devset.json"
        # self.test_path = "/home/yusenzhang/input_classify/models/input_multi_classification/dataset/type12_testset.json"
        # self.test_path = "/home/yusenzhang/input_classify/models/input_multi_classification/dataset/written_100_testset.json"
        self.label_dict = {
            'answerable': 0,
            'small talk': 1,
            'ambiguous' : 2,
            'lack data' : 3,
            'unanswerable by sql' : 4
        }



