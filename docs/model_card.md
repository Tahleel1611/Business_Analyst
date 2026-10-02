# Model card

The churn-risk baseline uses recency, frequency, and monetary value with logistic regression. The demo label is recency above the sample median. Production use requires a forward-looking label and time-based validation. The demand forecast is a transparent trailing three-month mean and does not model promotions, stockouts, holidays, or external variables.
