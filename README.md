# Clean Assist

Clean Assist is a simple library designed to help data scientists observe a summary of any DataFrame they would like to clean.
This library also displays charts to view the normal approximation of your variables.<br>

**Clean Assist is composed of 2 functions:**
1. clean_assist(df, n_rows, n_round)<br>
    Displays relevant features to help you on data cleaning and analysis.<br>
    
    PARAMETERS<br>
    ----------<br>
    df  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   : DataFrame you would like to analyze<br>
    n_rows  : Number of variables to display<br>
    n_round : Number of decimals to round calculations<br>
2. view_normality(df, list_var, print_img, size_x, size_y, font_size)<br>

### To import the library: copy paste the green colored code to your python code:
```diff
- Note: Ignore the plus(+) signs
```
```diff
+ import requests
+ url = 'https://raw.githubusercontent.com/juanduranc/categorical_distribution_juan/master/info'
+ exec(requests.get(url).text)
```

<!DOCTYPE html>
<html>
<body>

<h3>Example of library usage and interpretation:</h3>
The following table is a sample of an output clean_assist(df, n_rows, n_round) output:<br><br>

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
</table>

<img src="https://raw.githubusercontent.com/juanduranc/Clean-Assist/master/normality.png" />

</body>
</html>
