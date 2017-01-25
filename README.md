#02-DataVis-10ways

By Congyang Wang --- 2017/01/17

*Assignment 2: This is the second work of WPI CS573 Data Visualization, in A2, I used 10 tools to make the same scatter/bubble plot with size and color requirement, 1/3 of them have interactive function, 1/3 of them are deployed on the web with their own web server. 1/3 of them built with 0 code. This is a challenge for anyone, at the same time, it is a chance to familiar with different tools, to know the pros and cons.

**Table of Content**
* [1. D3.js](#d3.js)
* [2. R + ggplot2](#r+ggplot2)
* [3. Excel](#excel)
* [4. Tableau](#tableau)
* [5. Python+Plot.ly](#python+plot.ly)
* [6. ECharts](#echarts)
* [7. Matlab](#matlab)
* [8. Quadrigram](#quadrigram)
* [9. Python+Bokeh](#python+bokeh)
* [10. Visualizefree](#visualizefree)

#D3.js
- **Screenshots:**  
![](d3js/a2-congyang.jpg)
- **Note:**
I have to say d3 is real the state of the art visualization tool on the earth, there are a lot of smart programmers share the ideas and tutorials, its not easy, but there are a lot of ways to learn it, this is its advantage. As the key tool of the CS573, we should learn more and deep on this package.
To get this viz, I created the canvas like what I learned from assignment 1and the axes, then the advanced step, I loaded the .csv to fill the circles, at this step never forget to build a local server to tuning. then the color and legend. This work consumed my several hours to learn the sample code and tuning, I am so excited to learn this package, it shows me a beautiful word of information.

* http://bl.ocks.org/weiglemc/6185069
* http://chimera.labs.oreilly.com/books/1230000000345/ch04.html#_setting_up_a_web_server
* http://matthewgladney.com/blog/data-science/no-nonsense-guide-getting-started-scatter-plots-d3-js-d3-csv/

#R+ggplot2
- **Screenshots:**  
![](r-ggplot2/a2-congyang.jpg)
- **Note:** R is a language primarily focused on statistical computing.
As a student of data science major, most professor recommended the R and a package `ggplot2`  a popular and powerful library for charting in R.

To get this viz, used the ggplot2's `qplot()` layer, use five new colors to make it fancy not like a R work, but a fashion tool. I am familiar with R and these package, with this strong `ggplot2`, only 5 lines code can make it come true.

* http://www.cnblogs.com/muchen/p/5412278.html
* http://docs.ggplot2.org/0.9.3/qplot.html
* http://rpubs.com/coyawa/cs573-a2r

#Excel

- **Screenshots:**  
![](excel/a2-congyang.jpg)
- **Note:**
Everybody knows Excel, as a famous and all ages office software, it is great. For this task, excel can also do it well with a easy use and tune interface, but not everybody know it can be programed with `VBA`, after that training and practice, you can call you a master of Excel.
To get this vis, I ned to choose five times to make them as the 5 different series. after that, there is no difficult thought to go to the next step. excel has a magic, if you did once right you will never forget the steps how to do it. Nevertheless for is this viz, the bubble size can not tweak like Tableau.

* https://www.zhihu.com/question/21032715

#Tableau

- **Screenshots:**  
![](tableau/a2-congyang.jpg)
- **Note:**
Tableau is a dedicated tool to make a visualization, for starter they can use the drag & drop to make a beautiful figure, for expert they can programming to make more tuning on the data and figure. When you have a clean and small dataset stored in .csv or .xls and so on, the Tableau is a good tool to use for analysis. 
This is my first time to make a scatter plot with tableau, I only met one question is how to show the scatters on the canvas, I youtube that, and make it done. I give up two 'null' and one weight over 5000 all three records to get the right chart.

* https://public.tableau.com/views/573A2-Tableau/Sheet1?:embed=y&:display_count=yes
* https://onlinehelp.tableau.com/current/pro/desktop/en-us/buildexamples_scatter.html
* https://www.youtube.com/watch?v=72E8-FPHenc

#Python+Plot.ly

- **Screenshots:**  
![](python-plotly/a2-congyang.jpg)
- **Note:**
Plot.ly is a younger tool to make visualization with R, Python, and many other language, I met it on last semester one course's project, you can use it with `jupyter-notebook` or with its cloud easy-use online service.
To make this viz, I load the data first with pandas's `pd.read_csv` then make five categories `go.Scatter` to separated the circles to five colors. Plot.ly is easy and kindly to learn and use, it will help students to show simple or complicate graphic in many ways.

* https://plot.ly/~wangcongyang/16/mpg-vs-weight/
* https://plot.ly/python/bubble-charts/#new-to-plotly

#ECharts

- **Screenshots:**  
![](echarts/a2-congyang.jpg)
- **Note:**
ECharts is not a famous javascript package, it was created by a group of talents from the Chinese search engine company Baidu several years ago.
To make this viz, the first and important step is to make the .csv transfer to the array, and use the array in the script of ECharts. With the Chinese documents, I learned this tool with several hours, I know it can be tuned more perfect, I will learn this more deep in the future.

* http://tushuo.baidu.com/p.php?p=dta8pgkhf36qf40k8

#Matlab

- **Screenshots:**  
![](matlab/a2-congyang.jpg)
- **Note:**
Matlab, another big shot on analysis area, no need more words.
To me, this is not a easy use software to make the graphic which I want, to make this viz, after a long journey of learn the steps and sample code, first, I import the data, then use `for: loop` to build the scatter plot, then choose the color and transparence, then the tick, done. 

* https://www.mathworks.com/examples/matlab/mw/graphics-ex36949892-create-scatter-chart-with-transparency
#Quadrigram

- **Screenshots:**  
![](quadrigram/a2-congyang.jpg)
- **Note:**
Among these online visualize and analysis tool, Quadrigram si the best one with my experience. Quadrigram is an online visualization data tool that will help user to improve and make interactive presentations for every purpose.
To make this viz, all I need to do is to use the easy understanding model in the tool to tweak every detail part of a graphic, not only for a individual viz, it can also use for a dashboard or some other data report, at the end, it will generate a public link to show the report to more audience.

* http://www.quadrigram.com/hosting/%E5%B0%8F%E4%BB%8E%E4%BB%8E/a2/#p/Page1

#Python+Bokeh

- **Screenshots:**  
![](python-bokeh/a2-congyang.png)
- **Note:**
I love Bokeh. Bokeh is a Python interactive visualization library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of novel graphics in the style of D3.js.
To make this viz, with the help of `jupyter-notebook`, I just need to check the very easy-read documents and user guide to satisfy my demand, like other python package, read the .csv, use `colormap` model to divided the data into five different colors. After I finished the coding, the Bokeh will generate a html with a interactive page.

* http://bokeh.pydata.org/en/latest/docs/user_guide.html#userguide

#Visualizefree

- **Screenshots:**  
![](visualizefree/a2-congyang.jpg)
- **Note:**
Visualizefree is a java based online visualize tool, the target is to help the business to make the real time dashboard.
To make this viz, as other online tool, I need upload the .csv to generate the dataset inside the tool, then set the axes, choose the right column to make them as the X Axis and Y Axis, it's not difficult but with the non-perfect UX, it took me 2 hours to tune the right display.

#Technical and Design achievements:
1. Make them like the sample which the Professor showed us. It may not a very hard work to make a scatter / bubble plot with these powerful tools, but to make them looks the same is not a easy job, the fancy colors, canvas size, the axes and  tick, the font format and the legend. Even the legend is not a required one, but I also do my best to make 9/10 have legend, because it is a good way to show the viz clearly.
2. I am not coder in the last 28 years, this year is my second year with coding, thus, I love this challenge, its my technical achievement to make one plot with these totally different tools, I even found more ways inspired me to go further. 
* Links: http://www.creativebloq.com/design-tools/data-visualization-712402
* Links: https://source.opennews.org/en-US/articles/what-i-learned-recreating-one-chart-using-24-tools/


