# matplotlib.pyplot

* https://matplotlib.org/3.10.0/api/pyplot_summary.html

`matplotlib.pyplot` is a state-based interface to matplotlib. It provides an implicit, MATLAB-like, way of plotting. It also opens `figures` on your screen, and acts as the figure GUI manager.
matplotlib.pyplot 是 matplotlib 的基于状态的接口. 它提供了一种隐式的、类似 MATLAB 的绘图方式. 它还会在屏幕上打开图窗, 并充当图窗 GUI 管理器.

pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:
pyplot 主要用于交互式绘图和编程绘图生成的简单情况:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
```

The explicit object-oriented API is recommended for complex plots, though pyplot is still usually used to create the `figure` and often the `Axes` in the figure. See `pyplot.figure`, `pyplot.subplots`, and `pyplot.subplot_mosaic` to create figures, and `Axes API` for the plotting methods on an Axes:
对于复杂的绘图, 建议使用显式的面向对象的 API, 尽管 pyplot 通常仍用于创建图形, 并且通常用于创建图形中的 Axes. 请参阅 pyplot.figure、pyplot.subplots 和 pyplot.subplot_mosaic 来创建图形, 以及 Axes API 以了解 Axes 上的绘图方法:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

See [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces) for an explanation of the tradeoffs between the implicit and explicit interfaces.
有关隐式接口和显式接口之间权衡的说明, 请参阅 Matplotlib 应用程序接口 (API).

## Managing Figure and Axes
管理图窗和轴

* axes 	Add an Axes to the `current figure` and make it the `current Axes`.

* cla 	Clear the current Axes.

* clf 	Clear the current figure.

* close 	Close a `figure window`.

* delaxes 	Remove an Axes (defaulting to the current Axes) from its figure.

* fignum_exists 	Return whether the figure with the given id exists.
					返回具有给定 id 的图形是否存在.

* figure 	Create a new figure, or activate an existing figure.

* gca 	Get the current Axes.

* gcf 	Get the current figure.

* get_figlabels 	Return a list of existing figure labels.

* get_fignums 	Return a list of existing figure numbers.

* sca 	Set the current Axes to ax and the current Figure to the parent of ax.

* subplot 	Add an Axes to the current figure or retrieve an existing Axes.

* subplot2grid 	Create a subplot at a specific location inside a regular grid.

* subplot_mosaic 	Build a layout of Axes based on ASCII art or nested lists.

* subplots 	Create a figure and a set of subplots.

* twinx 	Make and return a second Axes that shares the x-axis.

* twiny 	Make and return a second Axes that shares the y-axis.

```
# Add an Axes to the current figure and make it the current Axes.
matplotlib.pyplot.axes() -> Axes, or a subclass of Axes

# Clear the current Axes.
matplotlib.pyplot.cla()

# Clear the current figure.
matplotlib.pyplot.clf()

# Close a figure window.
matplotlib.pyplot.close()

# Remove an Axes (defaulting to the current Axes) from its figure.
matplotlib.pyplot.delaxes()

# Return whether the figure with the given id exists.
matplotlib.pyplot.fignum_exists(num) -> bool

# Create a new figure, or activate an existing figure.
matplotlib.pyplot.figure() -> Figure

# Get the current Axes. If there is currently no Axes on this Figure, a new one is created using Figure.add_subplot.
matplotlib.pyplot.gca() -> Axes

# Get the current figure. If there is currently no figure on the pyplot figure stack, a new one is created using figure().
matplotlib.pyplot.gcf() -> Figure

# Return a list of existing figure labels.
matplotlib.pyplot.get_figlabels() -> [Figure]

# Return a list of existing figure numbers.
matplotlib.pyplot.get_fignums() -> [Figure]

# Set the current Axes to ax and the current Figure to the parent of ax.
matplotlib.pyplot.sca(ax)

# Add an Axes to the current figure or retrieve an existing Axes.
matplotlib.pyplot.subplot() -> Axes

# Create a subplot at a specific location inside a regular grid.
matplotlib.pyplot.subplot2grid(shape, loc, rowspan=1, colspan=1, fig=None, **kwargs) -> Axes

# Build a layout of Axes based on ASCII art or nested lists.
matplotlib.pyplot.subplot_mosaic() -> Figure, dict[label, Axes]

# Create a figure and a set of subplots.
matplotlib.pyplot.subplots() -> Figure, axAxes or array of Axes

# Make and return a second Axes that shares the x-axis. The new Axes will overlay ax (or the current Axes if ax is None), and its ticks will be on the right.
matplotlib.pyplot.twinx(ax=None)[] -> Axes

