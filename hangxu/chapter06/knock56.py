import knock51
from knock51 import test
import knock52
from knock52 import model
import knock54
from knock54 import test1

from sklearn.metrics import classification_report
print(classification_report(test['CATEGORY'], test1, labels=['b', 'e', 'm', 't']))
