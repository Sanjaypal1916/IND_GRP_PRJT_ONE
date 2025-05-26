
from dataclasses import dataclass
from pathlib import Path

@dataclass
class dataIngestionConfig:
    root_dir: Path
    source_url : str
    local_data_dir: Path
    unzip_data_dir: Path