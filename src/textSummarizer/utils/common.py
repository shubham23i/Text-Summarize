import os
from textSummarizer.logging import logger
from textSummarizer.exception import CustomException
from ensure import ensure_annotations
import yaml
from box import ConfigBox
from pathlib import Path
from typing import Any
import sys


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml,"r") as f:
            content=yaml.safe_load(f)
            logger.info("yaml file read successfully")
            return ConfigBox(content)
        
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def create_dir(dir_path:list,verbose=True):    
    for path in dir_path:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory created successfully at {dir_path}")


@ensure_annotations
def get_size(path:Path)->str:
    size_in_kb=os.path.getsize(path)/1024
    return ~f"{size_in_kb:.2f}"


