# stdlib
import re

# 3rd party
import nbformat
from domdf_python_tools.paths import PathPlus
from nbconvert import RSTExporter

rst_exporter = RSTExporter()

replacements = {
		# "pyms.GCMS.IO.JCAMP":
		# 		":mod:`pyms.GCMS.IO.JCAMP`",
		# "pyms.GCMS.IO.ANDI":
		# 		":mod:`pyms.GCMS.IO.ANDI`",
		# "pyms.GCMS.Class.GCMS_data":
		# 		":class:`pyms.GCMS.Class.GCMS_data`",
		# "GCMS_data":
		# 		":class:`~pyms.GCMS.Class.GCMS_data`",
		# "pyms.Spectrum.Scan":
		# 		":class:`pyms.Spectrum.Scan`",
		# "Scan":
		# 		":class:`~pyms.Spectrum.Scan`",
		# "GCMS_data.tic":
		# 		":attr:`GCMS_data.tic <pyms.GCMS.Class.GCMS_data.tic>`",
		# "IonChromatogram":
		# 		":class:`~pyms.IonChromatogram.IonChromatogram`",
		# "info()":
		# 		":py:meth:`info() <pyms.GCMS.Class.GCMS_data.info()>`",
		# "write()":
		# 		":py:meth:`write() <pyms.GCMS.Class.GCMS_data.write()>`",
		# "diff()":
		# 		":py:meth:`diff() <pyms.GCMS.Function.diff()>`",
		# "build_intensity_matrix()":
		# 		":meth:`build_intensity_matrix() <pyms.IntensityMatrix.build_intensity_matrix>`",
		# "build_intensity_matrix_i()":
		# 		":meth:`build_intensity_matrix_i() <pyms.IntensityMatrix.build_intensity_matrix_i>`",
		# "pyms.IntensityMatrix":
		# 		":mod:`pyms.IntensityMatrix <pyms.IntensityMatrix>`",
		# "IntensityMatrix":
		# 		":class:`~pyms.IntensityMatrix.IntensityMatrix`",
		# "im.min_mass":
		# 		":attr:`im.min_mass <pyms.IntensityMatrix.IntensityMatrix.min_mass>`",
		# "im.max_mass":
		# 		":attr:`im.max_mass <pyms.IntensityMatrix.IntensityMatrix.max_mass>`",
		# "im.get_index_of_mass()":
		# 		":meth:`im.get_index_of_mass() <pyms.IntensityMatrix.IntensityMatrix.get_index_of_mass>`",
		# "m/z":
		# 		":math:`m/z`",
		# "im.get_mass_at_index()":
		# 		":meth:`im.get_mass_at_index() <pyms.IntensityMatrix.IntensityMatrix.get_mass_at_index>`",
		# "build_intensity_matrix_i(data, lower, upper)":
		# 		":meth:`build_intensity_matrix_i(data, lower, upper) <pyms.IntensityMatrix.build_intensity_matrix_i>`",
		# "MassSpectrum":
		# 		":class:`~pyms.Spectrum.MassSpectrum`",
		# "mass_list":
		# 		":attr:`~pyms.Spectrum.MassSpectrum.mass_list`",
		# "intensity_list":
		# 		":attr:`~pyms.Spectrum.MassSpectrum.intensity_list`",
		# "get_ms_at_index(index)":
		# 		":meth:`get_ms_at_index(index) <pyms.IntensityMatrix.IntensityMatrix.get_ms_at_index()>`",
		# "is_tic()":
		# 		":meth:`is_tic() <pyms.IonChromatogram.IonChromatogram.is_tic>`",
		# "trim()":
		# 		":meth:`trim() <pyms.GCMS.Class.GCMS_data.trim>`",
		# "savitzky_golay()":
		# 		":meth:`savitzky_golay() <pyms.Noise.SavitzkyGolay.savitzky_golay>`",
		# "savitzky_golay_im()":
		# 		":meth:`savitzky_golay_im() <pyms.Noise.SavitzkyGolay.savitzky_golay_im>`",
		# "window_smooth()":
		# 		":meth:`window_smooth() <pyms.Noise.Window.window_smooth>`",
		# "window_smooth_im()":
		# 		":meth:`window_smooth_im() <pyms.Noise.Window.window_smooth_im>`",
		# "tophat()":
		# 		":meth:`tophat() <pyms.TopHat.tophat>`",
		# "tophat_im()":
		# 		":meth:`tophat_im() <pyms.TopHat.tophat_im>`",
		# "Peak":
		# 		":class:`~pyms.Peak.Class.Peak`",
		# "pyms.Peak.Class.Peak.rt":
		# 		":attr:`pyms.Peak.Class.Peak.rt`",
		# "pyms.Peak.Class.Peak.mass_spectrum":
		# 		":attr:`pyms.Peak.Class.Peak.mass_spectrum`",
		# "pyms.Peak.Class.Peak.UID":
		# 		":attr:`pyms.Peak.Class.Peak.UID`",
		# "crop_mass()":
		# 		":meth:`crop_mass() <pyms.Peak.Class.Peak.crop_mass>`",
		# "null_mass()":
		# 		":meth:`null_mass() <pyms.Peak.Class.Peak.null_mass>`",
		# "rel_threshold()":
		# 		":meth:`rel_threshold() <pyms.BillerBiemann.rel_threshold>`",
		# "num_ions_threshold()":
		# 		":meth:`num_ions_threshold() <pyms.BillerBiemann.num_ions_threshold>`",
		# "window_analyzer()":
		# 		":meth:`window_analyzer() <pyms.Noise.Analysis.window_analyzer>`",
		# "pyms.Peak.Class.Peak.area":
		# 		":attr:`~pyms.Peak.Class.Peak.area`",
		# "set_ion_areas()":
		# 		":meth:`set_ion_areas() <pyms.Peak.Class.Peak.set_ion_areas>`",
		# "peak_sum_area()":
		# 		":meth:`peak_sum_area() <pyms.Peak.Function.peak_sum_area>`",
		# "pyms.Peak.Function":
		# 		":mod:`pyms.Peak.Function`",
		# "Experiment":
		# 		":class:`~pyms.Experiment.Experiment`",
		# "Alignment":
		# 		":class:`~pyms.DPA.Alignment.Alignment` ",
		# "exprl2alignment()":
		# 		":meth:`exprl2alignment() <pyms.DPA.Function.exprl2alignment>`.",
		# "pyms.DPA.PairwiseAlignment.PairwiseAlignment":
		# 		":class:`pyms.DPA.PairwiseAlignment.PairwiseAlignment`",
		# "PairwiseAlignment":
		# 		":class:`~pyms.DPA.PairwiseAlignment.PairwiseAlignment`",
		# "align_with_tree()":
		# 		":meth:`align_with_tree() <pyms.DPA.Alignment.align_with_tree>`",
}

