# tests/test_recipe_scorer.py
from tools.recipe_scorer import get_scored_recipes

def test_scored_contains_score():
    # Call scorer with sample pantry
    scored = get_scored_recipes(["rice", "eggs"])

    # Should return at least 1 recipe
    assert len(scored) > 0

    # Each recipe must have "score"
    assert "score" in scored[0]
