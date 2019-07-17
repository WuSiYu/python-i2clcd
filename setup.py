import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="i2clcd",
    version="0.0.1",
    author="SiYu Wu",
    author_email="wu.siyu@hotmail.com",
    description="driver for LCD1602/2002/2004 with I2C adapter, for Raspberry Pi or other device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WuSiYu/python-i2clcd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
)
