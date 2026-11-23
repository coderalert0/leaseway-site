# API well number: verified facts

Research for the guide "How to read an API well number (US oil and gas wells)". Compiled 2026-11-22.

## How this was checked

- **PPDM standard (main source):** *The US Well Number Standard*, 2013 rev 1, published June 19, 2014. PDF: https://dl.ppdm.org/dl/1209
  - Quotes were taken word for word from text extracted from the PDF.
  - Page numbers are the printed page labels. The PDF page number is the printed one plus 1.
- **HTML pages:** these quotes came through a fetch tool that passes pages through a summarizer. Spot-check each one against the live page before you publish.
- **Not consulted:** the New Mexico OCD, North Dakota NDIC, Colorado ECMC, USGS and EIA pages were not fetched, because of the page-fetch budget. No claim below rests on them.
- **Not used:** Wikipedia, Enverus and other vendor blogs.

### Sources

| Tag | Source | URL |
|---|---|---|
| PPDM-STD | PPDM, *The US Well Number Standard* (2013 rev 1) | https://dl.ppdm.org/dl/1209 |
| PPDM-WEB | PPDM US Well Number Standard page | https://ppdm.org/ppdm/PPDM/IEDS/Well_Identification/US_Well_Number_Standard/PPDM/US_Well_Number_Standard.aspx |
| RRC-WRO | Texas RRC, Oil & Gas Well Records Online | https://rrc.texas.gov/oil-and-gas/research-and-statistics/obtaining-commission-records/oil-and-gas-well-records-online |
| RRC-GLOSS | Texas RRC, Glossary for Well Log List | https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/obtaining-commission-records/glossary-for-well-log-list/ |
| OCC | Oklahoma Corporation Commission, Oil & Gas County Table | https://oklahoma.gov/occ/divisions/oil-gas/county-table.html |
| WVDEP | West Virginia DEP, Office of Oil and Gas, API Well Number Explanation | https://dep.wv.gov/oil-and-gas/GI/API_Explanation/Pages/default.aspx |
| SPWLA | SPWLA, API Numbering Guidelines | https://spwla.org/SPWLA/Technical/API_Standards_Information_/API_Numbering_Guidelines.aspx |

SPWLA is the Society of Petrophysicists and Well Log Analysts, a professional society. Its page names no source document, so it is used only as a secondary source.

---

## 1. Structure of the number

**Verdict: mostly correct, with two corrections.**

- **Digits 1–10 are correct as stated:** 2-digit state code, 3-digit county code, 5-digit well code.
- **The current standard no longer uses the names "directional sidetrack code" or "event sequence code."**
  - Digits 11–12 are now called the **wellbore code**.
  - Digits 13–14 are an **optional extension** that the standard does not define.

**Digits 1–12 under the current PPDM standard**

| Positions | PPDM name | Meaning |
|---|---|---|
| 1–2 | State code | State or offshore "pseudo-state" |
| 3–5 | County code | County, parish (Louisiana), USGS quadrangle (Alaska), or offshore pseudo-county |
| 6–10 | Well code | One well origin (surface location), unique within the county |
| 11–12 | Wellbore code | One wellbore, unique within the well |
| 13+ | Extension (optional) | Not defined by the standard; guidance only |

Evidence:

- **Positions:** Figure 1 labels the positions "1-2, 3-5, 6-10, 11-12, 13+". The example given is "31 101 22963 03". (PPDM-STD p. 9)
- **Minimum length:** the US Well Number "is at least a 12-digit number assigned to every wellbore". (PPDM-STD p. 2)
- **Digits 1–12 are the whole standard:** "This Standard reserves and defines only digits 1 – 12." (PPDM-STD p. 10)
- **Digits 11–12 were renamed:** the comparison table reads "Directional sidetrack code | Wellbore code | Name change only." (PPDM-STD p. 26)
- **Wellbore code order means nothing:** "This Standard applies no temporal order or significance to the sequence of the wellbore code." (PPDM-STD p. 10)
  - So the guide should not promise that 00 is the original hole and 01 is the first sidetrack. That is common legacy practice, but the standard does not require it.
- **Digits 13–14 have no single meaning:** the standard "does not attempt a single prescription for positions 13+". (PPDM-STD p. 12)
- **PPDM's guidance for 13–14:**
  - "Use positions 13 – 14 only to describe events that create physical configuration changes". The examples it lists are completions, plugbacks, and recompletions. (PPDM-STD p. 12)
  - "Never use positions 13 – 14 to identify: Wellbores, including laterals; deepenings". (PPDM-STD p. 12)
- **"Event sequence code" is not a PPDM term.** The phrase does not appear in the standard.
  - A secondary description of 13–14 says they "indicate how many operations there have been on a single borehole". (SPWLA)
- **The old name for 11–12, from a secondary source:** "The sidetrack code is the eleventh and twelfth digits of the API number." (SPWLA)

