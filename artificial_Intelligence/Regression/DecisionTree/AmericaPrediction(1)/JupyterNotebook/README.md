<h1 align="center">I can explain this "Alternate History"...</h1>

<h3 align="center">What are decision trees and why I chose them?</h3>

<p>Decision trees are a type of AI/Machine Learning algorithm that aims to learn how the data works by creating partitions. Decision trees are a popular alternative to Neural Networks and Deep Learning, which are heavily used by colleges and the private sector(I won't complain, as they can take the computational burden of a Neural Network, as they take up lots of computation power; they are essentially useless unless you have more than 100,000 data points). This is the reason I chose Decision Trees, as they are essentially the knock-off "Neural Networks" that can accomplish similar feats without putting a huge burden on the computer and is fairly accurate with the amount of data I have(a neural network will just be wrong, unless I have more data). Anyway, decision trees create partitions in data that follow a certain pattern: when x is greater than 5, y does this. It isn't that simple, but it is good enough to get a basic enough idea. With decision trees, entropy, or the variance of the data set as the result of a partition, looks at the variance and tries to minimize itself(again, oversimplified). The partition that has the least entropy is made by the decision tree. The partitions will keep on happening until the entropy is zero. However, as I put a limit on the variable max_depth, it can't do that. The problem with letting entropy fall to zero is that it leads to overfitting: it fits the training data so well that it can't be used to analyze other datasets. Anyway, I should stop rambling about decision trees so that you can read about the data and the projection(you might call me a prophet of doom after you read, so read with caution).</p>

<h3 align="center">Original Data</h3>
<p>In this directory, using Jupyter Notebook to create an AI(Artificial Intelligence) model, I predicted that America, with high tariffs, will have its working 
generation live like the Baby Boomers(or Homer Simpson) But first, one needs to look at the dataset I trained the model on, and I have it on a graph to see.</p>

![image](https://user-images.githubusercontent.com/48994987/216375810-6ddc1ae7-be72-4c27-80d7-91835b3d65d3.png)

<h6 align="center">Fertility Rates and Debt</h6>

<p>As we can see, the 1920s saw the decline in birth rates, which is the decline in "standard of living"(THIS DOES NOT APPLY TO MATERIAL STANDARD OF LIVING)
when accounting for change in ideology and whether the economic system is sustainable(as we can see, the 1920s wasn't sustainable economics). Also, with 
fertility rates, a change in ideology shows a change in society, which is reflected through fertility rates, like how the baby boomers were different from
their parents in terms of ideology and they had a lot less children than their parents. Their ideology was less connected to god and more connected to just
chilling and doing whatever you felt like. There wasn't honour. Take the Vietnam war: the Baby Boomers didn't feel like they had to support the war because
they didn't have to go beyond what their ancestors did. This is one reason why the Vietnam War wasn't a popular war(another one is linked to television, or
maybe television led to an ideological shift for the Baby Boomers). Also, humans are naturally animals, and so we would have to spread our genes, unless our
new ideology justifies us for not having children, but for the most part, preserving the "group's genes" is important for the survival of the group(maybe that
is why the birth rate fell with baby boomers, they were the first generation who didn't have to care a whole lot about the survival of their group). Back to debt,
I just want to say that one can't have kids and then pay for the extra kid with the debt(some people might, who knows), but for the most part, debt is usually to help
sustain their life in hard times, or maybe bathe in luxuries during hard times(depends on who you are or how "hard" the times were, but most people decide not to have
another child when they have to be funded with debt. While the residence you and your children live in is paid with debt, and the costs of food might be funded with
debt, that doesn't mean that you will have another child because you can take out debt. Anyway, I would like to move on to inflation.</p>

<h6 align="center">Inflation</h6>

<p>Inflation, a metric that some countries just can't avoid being near the top. But more importantly, an indicator on how much energy the economy has. High inflation
is an economy with high energy, but it will eventually crash, like what happens to a kid after a "sugar rush". A low inflation economy doesn't have much energy and
is generally quite stagnant. What one should aim for is the sweet spot of around 2% annual inflation. The economy has energy, but not enough to just suddenly crash
whenever something goes wrong. Anyway, in the 1920s, the economy, for the most part, wasn't very energetic. One explaination is that during WWI, countries were 
producing so many supplies that they would be considered surplus at peacetime. However, that production carried over to the 1920s, and things were cheap(not good
news). While it meant that people could afford things easily, it also meant that there wasn't much competition to make things(sort've like there is now), but also
businesses weren't turning a profit, which hurt the economy. This is why you see the rise in tariffs in the 1920s, as it was needed to make sure the economy was doing
well despite the low inflation. Going into the Great Depression, inflation rates were below zero, which was a sign of how the economy pretty much grinded to a halt.
It was like during COVID when prices were really cheap, and companies also laid off lots of workers because of the lack of profits, which did come because of the 
lack of demand, but the Great Depression was different. Inflation was low from the beginning, and the house of cards fell when the stock market began to crash. 
Anyway, FDR saves the nation and inflation during WW2 is around 6 percent a year. Tariffs also ease as the economy is doing quite well. The inflation helped to
spur short term growth, which made America worth 1/2 the world economy at the end on World War 2. Once the 1950s came in, inflation was moderate(at the "golden"
level) and people were living fine lives. However, America was growing increasingly dependent on the outside world, and soon, inflation would kick in because
of the rapid rise in spending coupled with the expenses of the Vietnam War, which explains the rise in inflation. With America growing dependent on the outside
world due to globalization, a new crisis would come: the 1973 Recession!</p>

<a href="https://files.stlouisfed.org/files/htdocs/publications/review/69/12/Battle_Dec1969.pdf">Federal Reserve Report on Rising Inflation of the 60s</a>

<h6 align="center">Tariffs</h6>

<p>As we all know, tariffs help to protect the economy. Tariffs are generally a reaction to economic problems, like the increased protectionism after the 
Long Depression(late 1800s). Fun fact: the Long Depression was called the Great Depression before what we call the Great Depression happened. During the 1920s,
the economy was pretty sluggish in terms of growth, which was partially manifested in tariff. During the Great Depression, tariff rates went through the roof
in an effort to stop the Great Depression(it didn't work). While it might work for smaller scale recessions, the Great Depression affected the economy so deeply
that even this didn't work. A full revamp of the economy was needed, which is where FDR comes. America recovers, and decideds to spread its power via the
Bretton Woods Agreement near the end of WW2. When there is one economic superpower, it is easy to get everypne on the same page like the Bretton Woods agreement
did. In the next prediction, there will be more to say on tariffs other than a basic rundown.</p>

<h6 align="center">Foreign Born Percentage</h6>

<p>Immigration, a hotly debated issue in American politics. I just want to do a quick overview on immigration's effects on society(its not really biased). First,
immigration can add culture to a society, like how hot dogs are considered American food even though they were origninally German food. Second, in our moden world
where birth rates are plummeting, immigration can keep a constant stream of young workers even if the local birth rate is sluggish. However, immigration can also
threaten the culture of a society, which is why countries like Japan, despite having some of the lowest birth rates in the world, doesn't want to support 
immigration so that the homogenity of Japan. However, in America, a homogenous culture is constantly updated as the foreign born population remains constant or
declines in its share of the population, like the hot dog example. Another example is in antebellum America, many Scandinavians settled in America, and the post
World War II era and even now, there is an American cultural interest in Scandanavian culture(like Minnesota Vikings or all the Viking movies you might've heard
about). Overall, there is not much data about immigration other than decreasing immigration rates were seen from the 1910s and continued to the 1970s, and the
time after the Great Depression was a time of gains for many. Maybe they are possibly correlated. In the next analysis, I will look deeper into immigration as 
spoiler alert: immigration looks like a stable cycle of predicting future America.</p>

<h3 align="center">Alternate History Part</h3>

![image](https://user-images.githubusercontent.com/48994987/216721615-d489fcc7-1154-477c-93e6-57fcede90b15.png)

<p>So, as you can see, the fertility rate of our time(in this parallel universe) is high, just like when the Baby Boomers were little(what a nice time to be alive).
Anyway, the 1970s sees a rise in fertility rates. I would say that is because the model picked up on the post Great Depression high inflation and increase in 
fertility rates and thought that this is just like the Great Depression(it ain't). I would expect the opposite as the 1970s weren't a great time to be alive.
The government literally had to ration car fuel(because the inflation was so high). Anyway, we move into the terrible 1980s(also makes little sense as Reagan
saw great economic growth in the short term with the long term effects of his policies being debated). America then begins to increase tariffs, and now, its 
citizens live life like they did 70 years ago. Now of course, we all know that that isn't true, there are recessions and many other factors that make predictions
wrong, and not: this guy will win the election, but: America will experience a trouble in the coming years. But overall, I'd look forward to the next prediction.</p>

<a href="https://github.com/akhilmanhattan/cliodynamics/tree/main/America/1">The Next Prediction(at least its not an alternate history)</a>
