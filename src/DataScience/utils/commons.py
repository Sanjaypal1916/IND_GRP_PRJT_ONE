import os
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            print(f"yaml file: {path_to_yaml} loaded")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            print(f"created directory at : {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f,indent=4)

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, "r") as f:
        content = json.load(f)
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any):
    joblib.dump(value=data, filename=path)
    print(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path):
    data = joblib.load(path)
    print(f"binary file loaded from: {path}")
    return data

    
