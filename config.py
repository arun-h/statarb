from pathlib import Path

# Auto-detect project root
BASE_DIR = Path(__file__).parent

# Define directories
RAW_DATA_DIR = BASE_DIR / 'data' / 'raw'
UNIVERSE_DATA_DIR = BASE_DIR / 'data' / 'universe'

# Define file paths
LIQUIDITY_METRICS_CSV = RAW_DATA_DIR / 'liquidity_metrics.csv'
FILTERED_UNIVERSE_CSV = UNIVERSE_DATA_DIR / 'filtered_universe.csv'

# Create directories automatically
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
UNIVERSE_DATA_DIR.mkdir(parents=True, exist_ok=True)
