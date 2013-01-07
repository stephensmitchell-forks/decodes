

# written using this tutorial: http://getpython3.com/diveintopython3/packaging.html
from distutils.core import setup
setup(
    name = 'decodes',
    packages = ['decodes','decodes.core', 'decodes.extensions', 'decodes.io'],
    version = '0.0.1',
    description = 'a geometry library for 3d designers',
    url = "http://decod.es",
    author='Kyle Steinfeld',
    author_email = "ksteinfe@gmail.com",
    classifiers = [
      "Programming Language :: Python"
      "Programming Language :: Python :: 2"
      "Topic :: Multimedia :: Graphics :: 3D Modeling"
    ],
)

