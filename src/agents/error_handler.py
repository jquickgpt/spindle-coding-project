def detect_failure(results):
    """Detects potential failures by checking result consistency."""

    if results.count(None) > len(results) * 0.4:
        return {"warning": "High failure rate detected. Results may be unreliable."}

    return {"status": "Results stable."}
