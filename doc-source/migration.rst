=====================================
Migration from :mod:`pyms.Display`
=====================================

:mod:`pymassspec_plot` replaces :mod:`pyms.Display`. The latter will evantually deprecated and removed.

.. csv-table:: Mapping of names from :mod:`pyms.Display` to :mod:`pymassspec_plot`.
	:header: Old,New

	:func:`pyms.Display.plot_ic`,:func:`pymassspec_plot.plot_ic`
	:func:`pyms.Display.plot_mass_spec`,:func:`pymassspec_plot.plot_mass_spec`
	:func:`pyms.Display.plot_peaks`,:func:`pymassspec_plot.plot_peaks`
	:func:`pyms.Display.plot_head2tail`,:func:`pymassspec_plot.plot_head2tail`
	:class:`pyms.Display.ClickEventHandler`,:class:`pymassspec_plot.ClickEventHandler`
	:func:`pyms.Display.invert_mass_spec`,:func:`pymassspec_plot.utils.invert_mass_spec`


:mod:`pyms.Display` also provided a ``Display`` class.
Its methods were mostly thin wrappers around the functions this library provides.

.. csv-table:: Mapping of methods on :class:`pyms.Display.Display` to functions in :mod:`pymassspec_plot`.
	:header: Old,New

	:meth:`pyms.Display.Display.plot_ic`,:func:`pymassspec_plot.plot_ic`
	:meth:`pyms.Display.Display.plot_tic`,:func:`pymassspec_plot.plot_ic`
	:meth:`pyms.Display.Display.plot_mass_spec`,:func:`pymassspec_plot.plot_mass_spec`
	:meth:`pyms.Display.Display.plot_peaks`,:func:`pymassspec_plot.plot_peaks`
	:meth:`pyms.Display.Display.do_plotting`,"No replacement [*]_"
	:meth:`pyms.Display.Display.get_5_largest`,"No replacement [*]_"
	:meth:`pyms.Display.Display.onclick`,"No replacement [*]_"
	:meth:`pyms.Display.Display.save_chart`,"Achievable through :meth:`matplotlib.figure.Figure.savefig`"
	:meth:`pyms.Display.Display.show_chart`,":meth:`matplotlib.figure.Figure.show` or :func:`matplotlib.pyplot.show`"

.. [*] :meth:`pyms.Display.Display.do_plotting` did the following:

	* Emit a warning if called without any plotting functions
	  (e.g. :meth:`pyms.Display.Display.plot_ic`) being called.
	* Set the ``plot_label`` as the axes title. Use :meth:`matplotlib.axes.Axes.set_title` instead.
	* Create a legend for the axes. Use :meth:`matplotlib.axes.Axes.legend` instead.
	* Ensure the figure is drawn on the canvas.
	  Use ``matplotlib.figure.Figure.canvas.draw()`` instead.
	* Configure a callback for the plot being clicked. Use :class:`~.ClickEventHandler` instead.

.. [*] :meth:`pyms.Display.Display.get_5_largest` was used internally as part of the left click callback. See :meth:`pymassspec_plot.ClickEventHandler.get_n_largest` for a similar implementation.

.. [*] :meth:`pyms.Display.Display.onclick` was configured internally as an event callback. The same result can be obtained using the :class:`~.ClickEventHandler` class.
