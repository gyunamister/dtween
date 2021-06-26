import setuptools

setuptools.setup(
    name='dtween',
    version="0.0.2",
    description="Digital Twin of an Organization realized with Action-Oriented Process Mining",
    author="Gyunam Park",
    author_email="gnpark@pads.rwth-aachen.de",
    url="https://github.com/gyunamister/dtween",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools==51.1.2',
        'tqdm==4.56.2',
        'dash==1.19.0',
        'dash-bootstrap-components==0.11.1',
        'dash-table==4.11.2',
        'dash-daq==0.5.0',
        'dash_auth==1.4.1',
        'celery==5.0.2',
        'plotly==4.14.1',
        'plotly-express==0.4.1',
        'dash-interactive-graphviz==0.2.1',
        'fsspec==0.8.5',
        'locket==0.2.0',
        'partd==1.1.0',
        'numpy==1.19.3',
        'scikit-learn==0.24.1',
        'scikit-learn-extra==0.1.0b2',
        'dask==2.30.0',
        'pandas==1.2.2',
        'cvxopt==1.2.5',
        'pm4py>=2.2.0',
        'seaborn==0.11.0',
        'scipy==1.6.1',
        'pygraphviz==1.6',
        'redis==3.5.3',
        'matplotlib==3.3.3',
        'ipython==7.19.0',
        'ocpa',
        'dotenv'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.8.8',
)
