# 3rd party
from coincidence import AdvancedDataRegressionFixture
from pyms.Spectrum import MassSpectrum

# this package
from pymassspec_plot import invert_mass_spec


def test_invert_mass_spec(advanced_data_regression: AdvancedDataRegressionFixture):
	# Diphenylamine
	mz_int_pairs = [
			(27, 138),
			(28, 210),
			(32, 59),
			(37, 70),
			(38, 273),
			(39, 895),
			(40, 141),
			(41, 82),
			(50, 710),
			(51, 2151),
			(52, 434),
			(53, 49),
			(57, 41),
			(59, 121),
			(61, 73),
			(62, 229),
			(63, 703),
			(64, 490),
			(65, 1106),
			(66, 932),
			(67, 68),
			(70, 159),
			(71, 266),
			(72, 297),
			(73, 44),
			(74, 263),
			(75, 233),
			(76, 330),
			(77, 1636),
			(78, 294),
			(84, 1732),
			(87, 70),
			(88, 86),
			(89, 311),
			(90, 155),
			(91, 219),
			(92, 160),
			(93, 107),
			(101, 65),
			(102, 111),
			(103, 99),
			(104, 188),
			(113, 107),
			(114, 120),
			(115, 686),
			(116, 150),
			(117, 91),
			(126, 46),
			(127, 137),
			(128, 201),
			(129, 73),
			(130, 69),
			(139, 447),
			(140, 364),
			(141, 584),
			(142, 279),
			(143, 182),
			(152, 37),
			(153, 60),
			(154, 286),
			(166, 718),
			(167, 3770),
			(168, 6825),
			(169, 9999),
			(170, 1210),
			(171, 85),
			]

	ms = MassSpectrum.from_mz_int_pairs(mz_int_pairs)

	inverted = invert_mass_spec(ms)
	assert inverted is not ms
	assert inverted != ms
	advanced_data_regression.check({"mass_list": inverted.mass_list, "mass_spec": inverted.mass_spec})

	inverted_inplace = invert_mass_spec(ms, inplace=True)
	assert inverted_inplace is ms
	assert inverted_inplace is not inverted
	assert inverted_inplace == inverted
	advanced_data_regression.check({
			"mass_list": inverted_inplace.mass_list,
			"mass_spec": inverted_inplace.mass_spec,
			})
