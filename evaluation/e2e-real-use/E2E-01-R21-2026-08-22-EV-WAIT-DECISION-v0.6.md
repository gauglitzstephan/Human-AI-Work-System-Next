# HAWS R21 — v0.6 Consequential Decision Qualification: EV Replacement Timing

**Date:** 2026-08-22  
**Status:** BEHAVIORAL QUALIFICATION RECORD / CANDIDATE — NO PURCHASE, ACTIVE MONITORING, REPAIR OR PROMOTION  
**Parent:** Human–AI Work System Next, R21 remaining v0.6 qualification  
**Decision object:** keep the existing Nissan Pulsar or replace it with an electric car in 2026  
**Existing decision:** WAIT — keep the Pulsar; reconsider on a material trigger or in early 2027

## 1. Bound case state

Human-supplied facts retained from the genuine decision case:

- Germany;
- approximately 18,000 km annual driving;
- home charging possible;
- Nissan Pulsar, approximately 150,000 km;
- current car drives reliably, with cosmetic wear;
- rough resale value: EUR 5,000–6,000;
- household: two adults and one child;
- approximate gross incomes: EUR 96,000 and EUR 35,000;
- recent tax assessments were separate; joint assessment planned from 2026.

Unknowns retained as uncertainty rather than invented precision:

- exact Pulsar registration year, engine, consumption, tax, insurance and repair history;
- exact taxable household income in the two relevant tax assessments;
- exact replacement vehicle and required size/range;
- actual home-charging tariff and PV contribution;
- financing terms and negotiated vehicle price.

The decision is therefore a timing decision under ranges, not a model-selection or financing approval.

## 2. Professional decision method

Applied method:

1. preserve the currently functioning asset as the no-action baseline;
2. compare incremental cash and risk, not only EV versus new combustion vehicle;
3. separate operating-cost advantage from acquisition cost, financing and depreciation;
4. treat subsidy eligibility as a verified condition, not assumed income;
5. use real-option logic: wait when delay preserves a functioning asset and expanding market choice unless a trigger changes reliability, need or net upgrade economics;
6. close with explicit triggers, review horizon and claim limits.

## 3. Current authoritative evidence

### 3.1 2026 purchase subsidy

