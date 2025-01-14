"""Base model implementations for FFA forecasting."""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
import numpy as np
import pandas as pd


class BaseFFAModel(ABC):
    """Abstract base class for FFA forecasting models."""

    @abstractmethod
    def fit(self, features: pd.DataFrame, targets: pd.DataFrame) -> None:
        """Fit the model."""
        pass

    @abstractmethod
    def predict(self, features: pd.DataFrame) -> Dict[str, float]:
        """Generate predictions."""
        pass


