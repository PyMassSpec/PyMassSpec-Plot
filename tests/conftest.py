# stdlib
from copy import deepcopy
from typing import Callable, List, Type, TypeVar

# 3rd party
import numpy
import pytest
from domdf_python_tools.paths import PathPlus
from pyms.BillerBiemann import BillerBiemann  # type: ignore[import]
from pyms.GCMS.Class import GCMS_data  # type: ignore[import]
from pyms.GCMS.IO.JCAMP import JCAMP_reader  # type: ignore[import]
from pyms.IntensityMatrix import IntensityMatrix, build_intensity_matrix_i  # type: ignore[import]
from pyms.IonChromatogram import IonChromatogram  # type: ignore[import]
from pyms.Noise.SavitzkyGolay import savitzky_golay  # type: ignore[import]
from pyms.Peak import Peak  # type: ignore[import]
from pyms.Spectrum import MassSpectrum  # type: ignore[import]
from pyms.TopHat import tophat  # type: ignore[import]
from pytest_regressions.data_regression import RegressionYamlDumper

pytest_plugins = ("coincidence", )


@pytest.fixture(scope="session")
def pyms_datadir() -> PathPlus:
	return PathPlus(__file__).parent / "data"


@pytest.fixture(scope="session")
def data(pyms_datadir: PathPlus) -> GCMS_data:
	return JCAMP_reader(pyms_datadir / "ELEY_1_SUBTRACT.JDX")


@pytest.fixture(scope="session")
def tic(data: GCMS_data) -> IonChromatogram:
	# get the TIC
	return deepcopy(data.tic)


@pytest.fixture(scope="session")
def im_i(data: GCMS_data) -> IntensityMatrix:
	# build an intensity matrix object from the data
	return build_intensity_matrix_i(data)


@pytest.fixture()
def ms(im_i: IntensityMatrix) -> MassSpectrum:
	return deepcopy(im_i.get_ms_at_index(0))


@pytest.fixture(scope="session")
def _peak_list(im_i: IntensityMatrix) -> List[Peak]:
	im_i = deepcopy(im_i)

	# Intensity matrix size (scans, masses)
	n_scan, n_mz = im_i.size

	# noise filter and baseline correct
	for ii in range(n_mz):
		ic = im_i.get_ic_at_index(ii)
		ic_smooth = savitzky_golay(ic)
		ic_bc = tophat(ic_smooth, struct="1.5m")
		im_i.set_ic_at_index(ii, ic_bc)

	# Use Biller and Biemann technique to find apexing ions at a scan
	# default is maxima over three scans and not to combine with any neighbouring
	# scan.
	peak_list = BillerBiemann(im_i, points=9, scans=2)
	return peak_list


@pytest.fixture()
def peak_list(_peak_list: List[Peak]) -> List[Peak]:
	return deepcopy(_peak_list)


_C = TypeVar("_C", bound=Callable)


def _representer_for(*data_type: Type) -> Callable[[_C], _C]:

	def deco(representer_fn: _C) -> _C:
		for dtype in data_type:
			RegressionYamlDumper.add_custom_yaml_representer(dtype, representer_fn)

		return representer_fn

	return deco


@_representer_for(numpy.float64)
def _represent_float_like(dumper: RegressionYamlDumper, data):  # noqa: MAN001,MAN002
	return dumper.represent_float(float(data))
