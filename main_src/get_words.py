import hydra
import omegaconf
from openhands.apis.inference import InferenceModel

import json
from datetime import datetime
import os


# @hydra.main(config_path="/", config_name="stgcnconfig")
cfg = omegaconf.OmegaConf.load(r"C:\Users\JeongSeongYun\Desktop\OpenHands\OHTest\stgcnconfig.yaml")
def get_words(cfg=cfg):
    model = InferenceModel(cfg=cfg)
    print("🤖Model Calling Done!🤖")
    model.init_from_checkpoint_if_available()
    if cfg.data.test_pipeline.dataset.inference_mode:
        print("🚀🚀Starting Inference...🚀🚀")
        labels = model.test_inference()

        now =  datetime.now()
        log_time = now.strftime("%y%m%d_%H%M")  # Format as "yymmdd_HHMM"

        result_log_file_name = f"{log_time}.json"

        # Save the labels to a file
        with open(fr'C:\Users\JeongSeongYun\Desktop\OpenHands\OHTest\word_outputs\{result_log_file_name}', 'w', encoding='utf-8') as f:
            json.dump(labels, f, ensure_ascii=False, indent=4)
            

if __name__ == "__main__":
    from glob import glob
    
    print("🚀Start🚀")
    get_words()

    file_lst = glob(r'C:\Users\JeongSeongYun\Desktop\OpenHands\OHTest\word_outputs\*.json')
    target_label = file_lst[-1]

    # Load the labels from a file
    with open(f'{target_label}', 'r') as f:
        labels = json.load(f)
    
    print("Predictions...")
    print(labels)