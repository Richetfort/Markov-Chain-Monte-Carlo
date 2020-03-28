# Markov-Chain-Monte-Carlo
*Simulated Annealing for the Travelling Salesman Problem*

The Travelling Salesman Problem is a NP-hard optimization problem, asking the question : "*Given a list of cities with their coordinates and a starting point, what is the shortest path that visits each city and returns to the starting point?*".  

It is theoretically possible to explore all possible path and save the best one. But in practice, the complexity of such an algorithm will explode in computing time but also in memory allocation if the number of given cities grows.

Since the trivial algorithm exploring all potential routes is not viable, many other algorithms have been developed to find at least one of the optimal solutions.

The Simulated Annealing algorithm is one of these algorithms, and will be explained here.

# Exhaustive Research

An exhaustive research is feasible only when the number *m* of points is small. But since the number of possible route configuration grows by a factorial factor while *m* increases, it fastly becomes impossible to compute the best configuration.

How ever it is still interesting to compute such an algorithm and measure its time of execution while *m* increases. 

First, we need to compute the whole configuration list.

We know there are many existing algorithms for listing these configurations, but it tastes always better when it is homemade! 
Even if the purpose of this report is not to explain precisely how such an algorithm works, the corresponding python code ``exhaustive.py`` can be found in this repository.

Below is a table containing some measures taken following the number of cities *m*, and two images illustrating the result of the exhaustive research algorithm.

<table align = 'center'>
<tr align = 'center'>
  <th>m</th>
  <th>Number of routes</th>
  <th>Computation time (s)</th>
  <td rowspan=10><img src = 'images/start.png'></td>
<tr>
<tr align = 'center'>
  <td>4</td>
  <td>6</td>
  <td>0.0008</td>
<tr>
<tr align = 'center'>
  <td>5</td>
  <td>24</td>
  <td>0.0042</td>
<tr>
<tr align = 'center'>
  <td>6</td>
  <td>120</td>
  <td>0.0179</td>
<tr>
<tr align = 'center'>
  <td>7</td>
  <td>720</td>
  <td>0.1433</td>
<tr>
<tr align = 'center'>
  <td>8</td>
  <td>5040</td>
  <td>1.1130</td>
  <td rowspan=8><img src = 'images/end.png'></td>
<tr>
<tr align = 'center'>
  <td>9</td>
  <td>40320</td>
  <td>10.121</td>
<tr>
<tr align = 'center'>
  <td>10</td>
  <td>362880</td>
  <td>100.69</td>
<tr>
<tr align = 'center'>
  <td>11</td>
  <td>10!</td>
  <td>/!\ MY LAPTOP CRASHED /!\</td>
<tr>
</table>
