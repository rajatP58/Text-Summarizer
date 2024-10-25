<<<<<<< HEAD
import setuptools

with open("README.md", "r", encoding="utf-8") as f:  
    long_description = f.read()

_version_ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "rajatP58"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "22mc10ra565@mits.gwl.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,  # Changed `Long_description` to `long_description`
    long_description_content_type="text/markdown",  # Changed `Long_description_content` to `long_description_content_type`
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
=======
import setuptools

with open("README.md", "r", encoding="utf-8") as f:  
    long_description = f.read()

_version_ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "rajatP58"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "22mc10ra565@mits.gwl.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,  # Changed `Long_description` to `long_description`
    long_description_content_type="text/markdown",  # Changed `Long_description_content` to `long_description_content_type`
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
>>>>>>> a89bf240c359c07c034f19ff969ba9fac431bd33
