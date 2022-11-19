"""
The purpose of this program is to simulate dice rolls in the game monopoly, which means no doubles.
"""

from random import randint
import plotly.graph_objects as go

rolls = {'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0}
for i in range(1000000):
  roll1 = randint(1,6)
  roll2 = randint(1,6)

  if roll1 == roll2:
    continue

  roll = roll1 + roll2

  for possibility in list(rolls.keys()):
    if roll == int(possibility):
      rolls[possibility] += 1


graph = go.Figure([go.Bar(x=list(rolls.keys()), y=list(rolls.values()))])
graph.write_html("monopoly_rolls.html")
"""
The roll data is in the html file. If you download that, you will be able to see the graph.
"""
