import os
from glob import glob
from setuptools import setup

package_name = 'duckietown'

setup(
    name=package_name,
    version='0.0.0',
#    packages=[package_name],
    packages=[
        'duckietown_utils',
        'duckietown_utils_tests',
        'duckietown',
    ],
    package_dir={'': 'include'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf/meshes/duckiebot/DB18'), glob('urdf/meshes/duckiebot/DB18/*.dae')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marcel',
    maintainer_email='stuettgen@fh-aachen.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
