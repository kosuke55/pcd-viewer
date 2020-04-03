from __future__ import print_function

from setuptools import find_packages
from setuptools import setup


version = "0.0.1"

setup_requires = []
install_requires = ['open3d>=0.9.0']

setup(
    name="pcd_viewer",
    version=version,
    description="Just launch open3d viewer with command",
    author="kosuke55",
    author_email="kosuke.tnp@gmail.com",
    url="https://github.com/kosuke55/pcd-viewer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts':
        ['pcd-viewer=pcd_viewer.apps.view:main']},
    setup_requires=setup_requires,
    install_requires=install_requires,
)
