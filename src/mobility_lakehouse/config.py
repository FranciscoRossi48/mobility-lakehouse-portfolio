from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
BRONZE_DIR = DATA_DIR / "bronze"
WAREHOUSE_PATH = DATA_DIR / "warehouse.duckdb"
SQL_DIR = PROJECT_ROOT / "sql"