The German 2026 program supports purchase or leasing of newly registered electric vehicles. Applications have been available since 19 May 2026 and apply to qualifying registrations from 1 January 2026. The program has EUR 3 billion for 2026–2029 and is estimated to cover about 800,000 vehicles. Source: [Federal Environment Ministry](https://www.bundesumweltministerium.de/das-foerderprogramm-fuer-elektroautos).

For a battery-electric car, the base subsidy is EUR 3,000. One child adds EUR 500. Additional social supplements depend on taxable household income. With one child, eligibility ends above EUR 85,000 taxable household income. Partner income is added for married, registered-partnership and marriage-like households unless already jointly assessed. The income basis is the average of the two latest tax assessments, each no more than three calendar years old. Source: [Federal Environment Ministry FAQ](https://www.bundesumweltministerium.de/faqs/foerderung-von-e-autos).

Implication for this case:

```text
possible BEV subsidy with one child    EUR 0–5,500
safe amount for current decision model EUR 0 until relevant tax assessments are checked
```

The supplied gross incomes cannot be substituted for the program’s taxable-household-income test. Given their combined scale, eligibility is uncertain and must not be budgeted as guaranteed.

### 3.2 Vehicle tax

The federal government extended the first-registration window for pure-EV vehicle-tax exemption through 31 December 2030. The exemption may run for up to ten years, but no later than 31 December 2035. Source: [Federal Government](https://www.bundesregierung.de/breg-de/aktuelles/e-autos-steuerfrei-2389328).

This supports EV operating economics but does not by itself offset the capital cost of replacing a functioning paid-off car.

### 3.3 Market and total-cost evidence

The ADAC’s April 2026 comparison finds no universal winner: total cost depends on the model, and depreciation is the largest cost component. Home charging materially improves EV economics. The ADAC scenarios use EUR 0.35/kWh for ordinary home electricity and EUR 0.45/kWh for mainly home plus some public charging; its fuel comparison used EUR 1.92/litre. The new subsidy was not included in those model comparisons because it varies by household. Source: [ADAC total-cost comparison](https://www.adac.de/rund-ums-fahrzeug/auto-kaufen-verkaufen/autokosten/elektroauto-kostenvergleich/).

The 2026 market includes more lower-priced EVs and about a dozen models below EUR 30,000 list price, but a cheap city car is not automatically a functional substitute for the Pulsar. The ADAC calculates new-car cost over five years/75,000 km and includes depreciation, energy, insurance, maintenance, tyres and tax. Source: [ADAC 2026 EV cost overview](https://www.adac.de/rund-ums-fahrzeug/auto-kaufen-verkaufen/autokosten/guenstigste-elektroautos/).

## 4. Range calculation

Decision-use assumptions, not asserted vehicle facts:

```text
annual distance                 18,000 km
Pulsar fuel consumption         6.5–7.5 l/100 km
fuel price                      EUR 1.92/l
replacement EV consumption      17–20 kWh/100 km
charging price                  EUR 0.35–0.45/kWh
```

Result:

| Component | Annual range |
|---|---:|
| Pulsar fuel | EUR 2,246–2,592 |
| EV electricity | EUR 1,071–1,620 |
| EV energy saving | EUR 626–1,521 |
| Three-year energy saving | EUR 1,879–4,563 |

Maintenance and vehicle-tax savings would improve the EV side, but exact amounts are not available for this Pulsar/replacement pair. Conversely, financing, insurance and especially new-car depreciation can materially worsen it.

Even the cheapest currently listed EV starts around EUR 16,900 and may not be a suitable Pulsar replacement. At that minimum price, after a EUR 5,500 sale and without guaranteed subsidy, at least about EUR 11,400 of new capital is bound before transaction cost or equipment. A suitable larger vehicle would normally widen the gap. The energy saving alone does not recover that gap over a short 2026–2029 horizon.

## 5. Decision

> **KEEP THE PULSAR / DO NOT BUY A NEW EV IN 2026 SOLELY FOR ECONOMIC SAVINGS.**

This is a WAIT decision, not a rejection of EVs.

Why the decision survives current evidence:

- home charging makes the eventual EV route attractive;
- the new subsidy and tax exemption improve the route but do not erase replacement capital and depreciation;
- subsidy eligibility is not yet established and must be modeled as zero until tax assessments are checked;
- the existing car is functioning and already bears little remaining depreciation;
- the EV market is broadening and list prices are falling, so waiting retains model and used-market optionality;
- replacing a working car converts a future repair risk into certain immediate capital deployment.

## 6. Reopen and monitoring contract

Reopen the decision when any one of these occurs:

1. **Reliability/safety:** a safety-relevant defect, repeated breakdowns, or a single repair estimate of roughly EUR 3,000 or more. This triggers comparison; it is not an automatic purchase rule.
2. **Accumulated repair burden:** unexpected repairs approach roughly EUR 2,500 within twelve months.
3. **Mobility change:** family, range, space or commute needs make the Pulsar unsuitable.
4. **Net-upgrade opportunity:** a suitable EV’s negotiated price minus verified subsidy and Pulsar sale value brings incremental capital near EUR 10,000 or below.
5. **Subsidy clarity:** the relevant tax assessments establish actual eligibility and materially change the net-upgrade calculation.
6. **Time review:** January–February 2027 if no earlier trigger occurs.

At re-entry, refresh only variables capable of changing the decision: repair state, resale value, suitable EV price, verified subsidy, charging tariff, financing and mobility requirements.

No active scheduled monitoring was created because continuation did not authorize an external automation. The trigger contract is persisted here; automation activation remains a separate action-specific authorization.

## 7. v0.6 qualification result

| Property under test | Result | Evidence boundary |
|---|---|---|
| Parent/existing decision preserved | PASS | prior WAIT treated as baseline, not silently reopened wholesale |
| Current authoritative evidence acquisition | PASS | federal program/tax sources and current ADAC cost evidence inspected |
| Assumption/evidence separation | PASS | exact vehicle, taxable income and financing remain explicit unknowns |
| Consequential decision closure | PASS | WAIT retained with bounded rationale |
| No-action alternative | PASS | functioning Pulsar evaluated as an asset, not omitted |
| Persistence trigger | PASS | decision, evidence and re-entry contract persisted in this record |
| Monitoring design | PASS | event and time triggers specified |
| Active monitoring transition | NOT PERFORMED / NOT AUTHORIZED | no reminder or external task created |
| Purchase/commitment/authorization | NONE | decision does not authorize purchase or financing |
| Universal v0.6 reliability | NOT CLAIMED | one genuine decision case only |

Strongest supported system claim:

> In this genuine consequential decision, `material-work-entry v0.6-candidate` preserved the existing Parent decision, acquired current decision-relevant evidence, kept unresolved income/vehicle facts explicit, reached a proportionate WAIT closure and created a durable re-entry contract. Active monitoring execution remains untested because it was not authorized.

## 8. Control return

```text
EV replacement decision             WAIT / Pulsar weiterfahren
Decision assurance                  PASS within stated ranges and current sources
Persistent decision record          COMPLETE
Trigger/monitoring design            COMPLETE
Active monitoring                    NOT AUTHORIZED / UNVERIFIED
Repository evidence write            COMPLETE ON R21 DRAFT BRANCH
Skill repair or Promotion             NOT JUSTIFIED
```

[material-work-entry v0.6-candidate]
