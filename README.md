# Markov-Chain-Monte-Carlo
*Simulated Annealing for the Travelling Salesman Problem*
<p align='justify'>
The Travelling Salesman Problem is a NP-hard optimization problem, asking the question : "<i>Given a list of cities with their coordinates and a starting point, what is the shortest path that visits each city and returns to the starting point?</i>".  
<p/><p align='justify'>
It is theoretically possible to explore all possible path and save the best one. But in practice, the complexity of such an algorithm will explode in computing time but also in memory allocation if the number of given cities grows.
<p/><p align='justify'>
Since the trivial algorithm exploring all potential routes is not viable, many other algorithms have been developed to find at least one of the optimal solutions.
<p/><p align='justify'>
The Simulated Annealing algorithm is one of these algorithms, and will be explained here.
</p>
# Exhaustive Research
<p align='justify'>
An exhaustive research is feasible only when the number <i>m</i> of points is small. But since the number of possible route configuration grows by a factorial factor while <i>m</i>  increases, it fastly becomes impossible to compute the best configuration.
</p>
<p align='justify'>
How ever it is still interesting to compute such an algorithm and measure its time of execution while <i>m</i>  increases. 
</p>
First, we need to compute the whole configuration list.
<p align='justify'>
We know there are many existing algorithms for listing these configurations, but it tastes always better when it is homemade! 
Even if the purpose of this report is not to explain precisely how such an algorithm works, the corresponding python code <i>exhaustive.py</i>  can be found in this repository.
</p>
<p align='justify'>
Below is a table containing some measures taken following the number of cities *m*, and two images illustrating the result of the exhaustive research algorithm.
</p>
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

# The Simulated Annealing Algorithm
<p align= 'justify'>
Let the initial route where <img src="https://latex.codecogs.com/gif.latex?\sigma_0"/> is the departure city :
<p align='center'>
  <img src="https://latex.codecogs.com/gif.latex?\sigma^{[0]}=(\sigma_0,\sigma_1,...,\sigma_m)"/>
</p>

We compute the length of a route with the following formula :
<p align='center'>
  <img src="https://latex.codecogs.com/gif.latex?H(\sigma^{[i]})=\sum_{k=0}^{m-1}\delta(\sigma^{[i]}_k,\sigma^{[i]}_{k+1})+\delta(\sigma^{[i]}_m,\sigma_0)"/>
</p>
<p align='justify'>
Where <img src="https://latex.codecogs.com/gif.latex?\delta"/> is a function which compute the length between two cities given as parameters.
</p>
<p align='justify'>
The idea of the Simulated Annealing Algorithm applied to the Traveling Salesman Algorithm is to minimize the system's energy. Such an energy is here described as the length of the current selected route. Then, in order to minimize this energy, the target is to find the shortest route.
</p>
