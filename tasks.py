def grade_easy(actions):
    # spam detection
    return 1.0 if "classify:spam" in actions else 0.0


def grade_medium(actions):
    # classify boss email
    return 1.0 if "classify:important" in actions else 0.0


def grade_hard(actions):
    # priority handling
    if "prioritize:high" in actions and "classify:important" in actions:
        return 1.0
    return 0.5 if "classify:important" in actions else 0.0