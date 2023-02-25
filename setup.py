from pathlib import Path
from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# Define our package
setup(
    name="mlops",
    version=0.1,
    description="Classify machine learning projects.",
    author="Pranshu Bahadur",
    author_email="pranshubahadur@gmail.com",
    url="https://github.com/Pranshu-Bahadur/mlops-course.git",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
)
