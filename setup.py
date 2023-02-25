from pathlib import Path
from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent

with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = list(map(lambda ln: ln.strip(), file.readlines()))

setup(
    name="mlops",
    version=0.01,
    description="I don't know yet.",
    author="Pranshu Bahadur",
    author_email="pranshubahadur@gmail.com",
    url="https://github.com/Pranshu-Bahadur/mlops-course.git",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=[required_packages]
)
