# How to read an API well number

> An API well number (now officially the US Well Number) starts with 10 digits that identify a well's surface location: a 2-digit state code (Texas is 42), a 3-digit county code and a 5-digit well code. Digits 11–12, where a state issues them, identify one wellbore from that surface location, such as a sidetrack. Texas usually shows only 8 digits, the county and well codes, without the 42.

Source page: https://coderalert0.github.io/leaseway-site/how-to-read-an-api-well-number.html
Checked against its sources on November 22, 2026. Published by Leaseway, an oil well map for iPhone and iPad.

## The digits

The numbering scheme was introduced by the American Petroleum Institute in 1966 (API Bulletin D12A, last revised in 1979). In 2010 the API handed it to the Professional Petroleum Data Management Association (PPDM), whose 2013 *US Well Number Standard* replaced the bulletin. The number is still widely called the API number.

| Digits | Name | Meaning |
|---|---|---|
| 1–2 | State code | The state, or an offshore area |
| 3–5 | County code | The county (parish in Louisiana) of the well's surface location |
| 6–10 | Well code | One surface location, unique within the county |
| 11–12 | Wellbore code | One wellbore drilled from that surface location |
| 13–14 | Extension (optional) | Not defined by the standard; some states use it for completions or other work on a wellbore |

So `42-389-31203` is a Texas (42) well in Reeves County (389) with well code 31203. In practice API numbers are written with 10, 12 or 14 digits, often with dashes. Many state regulators issue only the first 10 digits.

The old names for the last digits, "directional sidetrack code" for 11–12 and "event sequence code" for 13–14, still show up on older documents. The current standard calls 11–12 the wellbore code and doesn't number its wellbores in any particular order, so `00` isn't guaranteed to be the original hole.

## State codes

The two-digit state codes are not the FIPS state codes (FIPS uses 48 for Texas). They go back to codes IBM drew up in the 1950s.

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

Offshore federal waters have their own codes, such as 60 for the northern Gulf of Mexico.

## County codes

County codes are usually odd numbers in alphabetical order within a state: West Virginia runs from 001 (Barbour) to 109 (Wyoming), and Oklahoma from 001 (Adair) to 153 (Woodward). Many match the counties' FIPS codes, but the standard doesn't promise that, and there are exceptions: Kern County, California has two codes (029 and 030) because it ran out of well codes, and Arizona, California, Colorado and New Mexico have added codes since 1979. The county code comes from where the well starts at the surface, even if the hole ends in another county, though a few regulators have used the producing zone's county instead.

## Texas shows 8 digits

The Railroad Commission of Texas generally leaves off the state code 42 and shows the 3-digit county code and the 5-digit well code, like `357-80808`. Its Well Records Online search says not to use the 42 at all. So when someone gives you an 8-digit Texas number, it's the same well as the 10-digit number with 42 in front.

Leaseway accepts all of these: 10, 12 or 14 digits, with or without dashes, the 8-digit Texas form, or just the last five digits, the well code, with results nearest you first.

## One well, several numbers

Every wellbore drilled from the same surface location keeps the same first 10 digits. A sidetrack, bypass, pilot hole or (where the regulator says so) a deepening gets a new wellbore code in digits 11–12, and a new wellbore drilled when an abandoned well is re-entered keeps the original first 10 digits. If a rig is skidded to a new spot after a junked hole, the new hole gets a new well code, so its first 10 digits change. Once assigned, a number is never reused for a different well.

The regulator assigns the numbers, usually when the drilling application is received or the permit is issued. Wells drilled before 1966 can still have API numbers: states numbered historical wells after the fact (West Virginia, for one, has numbered every well it permitted since 1929).

## Frequently asked questions

### What does the API number of an oil well mean?

It identifies the well's surface location: the first two digits are the state, the next three the county, and the next five the well. Two more digits, where the state issues them, pick out one wellbore drilled from there.

### What is Texas's API state code?

42. The Railroad Commission of Texas usually doesn't display it, so Texas numbers often appear as 8 digits, county plus well.

### Is the API number the same as the permit number or lease number?

No. A drilling permit and a lease have their own numbers. In Texas one oil lease can include several wells, each with its own API number.

## Sources

- [PPDM: The US Well Number Standard (2013, revision 1)](https://dl.ppdm.org/dl/1209)
- [PPDM: US Well Number Standard](https://ppdm.org/ppdm/PPDM/IEDS/Well_Identification/US_Well_Number_Standard/PPDM/US_Well_Number_Standard.aspx)
- [Railroad Commission of Texas: Oil and Gas Well Records Online](https://rrc.texas.gov/oil-and-gas/research-and-statistics/obtaining-commission-records/oil-and-gas-well-records-online)
- [Railroad Commission of Texas: Glossary for Well Log List](https://www.rrc.texas.gov/oil-and-gas/research-and-statistics/obtaining-commission-records/glossary-for-well-log-list/)
- [Oklahoma Corporation Commission: Oil and Gas County Table](https://oklahoma.gov/occ/divisions/oil-gas/county-table.html)
- [West Virginia DEP Office of Oil and Gas: API Well Number Explanation](https://dep.wv.gov/oil-and-gas/GI/API_Explanation/Pages/default.aspx)
