import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipi",
    version='0.0.1',
    description="The pipi tool is to install PyPi packages using pip from any source: dir, PyPi projects, Github.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anki-code/pipi",
    project_urls={
        "Documentation": "https://github.com/anki-code/pipi/blob/master/README.md",
        "Code": "https://github.com/anki-code/pipi",
        "Issue tracker": "https://github.com/anki-code/pipi/issues",
    },
    python_requires='>=3.6',
    install_requires=[
        'xonsh',
    ],
    platforms='Unix-like',
    scripts=['pipi'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Xonsh",
    ],
    license="BSD",
    author="anki-code",
    author_email="author@example.com"
)
