First I checked for the first input and it worked fine. The program ran fine and initialized the the root node.
Then I looked for the next inputs and the first issue I found was in a given condition if node.start <= self.end.
If this condition is true then we can have an overlapping time which we do not want. So we need to change the sign
>= to avoid overlapping.
Then while creating the right node we were setting it to the left child of the node which was wrong and we need to
set it to the right node.
Similar condition issue was with the next condition due to which it could have got overlapping time so I changed the
codition over there as well to avoid overlapping.
At last we were not returning false for any of the ovrlapping conditions so we were not getting any output in case 
of overlapping conditions so I returned a False in else part