**Is 10 digits the common "API number," with 12 and 14 as the longer forms?**

Yes for real-world usage. Under the current standard, though, 12 digits is the minimum.

- **The original scheme:** "This numbering scheme assigns each well a 10-digit unique identifier." (PPDM-STD p. 7)
- **12-digit forms also existed:** "Some wellbores are also identified with a 12-digit version of the number." (PPDM-STD p. 7)
- **Lengths in practice:** "The number is 10, 12, or 14 digits long." (PPDM-STD p. 8)
- **Many states issue only 10 digits:** "many state regulators assign the D12A Number as 10 digits only". (PPDM-STD p. 8)
- **Meanings vary by state:** "Different meanings are assigned to digits 11 – 14." (PPDM-STD p. 8)
- **A state example:** West Virginia "will use the full 10-digit API for correspondence concerning wells". (WVDEP)

Two more facts the guide could use:

- **Name history:** the old API Well Number is now officially the **US Well Number**.
  - "The US Well Number is the official successor to the API Well Number". (PPDM-WEB)
  - "This Standard Replaces: American Petroleum Institute Bulletin D12A, revised 1979". (PPDM-STD p. 1)
- **County codes follow the surface location.**
  - The standard requires the county code to come from the surface location, even when the hole ends in another county.
  - Some states don't follow this: "a few state regulators assign a county code based on the producing zone location". (PPDM-STD p. 8)

## 2. State codes

**Verdict: all 10 are confirmed.**

| State | Code |
|---|---|
| California | 04 |
| Colorado | 05 |
| Kansas | 15 |
| Montana | 25 |
| New Mexico | 30 |
| North Dakota | 33 |
| Ohio | 34 |
| Oklahoma | 35 |
| Texas | 42 |
| West Virginia | 47 |

These come from the "State Codes for the United States" table. (PPDM-STD p. 16)

- **These are not FIPS codes.** For example, FIPS uses 48 for Texas, where the API code is 42.
  - "These state codes were originally developed as early as 1952 by IBM". (PPDM-STD p. 16)
  - They "are not the same as codes from other standards organizations", including FIPS. (PPDM-STD p. 16)
- **West Virginia's own page agrees:** "47 is the state code for West Virginia." (WVDEP)
- **Offshore federal waters have pseudo-state codes:**

  | Area | Code |
  |---|---|
  | Alaska Offshore | 55 |
  | Pacific Coast Offshore | 56 |
  | Northern Gulf of Mexico | 60 |
  | Atlantic Coast Offshore | 61 |

  (PPDM-STD p. 16)

## 3. County codes: odd numbers, alphabetical, FIPS-style

**Verdict: true as a general pattern. False as a rule for all states. "Same as FIPS" is not guaranteed.**

Where it holds:

- **West Virginia:** "County codes are odd numbers, beginning with 001 (Barbour) continuing, alphabetically, to 109 (Wyoming)." (WVDEP)
- **Oklahoma:** the OCC table runs 001 Adair, 003 Alfalfa … 151 Woods, 153 Woodward.
  - All 77 codes are odd.
  - The order is alphabetical with one quirk: Major (093) comes after McIntosh (091). (OCC)
- **Secondary summary:** "all county codes are odd numbers except for certain counties in Arizona and New Mexico". (SPWLA)
  - The same page names Kern County, California, as a third exception.

Where it does not hold:

- **Kern County, California has two codes, one of them even.**
  - "this was done in about 1992 for Kern County, CA (county codes 029, 030)". (PPDM-STD p. 11)
  - The second code was added because Kern ran out of 5-digit well codes.
- **Some states added codes after 1979.** Codes match the 1979 bulletin "except for codes created since then by Arizona, California, Colorado, and New Mexico". (PPDM-STD p. 11)
- **Some "county" codes are not counties.** The code may be "an onshore county, parish (Louisiana), or USGS quadrangle (Alaska) or a pseudo-county". (PPDM-STD p. 10)
  - "County codes are also used to designate offshore areas for both state and federal waters." (SPWLA)
- **They are not necessarily FIPS.** "The county codes are not necessarily the same as codes from other standards organizations", and the standard names FIPS among them. (PPDM-STD p. 18)
  - Many states' codes do look like FIPS county codes. This research did not compare them state by state.
  - The guide should say "often match FIPS," not "are FIPS."
- **Not verified (search snippets only, pages not fetched):**
  - A Kentucky Geological Survey FAQ says Kentucky uses FIPS county codes.
  - A claim that Texas codes run from Anderson (001) to Zavala (507).

## 4. Texas specifics

**Verdict: confirmed.** The RRC normally shows the 8-digit form (3-digit county + 5-digit well number) without the 42. Its Well Records Online search tells users to leave the 42 out.

