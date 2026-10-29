from setuptools import find_packages, setup

package_name = 'turtle_duvar_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='afazilk',
    maintainer_email='f241229057@ktun.edu.tr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kacan_kaplumbaga = turtle_duvar_py.kacan_kaplumbaga:main'
        ],
    },
)
