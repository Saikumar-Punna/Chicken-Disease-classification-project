import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-classification-project"
AUTHOR_USER_NAME = "Saikumar Punna"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "sk8627928@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for cnn app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Fix typo in this line
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
