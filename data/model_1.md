## Parameters we're using for model 1:


### actual parameters:
* horse_no
* result
* win_percentage (calculated by us)
* horse_age
* if_gelding
* if_brown
* if_horse
* if_colt
* if_mare
* if_rig
* if_roan
* if_filly
* horse_rating
* declared_weight
* actual_weight
* draw

(race_id will group the horses together by race)

### What are we trying to find?
We are trying to find each horse's probability of winning 1st place.

### What loss function do we need to find that?
We need to minimize cross-entropy loss
Here's a helpful link: https://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html#cross-entropy

### How do we handle varying amount of horses per race?
Create "0 horses": These horses need to be back of the pack and all binary variables should be set to 0. For example, if 12 real horses are racing, we would have 2 "0 horses" who place 13th and 14th

### What does the model look like?
Input layer is 14*16 nodes (which are our 16 input variables multiplied by the 14 horses)
Hidden layer 1 will range over [32, 64, 128, 256, 512, 1024] (x)
Hidden layer 2 will have twice the number of nodes as layer 1 (2x)
Hidden layer 3 will have the same amount of nodes as layer 1 (x)
Output layer will have size 14 (for the 14 horsies)

### Breakdown of training/test data
First 60k rows will be training data
Remaining rows will be test data


### NOTES FOR THE FUTURE
Include ids as a categorical variable (build some sort of meaningful relationship)
Include individual horse racing results as children from race data (this connects the two)
Make sure you get both a cream-colored Maybach and a jet black one.
