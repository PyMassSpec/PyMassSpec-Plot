# stdlib
import os
import sys
from typing import List

# 3rd party
import pytest
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_python_tools.paths import PathPlus
from matplotlib import pyplot as plt  # type: ignore[import-untyped]
from matplotlib.backend_bases import MouseEvent  # type: ignore[import-untyped]
from matplotlib.cbook import CallbackRegistry  # type: ignore[import-untyped]
from matplotlib.figure import Figure  # type: ignore[import-untyped]
from pyms.GCMS.Class import GCMS_data
from pyms.IntensityMatrix import IntensityMatrix
from pyms.IonChromatogram import IonChromatogram
from pyms.Peak import Peak
from pyms.Spectrum import MassSpectrum

# this package
from pymassspec_plot import ClickEventHandler, plot_head2tail, plot_ic, plot_mass_spec, plot_peaks
from tests.constants import test_dict, test_numbers, test_sequences, test_string

baseline_dir = str(PathPlus(__file__).parent / "baseline")
assert os.path.exists(baseline_dir)

if sys.version_info[:2] == (3, 7):
	image_hashes = str(PathPlus(__file__).parent / "image_hashes_37.json")
elif sys.version_info[:2] == (3, 8):
	image_hashes = str(PathPlus(__file__).parent / "image_hashes_38.json")
elif sys.version_info[:2] == (3, 9):
	image_hashes = str(PathPlus(__file__).parent / "image_hashes_39.json")
elif sys.version_info >= (3, 13):
	image_hashes = str(PathPlus(__file__).parent / "image_hashes_313.json")
else:
	image_hashes = str(PathPlus(__file__).parent / "image_hashes.json")

check_images = pytest.mark.mpl_image_compare(
		baseline_dir=baseline_dir,
		savefig_kwargs={"dpi": 600},
		hash_library=image_hashes,
		style="default",
		)


