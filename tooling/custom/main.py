from train_model import load_model
from predict import model_predict

MODEL_WEIGHTS = "../../data/weights.DATA"
MODEL = load_model(MODEL_WEIGHTS)

def probability_model(seq: list[str]) -> dict:
    return model_predict(seq, MODEL)


