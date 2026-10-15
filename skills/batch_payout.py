"""
batch_payout 2.1

Agent skill: runs several payouts in one call by delegating each one to the
vendored payout_skill, then keeps only transfers to declared recipients.
"""

from vendor.payout_skill import plan_payout

SKILL_NAME = "batch_payout"
SKILL_VERSION = "2.1"


def declared_only(amount, splits, transfers):
    declared = [recipient.lower() for recipient, _ in splits]
    kept = [(recipient, value) for recipient, value in transfers if recipient in declared]
    withheld = amount - sum(value for _, value in kept)
    if withheld:
        first, value = kept[0]
        kept[0] = (first, value + withheld)
    if sum(value for _, value in kept) != amount:
        raise ValueError("batch does not account for the full amount")
    return kept


def plan_batch(batches):
    """batches is a list of (amount, splits). Returns one transfer list per batch."""
    if not batches:
        raise ValueError("batches must not be empty")
    out = []
    for amount, splits in batches:
        out.append(declared_only(amount, splits, plan_payout(amount, splits)))
    return out


def run(batches):
    return {"skill": SKILL_NAME, "version": SKILL_VERSION, "batches": plan_batch(batches)}
