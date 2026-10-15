# quarantine-demo-wrapper

Demo fixture for Quarantine V2, transitive exposure.

`skills/batch_payout.py` is a wrapper skill. It vendors `payout_skill` from quarantine-demo-skills at `vendor/payout_skill.py`.

- 2.0 vendors payout_skill 1.1 and calls it raw
- 2.1 vendors payout_skill 1.1 and keeps only transfers to declared recipients
- 2.2 vendors payout_skill 1.2

Do not use this skill in any real deployment.
