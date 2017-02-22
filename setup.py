################################################################################
# Install Tensile
# - installs python scripts, c++ source files and a few configs
# - creates executables for running benchmarking
# - installs TensileConfig.cmake so one call find_package(Tensile)
################################################################################
from setuptools import setup

def get_requires(filename):
    requirements = []
    with open(filename) as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements

project_requires = get_requires("requirements.txt")

setup(
  name="Tensile",
  version="2.0",
  description="An auto-tuning tool for GEMMs and higher-dimensional tensor contractions on GPUs.",
  url="https://github.com/RadeonOpenCompute/Tensile",
  author="Advanced Micro Devices",
  license="MIT",
  install_requires=project_requires,
  packages=["Tensile"],
  package_data={ "Tensile": ["Tensile/Source/*", "Tensile/Configs/*"] },
  data_files=[ ("cmake", ["Tensile/Source/TensileConfig.cmake"]) ], 
  include_package_data=True,
  entry_points={"console_scripts": [
    # user runs a benchmark
    "tensile = Tensile.Tensile:main",
    # CMake calls this to create Tensile.lib
    "TensileCreateLibrary = Tensile.TensileCreateLibrary:TensileCreateLibrary",
    # automatic benchmarking for rocblas
    "tensile_rocblas_sgemm = Tensile.Tensile:TensileROCBLASSGEMM",
    "tensile_rocblas_dgemm = Tensile.Tensile:TensileROCBLASDGEMM",
    "tensile_rocblas_cgemm = Tensile.Tensile:TensileROCBLASCGEMM",
    "tensile_rocblas_zgemm = Tensile.Tensile:TensileROCBLASZGEMM",
    # automatically find fastest sgemm exhaustive search
    "tensile_sgemm = Tensile.Tensile:TensileSGEMM5760",
    ]}
  )