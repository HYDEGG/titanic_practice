import argparse
import yaml

from src import preprocess, train, evaluate, predict

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def main(config_path: str):
    config = load_config(config_path)

    print("Step 1: Preprocessing")
    preprocess.preprocess_data(config)

    print("Step 2: Training")
    model_path = train.run(config)

    print("Step 3: Evaluation")
    evaluate.run(model_path, config)

    print("Step 4: Prediction")
    predict.run(model_path, config)

    print("All steps completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config", type=str, default="configs/train_config.yaml",
        help="Path to configuration file"
    )
    args = parser.parse_args()

    main(args.config)