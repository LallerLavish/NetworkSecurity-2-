from network_security.entity.artifact_entity import ClassificationMetricReport
from sklearn.metrics import f1_score,precision_score,recall_score
from network_security.exception.exception import NetworkSecurityException
import sys

def get_classification_report(y_true,y_pred)->ClassificationMetricReport:
    try: 
        f1_val=f1_score(y_true,y_pred)
        recall=recall_score(y_true,y_pred)
        precision=precision_score(y_true,y_pred)

        report=ClassificationMetricReport(
            f1_score=f1_val,
            recall=recall,
            precision=precision
        )
        return report
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)