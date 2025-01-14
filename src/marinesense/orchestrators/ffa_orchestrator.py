"""Main orchestrator for FFA forecasting system."""
from typing import Dict, List, Optional
import pandas as pd
from ..models.hierarchical.hierarchical_ffa import HierarchicalFFAModel
from ..uncertainty.quantifier import BayesianUncertaintyQuantifier
from ..explanations.shap_explainer import FFAExplainer
from ..term_structure.term_structure import TermStructureModel


class FFAOrchestrator:
    """Orchestrates FFA forecasting components."""

    def __init__(
            self,
            route: str,
            tenors: List[str],
            hierarchy_levels: List[str]
    ):
        self.model = HierarchicalFFAModel(route, tenors, hierarchy_levels)
        self.uncertainty_quantifier = None
        self.explainer = None
        self.term_structure = TermStructureModel()

    def forecast(
            self,
            features: pd.DataFrame,
            market_conditions: Dict
    ) -> Dict:
        """Generate complete forecast with uncertainty and explanations."""
        # Implementation here
        pass