The RRC describes the number two different ways on its own pages:

- **Well Records Online page (10 digits, 42 hidden):**
  - "It consists of 10 digits." (RRC-WRO)
  - "The state code for Texas is 42" and it "is not generally displayed on Railroad Commission documents". (RRC-WRO)
- **Glossary for Well Log List (8 digits):**
  - "It consists of 8 digits." (RRC-GLOSS)
  - "The fIrst 3 digits are the county code" (sic). (RRC-GLOSS)
  - "the last 5 digits are the unique number assigned to identify the wellbore". (RRC-GLOSS)

**Searching:** "When searching for Oil and Gas Records, do NOT use the state code 42". (RRC-WRO)

- The RRC's own example format is 8 digits: "API#357-80808". (RRC-WRO)
- **Scope of this check:** confirmed for Well Records Online only. Other RRC tools, such as the Production Data Query and the GIS Viewer, were not checked.

**Useful for the guide:** "there may be multiple API numbers associated with one RRC oil lease number". (RRC-WRO)

- The same page says each gas lease has only one well, so each gas lease number has only one API number.

**Oklahoma shows the same habit:** "The first field of the OCC API Number is the County Code." (OCC)

- That implies the OCC also drops the 35 in its databases. This is inferred from that one sentence and was not checked further.

## 5. When it was introduced, and who assigns numbers today

**Introduced in 1966.**

- It is "the API Well Number identifier introduced in 1966 by the American Petroleum Institute". (PPDM-STD p. 5)
- Bulletin D12A was revised over time; "the latest published version appeared in 1979". (PPDM-STD p. 7)
- **API handed the standard to PPDM in 2010:** "In 2010, the API transferred custody of this Standard". (PPDM-STD p. 2)
- PPDM's replacement is the 2013 US Well Number Standard (revision 1 published June 2014). (PPDM-STD p. 1)

**Caution: older wells were numbered after the fact.**

- West Virginia says every well "permitted in West Virginia since 1929 has been issued an API number". (WVDEP)
- The bulletin itself set aside numbers "for the retroactive identification of historical wells". (PPDM-STD p. 11)
- So a pre-1966 well with an API number is normal. It does not mean the system is older than 1966.

**Who assigns numbers: the regulator, in general the state oil and gas agency.**

- The assigner is "the governmental or jurisdictional agency, e.g. regulator, that assigns US Well Numbers". (PPDM-STD p. 5)
- Numbers are "assigned by the Primary Assigning Authority (in general the regulatory agency)". (PPDM-STD p. 13)
- **Timing:** a number is "usually assigned when the application is received or the drilling permit is issued". (PPDM-STD p. 13)
- **PPDM's role:** PPDM maintains the state code list. County and well codes come from the assigning authority.
- **Federal offshore:** in federal waters the assigning authority is federal, not a state. That is implied by the pseudo-state codes; no BSEE page was fetched.

## 6. Why one well can have several numbers, and whether the first 10 digits stay the same

**Verdict: confirmed, with one exception.** The first 10 digits stay the same for every wellbore drilled from the same surface location. A new surface location (for example, a skidded rig) gets a new well code, so the first 10 digits change.

**Same surface location: the first 10 digits stay the same.**

- "All Wellbores sharing the same Well Origin must have the same digits 1 – 10". (PPDM-STD p. 10)
- Figure 4 shows each wellbore with a different wellbore code but "the same first 10 digits". (PPDM-STD p. 20)

**Each new wellbore gets its own wellbore code (digits 11–12):**

- "a borehole from the side of an existing Wellbore", meaning a sidetrack. (PPDM-STD p. 12)
- Bypasses and pilot holes. (PPDM-STD pp. 14, 20)
- Deepenings, though each regulator decides what counts as a deepening: "this Standard allows each Authority to define the criteria". (PPDM-STD p. 13)

**Re-entry: same first 10 digits.** If an abandoned well is re-entered and a new wellbore is drilled, "the new US Well Number retains digits 1 – 10 of the original Well". (PPDM-STD p. 13)

**Skidded rig: new first 10 digits.** If a hole is junked and the rig is moved to spud nearby, "a new US Well Number (with a unique well code) must be assigned". (PPDM-STD p. 13)

**Non-drilling work: optional 13–14 extension.** Work such as completions, plugbacks or recompletions may be tracked in the 13–14 extension instead. (PPDM-STD p. 12)

**Numbers are permanent:** "A Number, once assigned, should not be reassigned to a different Well or Wellbore." (PPDM-STD p. 13)

**Caveat for the guide:** many states never issue 11–12 at all.

- Many states "assign the D12A Number as 10 digits only". (PPDM-STD p. 8)
- In those states, a sidetrack may not get its own published number.
- Some states have used 13–14, or even 11–14, to identify wellbores, which the current standard forbids. (PPDM-STD p. 12)
