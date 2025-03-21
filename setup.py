from setuptools import setup, find_packages

setup(
    name="nexolt",
    version="0.1.0",
    author="Nexolt Team",
    author_email="nexolt.project@gmail.com",
    description="A REST API for AI chat and other functionalities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zyppon/nexoltAPI", 
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-cors",
        "ollama"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
