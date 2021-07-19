import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text-formatter",
    version="0.0.2",
    author="Ruben Lipperts",
    author_email="",
    description="Simple text output formatter that helps with printing pretty stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlipperts/formatter",
    packages=['text_formatter'],
    install_requires=[
        'pprintpp',
        'colored',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: General",
    ],
    python_requires='~=3.9',
)
