import os


class Config:
    DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/SST2')
    PRE_TRAINED_MODEL_DIR = "pre_trained_model"
    PRE_TRAINED_MODEL_CACHE_DIR = "Currently not used"
    PRE_TRAINED_MODEL_BERT_BASE_UNCASED = os.path.join(PRE_TRAINED_MODEL_DIR, "bert-base-uncased")
    MODEL_OUTPUT_DIR = "experiments"
    MODEL_NAME = "SST2"
    TRAINED_MODEL_FOR_PREDICTION = "SST2_1553095240"
    MAX_SEQ_LENGTH = 100
    DO_LOWER_CASE = True
    TRAIN_BATCH_SIZE = 64
    EVAL_BATCH_SIZE = 64
    LEARNING_RATE = 5e-5
    NUM_EPOCHS = 3.0
    WARMUP_PROPORTION = 0.1
    WEIGHT_DECAY = 0.1
    SEED = 42
    LOSS_SCALE = 128
