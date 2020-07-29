import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy_yolo", # Replace with your own username
    version="0.0.2",
    author="Arjun Pandey",
    author_email="apandey@jpischool.com",
    description="Library to easily test YOLOv3 models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pandeyarjun242",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = ["opencv-python"],
)