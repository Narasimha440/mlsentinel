"""
Validation functions for MLSentinal SDK
"""

from .exceptions import (
    ProjectValidationError,
    ModelValidationError,
    MetricValidationError,
)

def validate_project(project: str):

    if not isinstance(project, str):
        raise ProjectValidationError(
            "Project name must be in string."
        )
    
    if not project.strip():
        raise ProjectValidationError(
            "Project name connot be empty."
        )
    

def validate_model(model: str):

    if not isinstance(model, str):
        raise ModelValidationError(
            "Model name must be in string."
        )
    
    if not model.strip():
        raise ModelValidationError(
            "Model name cannot be empty."
        )
    
def validate_metrics(metrics: dict):

    if not isinstance(metrics, dict):
        raise MetricValidationError(
            "Metrics should be in dictionary."
        )
    
    if len(metrics) == 0:
        raise MetricValidationError(
            "Metrics dictionary cannot be empty."
        )
    
    for metric_name, value in metrics.items():

        if not isinstance(value, (int, float)):
            raise MetricValidationError(
                f"{metric_name} must be numeric."
            )
        
        if metric_name != "val_loss":

            if value < 0 or value > 1:
                raise MetricValidationError(
                    f"{metric_name} must be between 0 and 1."
                )
            
        else:
            
            if value < 0:
                raise MetricValidationError(
                    "Validation loss cannot be negative."
                )