"""Tests for hierarchical FFA forecasting."""
import pytest
import numpy as np
import pandas as pd
from marinesense.models.hierarchical.hierarchical_ffa import HierarchicalFFAModel


def test_hierarchical_model_initialization():
    model = HierarchicalFFAModel(
        route='C5',
        tenors=['1M', '2M', '3M'],
        hierarchy_levels=['route', 'regional', 'global']
    )
    assert model.route == 'C5'
    assert len(model.tenors) == 3


