# Online Retail Marketplace

This domain models the clearest strategic core of `amazon.com`: a large-scale online retail marketplace that combines shopper demand, Prime convenience, third-party seller supply, fulfillment infrastructure, trust controls, and retail-media monetization.

Why this domain:

- `amazon.com` is most coherently modeled as a retail marketplace operating system rather than as a generic corporate domain.
- Amazon's consumer proposition depends on fast discovery, confident purchase decisions, Prime delivery convenience, and low-friction issue resolution.
- Amazon's business model compounds across marketplace fees, fulfillment services, subscriptions, and advertising, with third-party sellers now accounting for the majority of units sold.

Scope notes:

- The domain is kept current with the latest public materials (last refreshed 2026-07-04), not frozen as a point-in-time snapshot; Amazon's AI shopping assistant is therefore referred to by its current name, Alexa for Shopping (renamed from Rufus on 2026-05-13), while the stable internal ID `rufu` is retained.
- Internal operator and control-plane actors are modeled as customers, not only as teams and bricks: the Marketplace Trust & Compliance Operator and the Fulfillment & Customer Resolution Operator carry the jobs and guardrail KPIs behind fraud recovery, seller verification, returns abuse, delivery exception handling, and regulatory obligations.

Research summary (initial gather 2026-03-31, refreshed 2026-07-04):

- Amazon official stores and investor materials describe a business spanning Online Stores, Third-Party Seller Services, Subscription Services, and Advertising Services.
- Amazon states that independent sellers account for more than 60% of sales in the Amazon store.
- Amazon reported record delivery speed in 2025, with more than 13 billion items delivered the same or next day globally for Prime members and more than 8 billion in the U.S.
- Amazon states that Fulfillment by Amazon can reduce fulfillment cost per unit by up to 70% versus comparable premium options from major US carriers for participating sellers.
- Amazon positions Amazon Ads around closed-loop measurement, Sponsored Ads, DSP audiences, and retail-intent demand capture.
- Amazon positions Alexa for Shopping (its AI shopping assistant, renamed from Rufus on 2026-05-13), reviews, brand content, and fast delivery promises as shopper decision aids that increase confidence and reduce friction.

Domain hypothesis:

1. Shopper retention compounds when intent resolution, trust signals, and delivery reliability work as one system.
2. Seller growth depends on launch velocity, buyability, FBA economics, and measurable demand generation rather than listing alone.
3. Advertising growth is strongest when it is tightly connected to catalog quality, supply availability, and closed-loop purchase measurement.
4. Prime convenience is not only a benefit layer; it is a structural moat that raises frequency and lowers competitor consideration.
5. Marketplace trust, authenticity, and policy enforcement are foundational because fraud, counterfeit risk, and poor post-purchase handling break both shopper and seller economics.
