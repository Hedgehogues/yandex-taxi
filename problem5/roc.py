import numpy as np
from sklearn import metrics
y = np.array([0, 0, 1, 1])
pred = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, _ = metrics.roc_curve(y, pred, pos_label=1)
print(metrics.auc(fpr, tpr))
y = np.array([0, 0, 1, 1])
pred = 2 * np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, _ = metrics.roc_curve(y, pred, pos_label=1)
print(metrics.auc(fpr, tpr))
