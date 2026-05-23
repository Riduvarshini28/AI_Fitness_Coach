# expert_system.py
from knowledge_base import knowledge_base

def _match_condition(user_value, cond_value):
    """
    Return True if user_value satisfies cond_value.
    cond_value may be string exact, or starting with '>' or '<' for numeric comparisons.
    """
    try:
        # numeric comparisons
        if isinstance(cond_value, str) and cond_value.startswith(">"):
            return float(user_value) > float(cond_value[1:])
        if isinstance(cond_value, str) and cond_value.startswith("<"):
            return float(user_value) < float(cond_value[1:])
    except Exception:
        # fall through to string compare
        pass
    # fallback to string equality (case-insensitive)
    return str(user_value).strip().lower() == str(cond_value).strip().lower()

def infer(user_facts):
    """
    Forward-chaining: evaluate all rules and return list of recommendations with reasons.
    user_facts: dict of user attributes
    """
    recommendations = []
    for rule in knowledge_base:
        conds = rule.get("if", {})
        match = True
        for attr, cond_val in conds.items():
            if attr not in user_facts:
                match = False
                break
            if not _match_condition(user_facts[attr], cond_val):
                match = False
                break
        if match:
            then = rule.get("then", {})
            recommendations.append(then)
    return recommendations

def explain(recommendations):
    """
    Build a textual explanation for recommendations (list of 'then' dicts)
    """
    lines = []
    for rec in recommendations:
        # join key: value pairs excluding Reason (we include Reason)
        items = [f"{k}: {v}" for k, v in rec.items() if k != "Reason"]
        reason = rec.get("Reason", "")
        text = "; ".join(items)
        if reason:
            text += f"  (Why: {reason})"
        lines.append(text)
    return lines