string_replacements = {
		"``JCAMP_reader``":
				":func:`~pyms.GCMS.IO.JCAMP.JCAMP_reader`",
		"``plot_ic()``":
				":func:`~pymassspec_plot.plot_ic`",
		"``plot_peaks()``":
				":func:`~pymassspec_plot.plot_peaks`",
		"``plot_mass_spec()``":
				":func:`~pymassspec_plot.plot_mass_spec`",
		"``IonChromatogram``":
				":class:`~pyms.IonChromatogram.IonChromatogram`",
		"``IntensityMatrix``":
				":class:`~pyms.IntensityMatrix.IntensityMatrix`",
		"``MassSpectrum``":
				":class:`~pyms.Spectrum.MassSpectrum`",
		"``build_intensity_matrix()``":
				":meth:`build_intensity_matrix() <pyms.IntensityMatrix.build_intensity_matrix>`",
		"https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.lines.Line2D.html":
				":class:`matplotlib.lines.Line2D`",
		"developed in\nmathematical morphology":
				"developed in mathematical morphology [1]_",
		"proteomics based mass spectrometry":
				"proteomics based mass spectrometry [2]_",
		"“Peak detection and representation” chapter":
				"`Peak detection and representation <https://pymassspec.readthedocs.io/en/master/40_peak_detection_and_representation.html>`_ chapter",
		'“':
				'"',
		'”':
				'"',
		"``ClickEventHandler``":
				":class:`pymassspec_plot.ClickEventHandler`",
		"``ClickEventHandler(peak_list=new_peak_list)``":
				":class:`pymassspec_plot.ClickEventHandler`",
		"``plt.show()``":
				":func:`~matplotlib.pyplot.show`",
		"Note: This may not":
				".. note:: This may not",
		"Example: ":
				'',
		}

notebooks = [
		"Displaying_TIC",
		"Displaying_Multiple_IC",
		"Displaying_Mass_Spec",
		"Displaying_Detected_Peaks",
		"Display_User_Interaction",
		]

demo_rst_dir = PathPlus("doc-source/demo_rst").resolve()
if not demo_rst_dir.is_dir():
	demo_rst_dir.mkdir()

images_dir = PathPlus("doc-source/examples/graphics").resolve()
if not images_dir.is_dir():
	images_dir.mkdir()

for notebook in notebooks:
	# Convert the notebook to RST format

	markdown_content = PathPlus(f"demo/jupyter/{notebook}.ipynb").read_text()

	markdown_content = markdown_content.replace("<!---->", '|')

	(body, resources) = rst_exporter.from_notebook_node(nbformat.reads(markdown_content, as_version=4))

	for original, replacement in string_replacements.items():
		body = body.replace(original, replacement)

	i = 1
	while True:
		old_body = body

		# replace nbconvert syntax with sphinx-toolbox "code-cell" syntax
		body = re.sub(r".. code:: ipython\d?", f".. code-cell:: python\n    :execution-count: {i}", body, 1)
		if body == old_body:
			break

		# body = body.replace(".. parsed-literal::", f".. nboutput::", 1)
		body = body.replace(".. parsed-literal::", f".. parsed-literal::", 1)
		i += 1

	outputs = resources["outputs"]
	if outputs:
		# Embedded images present
		# Put images in the images_dir

		# Write images to file
		for name, data in outputs.items():
			(images_dir / f"{notebook}_{name}").write_bytes(data)

		# Replace `.. image:: output` with `.. figure:: {notebook}_output`
		body = body.replace(".. image:: output", f".. figure:: graphics/{notebook}_output")

	# Write rst to file
	PathPlus(f"{demo_rst_dir/notebook}.rst").write_clean(body)
