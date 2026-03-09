# Derived Variables

## ideology_score
- Definition: Placeholder numeric scale representing respondent ideology.
- Inputs: `ideology_self_placement`, recode rules.
- Notes: Confirm treatment of missing and out-of-range values.

## party_id
- Definition: Harmonized party identification category.
- Inputs: Raw party ID variables from each ANES vintage.
- Notes: Keep a crosswalk by year before collapsing categories.

## race_category
- Definition: Standardized race grouping used in analysis panels.
- Inputs: Race and ethnicity questionnaire items.
- Notes: Preserve both mutually-exclusive and multi-select versions when possible.

## vote_choice_binary
- Definition: Binary indicator for selected vote choice in target election.
- Inputs: Presidential vote items and validated vote fields.
- Notes: Document exclusions and third-party handling.
