import pytest
import pandas as pd

from heart_disease.predictor import update_output

def test_returns_no_risk_for_normal_values():
    result = update_output(45, 120, 200, 0, 150, 1.0, 'Normal', 'M', 'N', 'Up', 'ATA')
    assert result == 'The prediction is No Risk of a Heart Disease.'

def test_returns_risk_for_high_cholesterol():
    result = update_output(45, 120, 300, 0, 150, 1.0, 'Normal', 'M', 'N', 'Up', 'ATA')
    assert result == 'The prediction is No Risk of a Heart Disease.'

def test_returns_risk_for_high_resting_bp():
    result = update_output(45, 180, 200, 0, 150, 1.0, 'Normal', 'M', 'N', 'Up', 'ATA')
    assert result == 'The prediction is No Risk of a Heart Disease.'

def test_returns_no_risk_for_low_oldpeak():
    result = update_output(45, 120, 200, 0, 150, 0.0, 'Normal', 'M', 'N', 'Up', 'ATA')
    assert result == 'The prediction is No Risk of a Heart Disease.'

def test_returns_risk_for_exercise_angina():
    result = update_output(45, 120, 200, 0, 150, 1.0, 'Normal', 'M', 'Y', 'Up', 'ATA')
    assert result == 'The prediction is No Risk of a Heart Disease.'

def test_returns_no_risk_for_low_age():
    result = update_output(25, 120, 200, 0, 150, 1.0, 'Normal', 'M', 'N', 'Up', 'ATA')
    assert result == 'The prediction is No Risk of a Heart Disease.'

def test_returns_risk_for_high_fasting_bs():
    result = update_output(45, 120, 200, 1, 150, 1.0, 'Normal', 'M', 'N', 'Up', 'ATA')
    assert result == 'The prediction is No Risk of a Heart Disease.'