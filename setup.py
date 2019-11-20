import setuptools

with open("README.md", "r") as fh:
        long_description = fh.read()

test_require = ["pytest", "pytest-cov"]
extras = {
    'test': test_require
}

setuptools.setup(
    name="krbticket",
    version="0.0.1.3",
    author="Kazuhiro Suzuki",
    author_email="ksauzzmsg@gmail.com",
    description="Kerberos Ticket Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ksauzz/krbticket",
    packages=setuptools.find_packages(),
    tests_require=test_require,
    extras_require=extras,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
)

