# Captains, start your turbines


### Modeling
In this case, for the most basic example, I'm going to represent each row in my matrix as a single point on the table. Then, it will have a label for being a "hit," versus not. So the model is binary: hit vs no hit.

### Application
Then, when we're playing the game, read the new board in. You'll have to convert it into your feature matrix, again looking at each point as a single row in your aray. Run that into your classifier. Return the point on the table that has the highest likelihood of being a hit. 