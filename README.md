# Clean Assist

Clean Assist is a simple library to help data scientists observe a summary of any DataFrame they would like to clean.<br>
This library also displays charts to view the normal approximation of your variables.

### To import library: copy paste the green colored code to your python code:
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

<h2>Sample</h2><br>
The following table is a sample of clean_assist(df, n_rows, n_round) output:<br><br>

<table>
     <tr>
      <th>VARIABLES</th>
      <th>NULLS</th>
      <th>COUNT</th>
      <th>TYPES</th>
      <th>MEAN</th>
      <th>MEDIAN</th>
      <th>UNIQUES</th>
      <th>SAMPLE</th>
      <th>Outliers</th>
      <th>pval(Norm)</th>
    </tr>
    <tr>
      <td>AVG_CLICKS_PER_VISIT</td>
      <td>0</td>
      <td>1946</td>
      <td>int64</td>
      <td>13.508222</td>
      <td>13.0</td>
      <td>15</td>
      <td><font size="6">[11, 13, 12, 13, 13, 17, 10, 13, 12, 12]</font></td>
      <td>[6,0]</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>MEDIAN_MEAL_RATING</td>
      <td>0</td>
      <td>1946</td>
      <td>int64</td>
      <td>2.794964</td>
      <td>3.0</td>
      <td>5</td>
      <td>[3, 3, 3, 3, 3, 2, 4, 3, 3, 3]</td>
      <td>[0,13]</td>
      <td>3e-06</td>
    </tr>
    <tr>
      <td>LARGEST_ORDER_SIZE</td>
      <td>0</td>
      <td>1946</td>
      <td>int64</td>
      <td>4.436793</td>
      <td>4.0</td>
      <td>12</td>
      <td>[6, 4, 3, 3, 3, 3, 6, 5, 4, 7]</td>
      <td>[0,33]</td>
      <td>3e-25</td>
    </tr>
    <tr>
      <td>TOTAL_PHOTOS_VIEWED</td>
      <td>0</td>
      <td>1946</td>
      <td>int64</td>
      <td>106.433710</td>
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
      <td>0.678828</td>
      <td>1.0</td>
      <td>2</td>
      <td>[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]</td>
      <td></td>
      <td>1e-159</td>
</table>

</body>
</html>
