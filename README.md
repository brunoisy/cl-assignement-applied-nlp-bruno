# CitizenLab Applied NLP Engineer Assignment

I developed a model to predict the topics present in an idea, to be used for suggesting topics and potentially 
automatically adding topics. The problem is an instance of multilabel text classification with missing labels.

To mitigate the issue of missing labels, I attempted to use only ideas which have 2 or more encoded topics 
(assuming that those where more likely to be complete). The measured performance of this model is really quite poor, see following report

| precision                   | recall | f1-score | support |     |
|-----------------------------|--------|----------|---------|-----|
| Netheid en afval            | 0.00   | 0.00     | 0.00    | 4   |
| Duurzame ontwikkeling       | 0.40   | 0.12     | 0.19    | 16  |
| Cultuur                     | 0.00   | 0.00     | 0.00    | 10  |
| Wonen                       | 0.00   | 0.00     | 0.00    | 19  |
| Technologie                 | 0.00   | 0.00     | 0.00    | 4   |
| Sociale inclusie            | 0.00   | 0.00     | 0.00    | 10  |
| Natuur en biodiversiteit    | 1.00   | 0.20     | 0.33    | 20  |
| Zorg en welzijn             | 0.00   | 0.00     | 0.00    | 8   |
| Burgerschap                 | 0.00   | 0.00     | 0.00    | 5   |
| Dienstverlening van de stad | 0.00   | 0.00     | 0.00    | 7   |
| Mobiliteit                  | 0.89   | 0.57     | 0.69    | 30  |
| Straten en pleinen          | 0.46   | 0.25     | 0.32    | 24  |
| economie                    | 0.00   | 0.00     | 0.00    | 7   |
| Sport                       | 0.00   | 0.00     | 0.00    | 5   |
| Onderwijs en jeugd          | 0.50   | 0.20     | 0.29    | 5   |
| micro avg                   | 0.70   | 0.17     | 0.28    | 174 |
| macro avg                   | 0.22   | 0.09     | 0.12    | 174 |
| weighted avg                | 0.38   | 0.17     | 0.23    | 174 |
| samples avg                 | 0.26   | 0.17     | 0.20    | 174 |

Only "Mobiliteit" and "Natuur en biodiversiteit" have reasonable precisions (but their recall is still quite low). 
This is unsurprising, as those are among the two topics for which we have the most data.

Used resources : https://towardsdatascience.com/multi-label-text-classification-with-scikit-learn-30714b7819c5