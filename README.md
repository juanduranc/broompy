### Python Library
### Juan Duran, Business Analyst & Industrial Engineer
# broompy
**broompy** is a Python library designed to help 
data scientists observe a summary of their 
DataFrame and facilitate data cleaning. It reveals 
features that require cleaning or inspection. 
This library also displays charts to view the normal 
approximation of variable distributions and generates 
scatter plot to visualize patterns.

Main Features
-------------
  - Display count of null and available data.
  - Display mean, median and 1.5 IQR outliers count.
  - Identify data types of each variable.
  - Identify count of unique values per variable.
  - Identify the normal approximation using pvalue.
  - Show a dataset sample to understand data content.
  - Visualize trends with histograms and scatter plots.
  
Installation
-------------
- [x] pip install broompy
- [x] import broompy<br>
- [x] help(broompy.core)<br>

### Installation requirements:
```diff
+ pandas
+ seaborn
+ numpy
+ pylab
+ scipy
+ statistic
```

<!DOCTYPE html>
<html>
<body>
  
Example of library usage and interpretation:
-------------

**1. The following table is a sample of an output form the function:** broompy.core.table<br>
  This example is based on a dataset not provided.<br><br>

**Executing:**<br>
broompy.core.table(dataframe, n_rows, n_round)<br>

<table>
     <tr>
      <th>VARIABLES</th>
      <th>NULLS</th>
      <th>COUNT</th>
      <th>TYPES</th>
      <th>MEAN</th>
      <th>MEDIAN</th>
      <th>UNIQUES</th>
      <th>SAMPLE_________________________________</th>
      <th>Outliers</th>
      <th>pval(Norm)</th>
    </tr>
    <tr height="20">
      <td>AVG_CLICKS_PER_VISIT</td>
      <td>0</td>
      <td>1946</td>
      <td>int64</td>
      <td>13.5</td>
      <td>13.0</td>
      <td>15</td>
      <td>[11, 13, 12, 13, 13, 17, 10, 13, 12, 12]</td>
      <td>[6,0]</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>MEDIAN_MEAL_RATING</td>
      <td>47</td>
      <td>1899</td>
      <td>int64</td>
      <td>2.8</td>
      <td>3.0</td>
      <td>5</td>
      <td>[3, 3, 3, 3, 3, 2, 4, 3, 3, 3]</td>
      <td>[0,13]</td>
      <td>3e-06</td>
    </tr>
    <tr>
      <td>REVENUE</td>
      <td>0</td>
      <td>1946</td>
      <td>float64</td>
      <td>2107.3</td>
      <td>1740.0</td>
      <td>859</td>
      <td>[1880, 1495, 2572.5, 1647, 1923, 1250]</td>
      <td>[0,82]</td>
      <td>1e-21</td>
    </tr>
    <tr>
      <td>TOTAL_PHOTOS_VIEWED</td>
      <td>0</td>
      <td>1946</td>
      <td>int64</td>
      <td>106.4</td>
      <td>0.0</td>
      <td>371</td>
      <td>[0, 90, 0, 0, 253, 0, 705, 0, 0, 0]</td>
      <td>[0,120]</td>
      <td>5e-90</td>
    </tr>
      <td>CROSS_SELL_SUCCESS</td>
      <td>0</td>
      <td>1946</td>
      <td>int64</td>
      <td>0.7</td>
      <td>1.0</td>
      <td>2</td>
      <td>[1, 1, 1, 0, 1, 1, 0, 1, 1, 1]</td>
      <td></td>
      <td>1e-159</td>
</table><br>

**Examples of findings:**<br>
<ul>
  <li>AVG_CLICKS_PER_VISIT approximates a normal distribution and has 6 lower outliers.</li>
  <li>MEDIAN_MEAL_RATING has 47 nulls and requires imputation.</li>
  <li>REVENUE is the only float variable. The rest are integer.</li>
  <li>TOTAL_PHOTOS_VIEWED has a median of 0 and 120 upper outliers. This means most people do not view photos.</li>
  <li>CROSS_SELL_SUCCESS has 2 unique values. From the column named sample you can see only ones and zeros. This is a binary or boolean column.</li>
</ul>
<br>

**2. usage and interpretation of the function:** broompy.core.normality<br>
  This example is based on a dataset not provided.<br><br>

**Executing:**<br>
broompy.core.normality(dataframe, list_var, "y", 10, 30, 10)<br><br>
<img src="https://raw.githubusercontent.com/juanduranc/imgs/master/normality.png" />
<br>

**Histograms' interpretation:**<br>
<ul>
  <li>MEDIAN_MEAL_RATING ranges between 1 and 5, it has integer values and it mimics a normal distribution. The table in example #1 reveals there are only 5 unique values.</li>
  <li>AVG_CLICKS_PER_VISIT is the closest variable to a normal distribution with a p value of 0.03.</li>
  <li>REVENUE is right skewed with 82 upper outliers. The outlier’s quantity can be seen in the table of example #1.</li>
  <li>TOTAL_PHOTOS_VIEWED has too many zero values. It is also right skewed and far from being a normal distribution. Example #1 shows a median of 0 for total photos viewed.</li>
</ul>
<br>

**3. Scatterplots usage:** broompy.core.scatter<br>
  This example is based on a dataset not provided.<br><br>

**Executing:**<br>
broompy.core.scatter(df, explanatory_var, response_var, print_img, size_x, size_y, font_size, green_blue='g')<br><br>

<img src="https://raw.githubusercontent.com/juanduranc/imgs/master/scatter1.png" />
<img src="https://raw.githubusercontent.com/juanduranc/imgs/master/scatter2.png" />


**Examples of scatterplot findings:**<br>
<ul>
  <li>The more time users watch preparation videos, the higher the expected revenue.</li>
  <li>The more clicks customers performs at the website, the less revenue they might bring.</li>
  <li>Customers should take at least 1 master class.</li>
</ul>


</body>
</html>