# Make and return a second Axes that shares the y-axis. The new Axes will overlay ax (or the current Axes if ax is None), and its ticks will be on the top.
matplotlib.pyplot.twiny(ax=None) -> Axes

```

## Adding data to the plot
向图中添加数据

### Basic

* plot 	Plot y versus x as lines and/or markers.
		将 y 与 x 绘制为线条和/或标记.

* errorbar 	Plot y versus x as lines and/or markers with attached errorbars.
			将 y 与 x 绘制为带有附加误差线的线条和/或标记.

* scatter 	A scatter plot of y vs.
			y 与 的散点图

* plot_date 	[Deprecated] Plot coercing the axis to treat floats as dates.
				[已弃用]绘制强制轴以将浮点数视为日期.

* step 	Make a step plot.
		制作阶梯图.

* loglog 	Make a plot with log scaling on both the x- and y-axis.
			在 x 轴和 y 轴上都使用对数缩放进行绘图.

* semilogx 	Make a plot with log scaling on the x-axis.
			在 x 轴上绘制对数缩放的绘图.

* semilogy 	Make a plot with log scaling on the y-axis.
			在 y 轴上绘制对数缩放的绘图.

* fill_between 	Fill the area between two horizontal curves.
				填充两条水平曲线之间的区域.

* fill_betweenx 	Fill the area between two vertical curves.
					填充两条垂直曲线之间的区域.

* bar 	Make a bar plot.
		制作条形图.

* barh 	Make a horizontal bar plot.
		制作水平条形图.

* bar_label 	Label a bar plot.
				标记条形图.

* stem 	Create a stem plot.
		创建字干图.

* eventplot 	Plot identical parallel lines at the given positions.
				在给定位置绘制相同的平行线.

* pie 	Plot a pie chart.
		绘制饼图.

* stackplot 	Draw a stacked area plot or a streamgraph.
				绘制堆积面积图或流图.

* broken_barh 	Plot a horizontal sequence of rectangles.
				绘制一个水平矩形序列.

* vlines 	Plot vertical lines at each x from ymin to ymax.
			在每个 x 处绘制从 ymin 到 ymax 的垂直线.

* hlines 	Plot horizontal lines at each y from xmin to xmax.
			在每个 y 处绘制从 xmin 到 xmax 的水平线.

* fill 	Plot filled polygons.
		绘制填充的多边形.

* polar 	Make a polar plot.
			绘制极坐标图.

### Spans

* axhline 	Add a horizontal line spanning the whole or fraction of the Axes.
			添加一条横跨整个或部分 Axes 的水平线.

* axhspan 	Add a horizontal span (rectangle) across the Axes.
			添加跨 Axes 的水平跨度(矩形).

* axvline 	Add a vertical line spanning the whole or fraction of the Axes.
			添加一条跨越整个或部分 Axes 的垂直线.

* axvspan 	Add a vertical span (rectangle) across the Axes.
			添加跨 Axes 的垂直跨度(矩形).

* axline 	Add an infinitely long straight line.
			添加一条无限长的直线.

### Spectral

* acorr 	Plot the autocorrelation of x.
			绘制 x 的自相关.

* angle_spectrum 	Plot the angle spectrum.
					绘制角度光谱.

* cohere 	Plot the coherence between x and y.
			绘制 x 和 y 之间的连贯性.

* csd 	Plot the cross-spectral density.
		绘制交叉光谱密度.

* magnitude_spectrum 	Plot the magnitude spectrum.
						绘制幅值谱.

* phase_spectrum 	Plot the phase spectrum.
					绘制相位谱.

* psd 	Plot the power spectral density.
		绘制功率谱密度.

* specgram 	Plot a spectrogram.
			绘制频谱图.

* xcorr 	Plot the cross correlation between x and y.
			绘制 x 和 y 之间的互相关.

### Statistics

* ecdf 	Compute and plot the empirical cumulative distribution function of x.
		计算并绘制 x 的经验累积分布函数.

* boxplot 	Draw a box and whisker plot.
			绘制箱须图.

* violinplot 	Make a violin plot.
				制作一个小提琴情节.

### Binned

* hexbin 	Make a 2D hexagonal binning plot of points x, y.
			制作点 x、y 的 2D 六边形分箱图.

* hist 	Compute and plot a histogram.
		计算并绘制直方图.

* hist2d 	Make a 2D histogram plot.
			制作 2D 直方图.

* stairs 	Draw a stepwise constant function as a line or a filled plot.
			将逐步常数函数绘制为线条或填充图.

### Contours

* clabel 	Label a contour plot.
			标记等值线图.

* contour 	Plot contour lines.
			绘制等值线.

* contourf 	Plot filled contours.
			绘制填充的等值线.

### 2D arrays

* imshow 	Display data as an image, i.e., on a 2D regular raster.
			将数据显示为图像, 即在 2D 规则光栅上.

* matshow 	Display a 2D array as a matrix in a new figure window.
			在新的图窗窗口中将 2D 数组显示为矩阵.

* pcolor 	Create a pseudocolor plot with a non-regular rectangular grid.
			创建具有非规则矩形网格的伪彩色图解.

* pcolormesh 	Create a pseudocolor plot with a non-regular rectangular grid.
				创建具有非规则矩形网格的伪彩色图解.

* spy 	Plot the sparsity pattern of a 2D array.
		绘制 2D 数组的稀疏模式.

* figimage 	Add a non-resampled image to the figure.
			将未重新取样的图像添加到图窗中.

### Unstructured triangles

* triplot 	Draw an unstructured triangular grid as lines and/or markers.
			绘制一个非结构化的三角形网格作为线条和/或标记.

* tripcolor 	Create a pseudocolor plot of an unstructured triangular grid.
				创建非结构化三角形网格的伪彩色图解.

* tricontour 	Draw contour lines on an unstructured triangular grid.
				在非结构化三角形网格上绘制等值线.

* tricontourf 	Draw contour regions on an unstructured triangular grid.
				在非结构化三角形网格上绘制等值线区域.

### Text and annotations

* annotate 	Annotate the point xy with text text.
			用文本文本注释点 xy.

* text 	Add text to the Axes.
		向 Axes 添加文本.

* figtext 	Add text to figure.
			向图窗添加文本.

* table 	Add a table to an Axes.
			将表添加到 Axes.

* arrow 	Add an arrow to the Axes.
			向 Axes 添加箭头.

* figlegend 	Place a legend on the figure.
				在图窗上放置图例.

* legend 	Place a legend on the Axes.
			在 Axes 上放置图例.

### Vector fields

* barbs 	Plot a 2D field of wind barbs.
			绘制风倒钩的 2D 区域.

* quiver 	Plot a 2D field of arrows.
			绘制 2D 箭头区域.

* quiverkey 	Add a key to a quiver plot.
				向 Quiver 图添加键.

* streamplot 	Draw streamlines of a vector flow.
				绘制矢量流的流线.

## Axis configuration

* autoscale 	Autoscale the axis view to the data (toggle).
				根据数据自动缩放轴视图(切换).

* axis 	Convenience method to get or set some axis properties.
		获取或设置某些轴属性的便捷方法.

* box 	Turn the Axes box on or off on the current Axes.
		打开或关闭当前 Axes 上的 Axes 框.

* grid 	Configure the grid lines.
		配置网格线.

* locator_params 	Control behavior of major tick locators.
					控制主要刻度定位符的行为.

* minorticks_off 	Remove minor ticks from the Axes.
					从 Axes 中删除次要刻度.

* minorticks_on 	Display minor ticks on the Axes.
					在 Axes 上显示小刻度.

* rgrids 	Get or set the radial gridlines on the current polar plot.
			获取或设置当前极坐标图上的径向网格线.

* thetagrids 	Get or set the theta gridlines on the current polar plot.
				获取或设置当前极坐标图上的 theta 网格线.

* tick_params 	Change the appearance of ticks, tick labels, and gridlines.
				更改刻度、刻度标签和网格线的外观.

* ticklabel_format 	Configure the ScalarFormatter used by default for linear Axes.
					配置默认用于线性轴的 ScalarFormatter.

* xlabel 	Set the label for the x-axis.
			设置 x 轴的标签.

* xlim 	Get or set the x limits of the current Axes.
		获取或设置当前 Axes 的 x 限制.

* xscale 	Set the xaxis' scale.
			设置 xaxis 的比例.

* xticks 	Get or set the current tick locations and labels of the x-axis.
			获取或设置 x 轴的当前刻度位置和标签.

* ylabel 	Set the label for the y-axis.
			设置 y 轴的标签.

* ylim 	Get or set the y-limits of the current Axes.
		获取或设置当前 Axes 的 y 限制.

* yscale 	Set the yaxis' scale.
			设置 yaxis 的比例.

* yticks 	Get or set the current tick locations and labels of the y-axis.
			获取或设置 y 轴的当前刻度位置和标签.

* suptitle 	Add a centered super title to the figure.
			为图窗添加居中的超级标题.

* title 	Set a title for the Axes.
			设置 Axes 的标题.

## Layout

* margins 	Set or retrieve margins around the data for autoscaling axis limits.
			设置或检索数据周围的边距, 以便自动缩放轴限制.

* subplots_adjust 	Adjust the subplot layout parameters.
					调整子图布局参数.

* subplot_tool 	Launch a subplot tool window for a figure.
				启动图窗的子图工具窗口.

* tight_layout 	Adjust the padding between and around subplots.
				调整子图之间和周围的填充.

## Colormapping

* clim 	Set the color limits of the current image.
		设置当前图像的颜色限制.

* colorbar 	Add a colorbar to a plot.
			向绘图中添加颜色条.

* gci 	Get the current colorable artist.
		获取当前可着色艺术家.

* sci 	Set the current image.
		设置当前图像.

* get_cmap 	Get a colormap instance, defaulting to rc values if name is None.
			获取颜色图实例, 如果 name 为 None, 则默认为 rc 值.

* set_cmap 	Set the default colormap, and applies it to the current image if any.
			设置默认颜色图, 并将其应用于当前图像(如果有).

* imread 	Read an image from a file into an array.
			将图像从文件中读取到数组中.

* imsave 	Colormap and save an array as an image file.
			颜色映射表并将数组另存为图像文件.

Colormaps are available via the colormap registry `matplotlib.colormaps`. For convenience this registry is available in `pyplot` as `matplotlib.pyplot.colormaps`.
颜色图可通过颜色图注册表 matplotlib.colormaps 获得. 为方便起见, 此注册表在 pyplot 中为 matplotlib.pyplot.colormaps.

Additionally, there are shortcut functions to set builtin colormaps; e.g. `plt.viridis()` is equivalent to `plt.set_cmap('viridis')`.
此外, 还有一些快捷键可以设置内置颜色图;例如, plt.viridis() 等同于 plt.set_cmap('viridis').

## Configuration

* rc 	Set the current rcParams. group is the grouping for the rc, e.g., for `lines.linewidth` the group is `lines`, for `axes.facecolor`, the group is `axes`, and so on. Group may also be a list or tuple of group names, e.g., (xtick, ytick). kwargs is a dictionary attribute name/value pairs, e.g.,::.
		设置当前的 rcParams. group 是 rc 的分组, 例如, 对于 lines.linewidth 的组是 lines, 对于 axes.facecolor, 组是 axes, 依此类推. Group 也可以是组名称的列表或 Tuples, 例如 (xtick, ytick). kwargs 是字典属性名称/值对, 例如::.

* rc_context 	Return a context manager for temporarily changing rcParams.
				返回临时更改 rcParams 的上下文管理器.

* rcdefaults 	Restore the rcParams from Matplotlib's internal default style.
				从 Matplotlib 的内部默认样式恢复 rcParams.

## Output

* draw 	Redraw the current figure.
		重绘当前图窗.

* draw_if_interactive 	Redraw the current figure if in interactive mode.
						如果处于交互模式, 请重新绘制当前图窗.

* ioff 	Disable interactive mode.
		禁用交互模式.

* ion 	Enable interactive mode.
		启用交互模式.

* install_repl_displayhook 	Connect to the display hook of the current shell.
							连接到当前 shell 的 display hook.

* isinteractive 	Return whether plots are updated after every plotting command.
					返回是否在每次绘图命令后更新绘图.

* pause 	Run the GUI event loop for interval seconds.
			运行 GUI 事件循环 interval seconds.

* savefig 	Save the current figure as an image or vector graphic to a file.
			将当前图窗作为图像或矢量图形保存到文件中.

* show 	Display all open figures.
		显示所有打开的图窗.

* switch_backend 	Set the pyplot backend.
					设置 pyplot 后端.

* uninstall_repl_displayhook 	Disconnect from the display hook of the current shell.
								断开与当前 shell 的 display hook 的连接.

## Other

* connect 	Bind function func to event s.
			将函数 func 绑定到事件.

* disconnect 	Disconnect the callback with id cid.
				断开 id 为 cid 的回调.

* findobj 	Find artist objects.
			查找 artist 对象.

* get 	Return the value of an Artist's property, or print all of them.
		返回 Artist 属性的值, 或打印所有 Artist.

* getp 	Return the value of an Artist's property, or print all of them.
		返回 Artist 属性的值, 或打印所有 Artist.

* get_current_fig_manager 	Return the figure manager of the current figure.
							返回当前图窗的图窗管理器.

* ginput 	Blocking call to interact with a figure.
			阻止调用与图形交互.

* new_figure_manager 	Create a new figure manager instance.
						创建新的图窗管理器实例.

* set_loglevel 	Configure Matplotlib's logging levels.
				配置 Matplotlib 的日志记录级别.

* setp 	Set one or more properties on an Artist, or list allowed values.
		在 Artist 上设置一个或多个属性, 或列出允许的值.

* waitforbuttonpress 	Blocking call to interact with the figure.
						阻止调用以与图形交互.

* xkcd 	Turn on xkcd sketch-style drawing mode.
		开 xkcd 草图样式的绘制模式.


