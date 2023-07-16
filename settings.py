from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'

SOURCES_LIST = [IMAGE, VIDEO]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_DIR = ROOT / 'default'
DEFAULT_IMAGE = DEFAULT_DIR / 'GX010143.jpg'
DEFAULT_DETECT_IMAGE = DEFAULT_DIR / '143_detected.jpg'

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'SLseg_V5.pt'
# DETECTION_MODEL = MODEL_DIR / 'jun26_urchin_seastar_cucumber.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'SLseg_V5.pt'
# SEGMENTATION_MODEL = DETECTION_MODEL
RESULTS_DIR = ROOT / 'Detected_Images'

