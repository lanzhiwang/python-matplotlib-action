Figure
	Axes
	GridSpec
	SubFigure
	Colorbar
	Legend
	Text
	suptitle() -> Text
	supxlabel() -> Text
	supylabel() -> Text
	Artist
	FigureImage
	SubFigure

---

plt.figure() -> Figure

	Figure.add_axes() -> Axes, or a subclass of Axes

	Figure.add_subplot() -> Axes

	Figure.subplots() -> Axes or array of Axes

	Figure.subplot_mosaic() -> dict[label, Axes]

	Figure.add_gridspec() -> GridSpec

	Figure.get_axes() -> List of Axes in the Figure.

	Figure.axes

	Figure.delaxes() -> Remove the Axes ax from the figure; update the current Axes.

	Figure.subfigures() -> Add a set of subfigures to this figure or subfigure.

	Figure.add_subfigure() -> SubFigure

	Figure.savefig() -> Save the current figure as an image or vector graphic to a file.

	Figure.colorbar() -> Colorbar

	Figure.legend() -> Legend

	Figure.text() -> Text

	Figure.suptitle() -> Text

	Figure.get_suptitle() -> Return the suptitle as string or an empty string if not set.

	Figure.supxlabel() -> Text

	Figure.get_supxlabel() -> Return the supxlabel as string or an empty string if not set.

	Figure.supylabel() -> Text

	Figure.get_supylabel() -> Return the supylabel as string or an empty string if not set.

	Figure.align_labels() -> Align对齐 the xlabels and ylabels.

	Figure.align_xlabels() -> Align the xlabels.

	Figure.align_ylabels() -> Align the ylabels.

	Figure.align_titles() -> Align the titles

	Figure.autofmt_xdate() -> 日期刻度标签经常重叠, 因此旋转它们并右对齐它们很有用.

	Figure.set_size_inches() -> 以英寸为单位设置图窗大小.

	Figure.get_size_inches() -> ndarray, The size (width, height) of the figure in inches.

	Figure.set_figheight()

	Figure.get_figheight()

	Figure.set_figwidth()

	Figure.get_figwidth()

	Figure.dpi -> 分辨率(以每英寸点数为单位).

	Figure.set_dpi()

	Figure.get_dpi()

	Figure.subplots_adjust() -> Adjust the subplot layout parameters.

	Figure.set_layout_engine() -> Set the layout engine for this figure.

	Figure.get_layout_engine()

	Figure.tight_layout() -> Adjust the padding between and around subplots.

	Figure.set_tight_layout()

	Figure.get_tight_layout()

	Figure.set_constrained_layout()

	Figure.get_constrained_layout()

	Figure.set_constrained_layout_pads()

	Figure.get_constrained_layout_pads()

	Figure.ginput() -> Blocking call to interact with a figure.

	Figure.add_axobserver()

	Figure.waitforbuttonpress()

	Figure.pick()

	Figure.set_frameon() -> 设置图窗的背景面片可见性, 即是否绘制图窗背景. 等效于 Figure.patch.set_visible().

	Figure.get_frameon()

	Figure.set_linewidth()

	Figure.get_linewidth()

	Figure.set_facecolor()

	Figure.get_facecolor()

	Figure.set_edgecolor()

	Figure.get_edgecolor()

	Figure.add_artist() -> Artist

	Figure.get_children() -> Get a list of artists contained in the figure.

	Figure.figimage() -> matplotlib.image.FigureImage

	Figure.clear()

	Figure.gca() -> Get the current Axes.

	Figure.sca(a) -> Set the current Axes to be a and return a.

	Figure.get_tightbbox() -> BboxBase 返回图形的(紧密)边界框(以英寸为单位).

	Figure.get_window_extent()

	Figure.show()

	Figure.set_canvas()

	Figure.draw()

	Figure.draw_without_rendering()

	Figure.draw_artist() -> Draw Artist a only.

	SubFigure -> class matplotlib.figure.SubFigure()
