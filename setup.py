from setuptools import setup

setup(name     = "ahu",
  version      = "0.1.1",
  description  = "PostgreSQL foreign data wrapper for REST apis",
  author       = "Matthew Carter",
  author_email = "m@ahungry.com",
  packages     = ["ahu"],
  install_requires=["requests"]
)
