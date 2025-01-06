#!/usr/bin/env bash
set -e

###############################################################################
# WARNING: This script performs renaming and removal of certain files/folders #
#          to keep the structure consistent with the new approach.           #
#          Ensure you have everything committed or backed up before running. #
###############################################################################

echo "=== Starting full rename and cleanup script ==="

### 1. Remove or rename files that are no longer relevant

# If you want to remove 'uw.lock' or references to 'uw' if present, uncomment:
# rm -f uw.lock || true

# If you want to remove 'uw.toml', uncomment:
# rm -f uw.toml || true

# If you want to remove 'poetry.lock' entirely, uncomment:
# rm -f poetry.lock || true

# Alternatively, if you just want to rename 'poetry.lock' for some reason, e.g. to 'poetry.lock.bak':
# mv poetry.lock poetry.lock.bak 2>/dev/null || true

# If you want to remove 'pyproject.toml', uncomment:
# rm -f pyproject.toml || true

### 2. Rename directories for clarity
# For instance, rename "agents" to "analysis_agents":
# If you prefer a different name, adjust accordingly.
echo "Renaming 'agents' to 'analysis_agents'..."
mv src/forecastiq/agents src/forecastiq/analysis_agents 2>/dev/null || true

# Also rename "main.py" -> "forecastiq_main.py" (example):
echo "Renaming 'main.py' to 'forecastiq_main.py'..."
mv src/forecastiq/main.py src/forecastiq/forecastiq_main.py 2>/dev/null || true

### 3. Rename orchestrator files for clarity
# Examples: static.py -> static_data_orchestrator.py, etc.
echo "Renaming orchestrator files..."

mv src/forecastiq/orchestrators/static.py   src/forecastiq/orchestrators/static_data_orchestrator.py   2>/dev/null || true
mv src/forecastiq/orchestrators/dynamic.py  src/forecastiq/orchestrators/dynamic_data_orchestrator.py  2>/dev/null || true
mv src/forecastiq/orchestrators/scenario.py src/forecastiq/orchestrators/scenario_orchestrator.py       2>/dev/null || true
mv src/forecastiq/orchestrators/forecast.py src/forecastiq/orchestrators/forecast_orchestrator.py       2>/dev/null || true
mv src/forecastiq/orchestrators/insights.py src/forecastiq/orchestrators/insights_orchestrator.py       2>/dev/null || true

### 4. Rename test files if desired
echo "Renaming test_basic.py to test_sanity.py (example)..."
mv tests/test_basic.py tests/test_sanity.py 2>/dev/null || true

### 5. Create or rename a graph-based workflow structure
# If the graph structure doesn't already exist, create it:
echo "Ensuring a 'graph' directory for state machine logic..."
mkdir -p src/forecastiq/graph/nodes
touch src/forecastiq/graph/__init__.py
touch src/forecastiq/graph/nodes/__init__.py
# Create placeholders if they don't exist
touch src/forecastiq/graph/state.py       # Where AgentState or typed dict might go
touch src/forecastiq/graph/workflow.py    # Where we define/compile StateGraph
touch src/forecastiq/graph/nodes/start_node.py
touch src/forecastiq/graph/nodes/end_node.py

### 6. Create a "tools" directory for utilities, if not present
echo "Setting up a 'tools' directory for utility code..."
mkdir -p src/forecastiq/tools
touch src/forecastiq/tools/__init__.py
touch src/forecastiq/tools/data_io.py
touch src/forecastiq/tools/transformations.py

### 7. Display final structure
echo "=== Final Directory Structure (excluding __pycache__ and .pyc) ==="
tree -I '__pycache__|*.pyc' .

echo "=== Rename and cleanup complete. Review changes to ensure correctness. ==="
