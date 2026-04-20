#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

scripts=(
  "generate-start-docs.py"
  "generate-customers-docs.py"
  "generate-products-docs.py"
  "generate-product-bricks-docs.py"
  "generate-delivery-docs.py"
  "generate-objectives-docs.py"
  "generate-teams-docs.py"
  "generate-scorecard-docs.py"
  "generate-competition-docs.py"
)

domains=(
  "ride-sharing-marketplace|Ride Sharing Marketplace|The Ride Sharing Marketplace domain covers the rider, driver, fleet, business-travel, and marketplace-operations workflows required to run an on-demand and scheduled rides platform with dynamic pricing, dispatch, trust, and multimodal extensions."
  "enterprise-crm-and-revenue-operations|Enterprise CRM and Revenue Operations|The Enterprise CRM and Revenue Operations domain covers lead-to-cash execution, customer service operations, customer data unification, workflow automation, and platform governance for large B2B and B2C organizations."
  "digital-news-publishing-platform|Digital News Publishing Platform|Covers the audience, editorial, advertising, subscription, loyalty, partner-bundle, and data capabilities required to run a multi-brand digital news publisher across web, apps, print-linked editions, social, newsletters, and commercial partnerships."
  "technical-design-collaboration-platform|Technical Design Collaboration Platform|Product-led B2B SaaS company serving engineering organizations with AI-assisted technical design and collaboration workflows."
  "mental-wellbeing-community-platform|Mental Wellbeing Community Platform|Covers the member, employer, contributor, and trust workflows required to operate a digital mental wellbeing platform built around community support, live programming, on-demand content, and employer-sponsored access."
  "industrial-water-intelligence|Industrial Water Intelligence|The Industrial Water Intelligence domain covers connected water treatment, plant-system monitoring, enterprise water analytics, wastewater compliance, and reuse workflows used by water-intensive industrial operators to improve uptime, conserve water, reduce energy and chemistry waste, and prove financial impact."
  "big-enterprise|Big Enterprise|The Big Enterprise domain covers the tools, workflows, and enabling capabilities used by internal teams and enterprise employees across revenue and growth, service, operations, finance, control, workplace, and internal productivity."
  "ignore_iwt|ImmoWelt|The ImmoWelt domain covers the customer journeys, commercial workflows, and platform capabilities required to connect property seekers, owners, intermediaries, and partners."
  "emobility|eMobility|The eMobility domain covers the platforms, operations, and customer journeys required to run charging networks, roaming services, driver experiences, and fleet electrification at scale."
  "nutrition|Nutrition|The Nutrition domain covers the products, capabilities, and stakeholders needed to design, produce, govern, and improve nutrition solutions with strong compliance, quality, and sustainability outcomes."
  "real-estate-marketplace|Real Estate Marketplace|The Real Estate Marketplace domain covers the customer journeys, commercial workflows, and platform capabilities required to connect property seekers, owners, intermediaries, and partners."
  "general-listings-marketplace|General Listings Marketplace|Covers the customer journeys, trust mechanisms, commercial workflows, and platform capabilities required to run a broad local classifieds marketplace across goods, vehicles, services, jobs, and professional storefront supply."
  "maas|Mobility-as-a-Service (MaaS)|The products, workflows, and platform capabilities required to run parking, curbside, public transport payments, fleet mobility, city-planning intelligence, and partner ecosystems at global urban-mobility scale."
  "platform-engineering|Platform Engineering|The Platform Engineering domain covers the internal developer platforms, golden paths, runtime foundations, delivery guardrails, and reliability workflows used by product and technology teams to ship software faster, safer, and with lower cognitive load."
  "mambu|Mambu|The Mambu domain covers the banking products, platform capabilities, and ecosystem integrations needed for lenders and financial institutions to launch and scale modern cloud-native banking services."
  "payments-and-revenue-infrastructure|Payments and Revenue Infrastructure|The Payments and Revenue Infrastructure domain covers the merchant, platform, finance, and risk workflows required to accept payments globally, automate recurring revenue, orchestrate multi-party funds flows, and operate internet-scale commerce with compliance and financial control."
  "bike-mobility|Bike Mobility|The Bike Mobility domain covers the products, workflows, and platform capabilities required to launch and scale employer-backed bike leasing, rider services, dealer ecosystems, pooled bike fleets, and lifecycle services across European markets."
  "premium-long-haul-airline|Premium Long-Haul Airline|The Premium Long-Haul Airline domain covers the products, workflows, and platform capabilities required to retail, operate, service, recover, and grow a premium airline across long-haul passenger travel, holidays, loyalty, partner connectivity, and cargo."
  "travel-accommodations-marketplace|Travel Accommodations Marketplace|The Travel Accommodations Marketplace domain covers the traveler journeys, partner workflows, trust controls, merchandising systems, and platform capabilities required to run a global accommodations marketplace across hotels, homes, apartments, hostels, and managed travel stays."
  "hosted-stays-marketplace|Hosted Stays Marketplace|The Hosted Stays Marketplace domain covers the guest, host, co-host, trust, payment, and compliance workflows required to run a global marketplace for homes, rooms, and professionally managed short-term rental stays."
  "audio-streaming-platform|Audio Streaming Platform|The Audio Streaming Platform domain covers the listener, creator, rights-holder, and advertiser workflows required to run a global audio platform spanning music, podcasts, video podcasts, audiobooks, subscriptions, creator growth, and advertising monetization."
  "online-retail-marketplace|Online Retail Marketplace|The Online Retail Marketplace domain covers the shopper, Prime, seller, fulfillment, retail-media, trust, and shared-commerce workflows required to run a scaled digital retail marketplace across first-party retail, third-party supply, subscriptions, and advertising."
  "municipal-public-space-enforcement|Municipal Public Space Enforcement|The devices, workflows, legal procedures, and analytics that help local authorities detect public-space offences, build enforceable cases, coordinate field action, and demonstrate visible resident impact without intrusive surveillance."
  "travel-and-expense-management|Travel and Expense Management|Expense management, travel expense flows, mileage, per diem, approvals, policy, card reconciliation, and finance integrations"
)

for script in "${scripts[@]}"; do
  for domain in "${domains[@]}"; do
    IFS='|' read -r domain_id domain_name domain_description <<< "$domain"
    python3 "$script" "$domain_id" "$domain_name" "$domain_description"
  done
done