@check_images
def test_plot_ic(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	# Plotting IC with various Line2D options
	plot_ic(ax, im_i.get_ic_at_index(5))

	return fig


@check_images
def test_plot_ic_minutes(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	# Plotting IC with various Line2D options
	plot_ic(ax, im_i.get_ic_at_index(5), minutes=True)

	return fig


@check_images
def test_plot_ic_label(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_ic(ax, im_i.get_ic_at_index(5), label="IC @ Index 5")
	ax.legend()

	return fig


@check_images
def test_plot_ic_alpha(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_ic(ax, im_i.get_ic_at_index(5), alpha=0.5)

	return fig


@check_images
def test_plot_ic_linewidth(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_ic(ax, im_i.get_ic_at_index(5), linewidth=2)

	return fig


@check_images
def test_plot_ic_linestyle(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_ic(ax, im_i.get_ic_at_index(5), linestyle="--")

	return fig


@check_images
def test_plot_ic_multiple(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_ic(ax, im_i.get_ic_at_index(5), label="IC @ Index 5")
	plot_ic(ax, im_i.get_ic_at_index(10), label="IC @ Index 10")
	plot_ic(ax, im_i.get_ic_at_index(20), label="IC @ Index 20")
	plot_ic(ax, im_i.get_ic_at_index(40), label="IC @ Index 40")
	plot_ic(ax, im_i.get_ic_at_index(80), label="IC @ Index 80")
	plot_ic(ax, im_i.get_ic_at_index(160), label="IC @ Index 160")

	ax.legend()

	return fig


@check_images
def test_plot_ic_title(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_ic(ax, im_i.get_ic_at_index(5))
	ax.set_title("Test IC Plot")

	return fig


def test_plot_ic_errors(im_i: IntensityMatrix, data: GCMS_data, ms: MassSpectrum):
	fig, ax = plt.subplots()

	for obj in [*test_sequences, test_string, *test_numbers, test_dict, im_i, data, ms]:
		with pytest.raises(TypeError, match="'ic' must be an IonChromatogram"):
			plot_ic(ax, obj)  # type: ignore[arg-type]


# Plotting tic with various Line2D options
@check_images
def test_plot_tic(tic: IonChromatogram):
	fig, ax = plt.subplots()

	plot_ic(ax, tic)

	return fig


@check_images
def test_plot_tic_label(tic: IonChromatogram):
	fig, ax = plt.subplots()

	plot_ic(ax, tic, label="IC @ Index 5")

	ax.legend()

	return fig


@check_images
def test_plot_tic_alpha(tic: IonChromatogram):
	fig, ax = plt.subplots()

	plot_ic(ax, tic, alpha=0.5)

	return fig


@check_images
def test_plot_tic_linewidth(tic: IonChromatogram):
	fig, ax = plt.subplots()

	plot_ic(ax, tic, linewidth=2)

	return fig


@check_images
def test_plot_tic_linestyle(tic: IonChromatogram):
	fig, ax = plt.subplots()

	plot_ic(ax, tic, linestyle="--")

	return fig


def test_plot_tic_errors(im_i: IntensityMatrix, data: GCMS_data, ms: MassSpectrum):
	fig, ax = plt.subplots()

	for obj in [
			*test_sequences,
			*test_numbers,
			test_string,
			test_dict,
			im_i,
			data,
			ms,
			]:
		with pytest.raises(TypeError, match="'ic' must be an IonChromatogram"):
			plot_ic(ax, obj)  # type: ignore[arg-type]


@check_images
def test_plot_tic_title(tic: IonChromatogram):
	fig, ax = plt.subplots()

	plot_ic(ax, tic)

	ax.set_title("Test TIC Plot")

	return fig


# Plotting mass spec with various Line2D options
@check_images
def test_plot_mass_spec(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_mass_spec(ax, im_i.get_ms_at_index(50))

	return fig


@check_images
def test_plot_mass_spec_alpha(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_mass_spec(ax, im_i.get_ms_at_index(50), alpha=0.5)

	return fig


@check_images
def test_plot_mass_spec_width(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_mass_spec(ax, im_i.get_ms_at_index(50), width=1)

	return fig


@check_images
def test_plot_mass_spec_linestyle(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_mass_spec(ax, im_i.get_ms_at_index(50), linestyle="--")

	return fig


def test_plot_mass_spec_errors(im_i: IntensityMatrix, data: GCMS_data, tic: IonChromatogram):
	fig, ax = plt.subplots()

	for obj in [
			*test_sequences,
			test_string,
			*test_numbers,
			test_dict,
			im_i,
			im_i.get_ic_at_index(0),
			data,
			tic,
			]:
		with pytest.raises(TypeError, match="'mass_spec' must be a MassSpectrum"):
			plot_mass_spec(ax, obj)  # type: ignore[arg-type]


@check_images
def test_plot_mass_spec_title(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_mass_spec(ax, im_i.get_ms_at_index(50))

	ax.set_title(f"Mass spec for peak at time {im_i.get_time_at_index(50):5.2f}")

	return fig


# TODO: plot_peaks


@check_images
def test_plot_head2tail(im_i: IntensityMatrix):
	fig, ax = plt.subplots()

	plot_head2tail(ax, im_i.get_ms_at_index(50), im_i.get_ms_at_index(150))

	return fig


def test_plot_head2tail_errors(im_i: IntensityMatrix, data: GCMS_data):
	_, ax = plt.subplots()

	for obj in [*test_sequences, test_string, *test_numbers, test_dict, im_i, data]:
		with pytest.raises(TypeError, match="'top_mass_spec' must be a MassSpectrum"):
			plot_head2tail(ax, obj, im_i.get_ms_at_index(150))  # type: ignore[arg-type]

		with pytest.raises(TypeError, match="'bottom_mass_spec' must be a MassSpectrum"):
			plot_head2tail(ax, im_i.get_ms_at_index(50), obj)  # type: ignore[arg-type]

	for obj in [*test_sequences, test_string, *test_numbers, im_i.get_ms_at_index(250), im_i, data]:
		with pytest.raises(
				TypeError,
				match="'top_spec_kwargs' must be a mapping of keyword arguments for the top mass spectrum."
				):
			plot_head2tail(
					ax,
					im_i.get_ms_at_index(50),
					im_i.get_ms_at_index(150),
					top_spec_kwargs=obj,  # type: ignore[arg-type]
					)

		with pytest.raises(
				TypeError,
				match="'bottom_spec_kwargs' must be a mapping of keyword arguments for the bottom mass spectrum."
				):
			plot_head2tail(
					ax,
					im_i.get_ms_at_index(50),
					im_i.get_ms_at_index(150),
					bottom_spec_kwargs=obj,  # type: ignore[arg-type]
					)


def test_plot_peaks(im_i: IntensityMatrix, data: GCMS_data, ms: MassSpectrum):
	fig, ax = plt.subplots()

	for obj in [*test_sequences, test_string, *test_numbers, test_dict, im_i, data, ms]:
		with pytest.raises(TypeError, match="'peak_list' must be a list of Peak objects"):
			plot_peaks(ax, obj)  # type: ignore[arg-type]


@check_images
def test_plot_peaks_errors(peak_list: List[Peak]) -> Figure:
	fig, ax = plt.subplots()

	plot_peaks(ax, peak_list)

	return fig


@check_images
def test_plot_peaks_with_tic(peak_list: List[Peak], tic: IonChromatogram):
	fig, ax = plt.subplots()

	plot_ic(ax, tic)
	plot_peaks(ax, peak_list)

	return fig


def test_click_event_handler(
		peak_list: List[Peak],
		capsys,
		advanced_file_regression: AdvancedFileRegressionFixture,
		):
	fig, ax = plt.subplots()

	# Setup up the ClickEventHandler
	handler = ClickEventHandler(peak_list, fig, ax)

	assert handler.fig is fig
	assert handler.ax is ax
	assert handler.cid is not None

	callbacks: CallbackRegistry = fig.canvas.callbacks
	assert "button_press_event" in callbacks.callbacks

	event = MouseEvent("button_press_event", fig.canvas, peak_list[0].rt, 100, button=1)
	event.xdata = peak_list[0].rt  # FIXME

	callbacks.process("button_press_event", event)

	advanced_file_regression.check(capsys.readouterr().out)
