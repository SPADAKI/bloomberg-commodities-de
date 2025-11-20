# flow.py — Prefect 2 flow (2025 version, zero config pain)
from prefect import flow, task, get_run_logger
import subprocess
from datetime import datetime

@task
def run_pipeline():
    logger = get_run_logger()
    logger.info("Starting Bloomberg commodities pipeline...")
    result = subprocess.run(["python", "pipeline.py"], capture_output=True, text=True)
    if result.returncode == 0:
        logger.info("Pipeline succeeded!")
        print(result.stdout)
    else:
        logger.error("Pipeline failed!")
        raise RuntimeError(result.stderr)

@flow(name="Bloomberg Commodities Daily ETL")
def commodities_flow():
    run_pipeline()

if __name__ == "__main__":
    commodities_flow()   # Run once now
    # → For scheduling later: prefect deploy + agent (we’ll do in Loom)