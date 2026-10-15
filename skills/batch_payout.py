"""
batch_payout 2.2

Agent skill: runs several payouts in one call by delegating each one to the
vendored payout_skill. 2.2 vendors payout_skill 1.2.
"""

from vendor.payout_skill import plan_payout

SKILL_NAME = "batch_payout"
SKILL_VERSION = "2.2"


def plan_batch(batches):
    """batches is a list of (amount, splits). Returns one transfer list per batch."""
    if not batches:
        raise ValueError("batches must not be empty")
    return [plan_payout(amount, splits) for amount, splits in batches]


def run(batches):
    return {"skill": SKILL_NAME, "version": SKILL_VERSION, "batches": plan_batch(batches)}
