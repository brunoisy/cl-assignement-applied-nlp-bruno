# CitizenLab Applied NLP Engineer Assignment

I developed a model to predict the topics present in an idea, to be used for suggesting topics and potentially 
automatically adding topics. The problem is an instance of multilabel text classification with missing labels.

To mitigate the issue of missing labels, I attempted to use only ideas which have 2 or more encoded topics 
(assuming that those where more likely to be complete). I was nevertheless unable to get decent performance in the required time.