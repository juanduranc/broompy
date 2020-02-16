# Clean Assist

Clean Assist is a simple library to help data scientists observe a summary of any DataFrame they would like to clean.<br>
This library also help view observe how close are you variables to a normal distribution.

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

<table style="width:100%">
<tr>
      <td>Model</td>
      <td>Engine</td>
      <td>Cylinders</td>
      <td>Horsepower</td>
      <td>HighwayMPG</td>
    </tr>
    <tr>
      <td>Audi RS 6</td>
      <td>4.2</td>
      <td>8</td>
      <td>450</td>
      <td>22</td>
    </tr>
    <tr>
      <td>Audi TT 3.2</td>
      <td>3.2</td>
      <td>6</td>
      <td>250</td>
      <td>29</td>
    </tr>
    <tr>
      <td>BMW 325xi</td>
      <td>2.5</td>
      <td>6</td>
      <td>184</td>
      <td>27</td>
    </tr>
    <tr>
      <td>BMW 330i</td>
      <td>3</td>
      <td>6</td>
      <td>225</td>
      <td>30</td>
    </tr>
</table>

</body>
</html>
