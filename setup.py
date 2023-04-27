import setuptools
from os import path
import paper_summarizer

here = path.abspath(path.dirname(__file__))
AUTHORS = """
Evan Komp, Nels Schimek
"""

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

if __name__ == "__main__":
    setuptools.setup(
        name='paper_summarizer',
        version=paper_summarizer.__version__,
        author=AUTHORS,
        project_urls={
            'Source': 'https://github.com/BeckResearchLab/paper_sumarizer',
        },
        description=
        'LLM based linear summarizer for papers',
        long_description=long_description,
        include_package_data=False, #no data yet, True if we want to include data
        keywords=[
            'LLM', 'Agent-based modeling', 'Summarizer', 'Paper summarizer'
        ],
        license='MIT',
        packages=setuptools.find_packages(exclude="tests"),
        scripts = [], #if we want to include shell scripts we make in the install
        install_requires=[
            'numpy', 
            'pandas', 
        ],
        extras_require={
            'tests': [
                'pytest',
                'coverage',
                'flake8',
                'flake8-docstrings'
            ],
            'docs': [
                'sphinx',
                'sphinx_rtd_theme',

            ]
        },
        classifiers=[
            'Development Status :: 1 - Planning',
            'Environment :: Console',
            'Operating System :: OS Independant',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
        ],
        zip_safe=False,
    )
