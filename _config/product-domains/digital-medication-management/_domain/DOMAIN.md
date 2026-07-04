# Digital Medication Management — Domain Brief

*Modeled on Evondos Group, a European leader in automated medicine dispensing and
remote medication management for home care and supported living. Figures below are
company-reported unless a source is cited and should be treated as illustrative of a
real business, not audited fact.*

## 1. Company snapshot

Evondos Group provides automated medicine dispensing and medication-management
**services** — not just a device — mainly for home care, elderly care, supported
living, and municipal/care-provider settings. Its core promise is simple: the right
medication, at the right time, to the right person, with remote monitoring and
escalation if something goes wrong. Evondos describes itself as a leading provider of
automated medicine dispensing services in Northern Europe; company material refers to
more than **120 million medication sachets/doses** dispensed.

The company's public timeline is meaningful: the idea dates to **2007**, R&D and
clinical trials followed, CE marking came in the early 2010s, Nordic subsidiaries
followed, **Verdane** became a growth partner in 2020, **Medido** (Netherlands) was
acquired in 2023, **VitaCam** in 2024, and a UK subsidiary was established in 2025.

| Area | What we found |
|---|---|
| Core product | Automated medication-dispensing device + cloud/telecare monitoring, support, training, audit trail, and pharmacy pouch workflow |
| Main markets | Nordics (Finland, Sweden, Norway, Denmark), Netherlands, UK, and broader European expansion |
| Ownership | Verdane-backed; positioned as a European leader in automated medicine dispensing and medication management |
| Scale claims | ~40,000 devices deployed, 700+ municipalities/care organizations, 30,000+ nurses/carers using it daily, and 99%–99.5% adherence — company-reported, to be verified |
| Regulatory posture | Evondos Anna presented as a CE-marked medical-device service under **MDR**, with **ISO 13485** and **ISO 27001** certifications |
| Key acquisitions | Medido/Vitavanti (2023); VitaCam (2024) |

## 2. What the business actually is

Evondos is not selling a pill dispenser. The defensible business is the **service
system** around the dispenser:

- A locked, tamper-resistant medication-dispensing device in the patient's home.
- Medication pouches ("sachets") prepared by a pharmacy multi-dose-packaging workflow.
- Cloud monitoring through **Evondos Telecare**, with a care-team web portal.
- **Escalation** if medicine is not taken (missed-dose alarms routed to care staff).
- Audit trail and care-team visibility for every dose event.
- Support, training, field operations, logistics, and change management.
- Increasingly, video support and remote patient monitoring (VitaCam).

The device dispenses **only the correct sachet at the correct time**, reminds the
patient with sound, light, and voice, handles missed medication safely (locking the
dose away for a nurse to resolve), and lets authorized professionals manage the system
remotely. The service supports two-factor authentication / SSO and an EU cloud
ownership model for health-data residency.

The moat is the **full combination** — hardware reliability, regulated software,
pharmacy logistics, alerting, clinical safety, municipal procurement, data security,
and operational support — not the dispenser alone.

## 3. Domain scope

**Core scope (modeled here):**
- The in-home **dispensing device** (firmware, dose mechanism, connectivity, on-device
  reminders and confirmation).
- **Pharmacy pouch logistics** — multi-dose packaging orders, roll production, loading,
  and reconciliation against the prescribed schedule.
- **Remote medication management** — schedules, dose events, adherence records, and the
  care-team **telecare portal**.
- **Alarm & escalation** — missed-dose detection, alarm routing, and care-staff
  response workflows.
- **Regulated platform** — identity/access, integrations to care and pharmacy systems,
  device fleet operations, data governance, and audit.
- **Video support & remote monitoring** (VitaCam-style) as an adjacent care channel.

**Adjacent scope (referenced, not fully modeled):** electronic care records (EHR/EPR)
and municipal case-management systems we integrate with; the pharmacy's own dispensing
robots; national e-prescription services.

**Explicitly excluded:** diagnosis and prescribing decisions (a clinician's job), acute
in-hospital medication administration, and the manufacture of the medicines themselves.

**Value exchange:** care organizations and municipalities **pay** a per-device
subscription (device + software + service); **patients/residents** get safe, reliable,
independent medication at home; **nurses/carers** get time back and fewer risky home
visits; **pharmacies** get a recurring multi-dose-packaging channel. Value is repeatable
because it is sold as a managed service with high adherence and measurable home-visit
savings.

## 4. Customers (who the model covers)

1. **Home-care patient / resident** — an elderly or chronically ill person managing
   multiple daily medications at home, wanting independence and safety.
2. **Home-care nurse / carer** — front-line care staff who previously drove to homes to
   hand out pills, now monitoring remotely and responding to alarms.
3. **Care-provider / municipality manager** — the buyer and operator: home-care service
   managers and municipal procurement who own budgets, outcomes, and compliance.
4. **Pharmacy dose-packaging partner** — the pharmacy that fills and supplies the
   multi-dose sachet rolls the device dispenses.

## 5. Vision & strategic spine

**Vision.** Make it normal for people to live safely and independently at home for
longer by taking exactly the medication they need, exactly when they need it — turning
medication from the single most error-prone, labor-intensive part of home care into a
reliable, remotely-managed, evidence-generating service, so care organizations can serve
more people with the staff they have.

**Differentiation.** A regulated, closed-loop *service* (device + pharmacy logistics +
telecare + escalation + support), not a consumer gadget; measurable ~99% adherence and
home-visit reduction; EU health-data residency and MDR/ISO compliance as a procurement
advantage.

**North-star metric:** medication **adherence rate** (share of scheduled doses taken on
time), supported by **home-visits avoided** and **safe days at home**.

**Strategic horizons (sequenced, not repeated):**

- **1 year — Reliable core service.** Rock-solid dispensing, alarm escalation, and the
  telecare portal in existing Nordic markets. Focus: device uptime, adherence, and
  nurse trust. Customer KPI: *Medication Adherence Rate* (north-star), *Missed-Dose
  Alarm Response Time*. Business KPI: *Net Device Retention*.
- **3 years — Scale & integrate.** Expand across Europe (NL, UK), integrate with EHR /
  municipal care systems and e-prescription, and industrialize pharmacy pouch
  logistics. Focus: interoperability and onboarding at scale. Customer KPI: *Home Visits
  Avoided per Device*, *Onboarding Time to First Dose*. Business KPI: *Devices Deployed*
  / *Cost-to-Serve per Device*.
- **5 years — Evidence-led care platform.** Add remote patient monitoring and video
  support (VitaCam), turn the adherence dataset into outcome evidence for payers, and
  extend from dispensing into broader remote medication and vitals management. Focus:
  clinical outcomes and platform breadth. Customer KPI: *Safe Days at Home*, *Adverse
  Medication Events Avoided*. Business KPI: *Revenue per Care Organization* / *Gross
  Margin per Device*.

## 6. Regulatory & data context

Medication management is **health data** and the device is a **medical device**:
- **MDR** medical-device classification; **CE** marking; **ISO 13485** (quality
  management for medical devices) and **ISO 27001** (information security).
- **GDPR** special-category health data, with EU data residency and strict access
  control (2FA/SSO), full audit trail, and retention governed by care regulation.
- Clinical safety: fail-safe dispensing (never dispense the wrong dose; lock away and
  alarm on uncertainty), and traceability of every dose event for care accountability.

These constraints are load-bearing for the domain: they shape the identity/access,
audit, data-governance, and device-safety bricks, and they are a genuine competitive
moat versus consumer adherence gadgets.
