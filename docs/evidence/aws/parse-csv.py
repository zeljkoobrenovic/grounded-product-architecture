from pathlib import Path
import subprocess


ROOT_DIR = Path(__file__).resolve().parents[3]


if __name__ == "__main__":
    subprocess.run(
        ["python3", str(ROOT_DIR / "docs" / "evidence" / "generate-aws-docs.py")],
        check=True,
    )
