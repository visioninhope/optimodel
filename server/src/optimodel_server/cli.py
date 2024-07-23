import uvicorn
from .index import app


import argparse


def main():
    parser = argparse.ArgumentParser(description="Run the Uvicorn server.")
    parser.add_argument(
        "--workers", type=int, default=1, help="Number of worker processes"
    )
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=8000, workers=args.workers)
