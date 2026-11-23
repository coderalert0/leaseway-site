# Oil and gas well locations by state: where the free public data comes from

> Every oil-producing state's regulator publishes its wells' locations for free, usually as a public map service or a downloadable file. Texas has the Railroad Commission's GIS well layer plus its well and permit files, New Mexico the OCD's well map service, Oklahoma the OCC's RBDMS well file, North Dakota the NDIC's daily well shapefile, and Colorado the ECMC's daily well-spot shapefile. Locations are what operators filed, so they can be off, and some states' coordinates use the older NAD27 datum.

Source page: https://coderalert0.github.io/leaseway-site/oil-gas-well-data-by-state.html
Checked against its sources on November 22, 2026. Published by Leaseway, an oil well map for iPhone and iPad.

## The short list

These are the sources Leaseway rebuilds its well maps from every night, checked on November 22, 2026. Each one is the state regulator's own public data; none needs an account.

| State | Agency | What's published | How often |
|---|---|---|---|
| Texas | Railroad Commission of Texas (RRC) | Public GIS "Well Locations" layer (1.4 million points); statewide well records by county; drilling permits with coordinates | Map layer live; well records twice a week; permits nightly and monthly |
| New Mexico | Oil Conservation Division (OCD), EMNRD | Public "Oil and Gas Wells" map service | Live (the OCD's permitting database) |
| Oklahoma | Oklahoma Corporation Commission (OCC) | RBDMS well data file (CSV) | Nightly |
| North Dakota | NDIC Department of Mineral Resources, Oil and Gas Division | Well shapefile | Daily |
| Colorado | Energy & Carbon Management Commission (ECMC, formerly COGCC) | "Well Spots (APIs)" shapefile, all wells regardless of status | Daily |
| Kansas | Kansas Geological Survey (KGS), with Kansas Corporation Commission status | KGS master well list | Every week or two |
| California | Geologic Energy Management Division (CalGEM) | WellSTAR "Wells" map service | Live |
| Ohio | ODNR Division of Oil and Gas Resources Management | Public oil and gas wells map service | Live |
| Montana | Board of Oil and Gas Conservation | DataMiner map service | Live |
| West Virginia | WVDEP Office of Oil and Gas | TAGIS oil and gas wells map service | Live |

## Texas: three files make one well

Texas splits a well across several RRC products, joined by the well's 8-digit API number (county code plus unique number, without Texas's state code 42):

- **Where it is:** the RRC's public GIS service has a "Well Locations" layer with each well's API, symbol (oil, gas, plugged, permitted and so on) and NAD83 latitude and longitude.
- **What it's called:** the RRC's "Statewide API Data" files (one per county, described in the RRC's Well API manual) hold the lease name, well number, operator and field. A well can point to another API (its "refer to" API), and the manual says to follow it.
- **What's new:** the "Drilling Permit Master and Trailer" files list approved permits with their surface location, so a well can show up on the map as soon as it's permitted, before it appears in the GIS layer.

## New Mexico, California, Ohio, Montana, West Virginia: live map services

These states publish their wells through public ArcGIS map services, the same ones behind their own web maps. A service can be queried for every well with its API number, name, operator, status and coordinates. New Mexico's OCD service includes plugged and cancelled wells and new permits; California's WellSTAR layer is documented in CalGEM's GIS ReadMe, which states its coordinates are NAD83.

## Oklahoma, North Dakota, Colorado, Kansas: downloadable files

- **Oklahoma:** the OCC publishes the RBDMS well file as a CSV with a data dictionary.
- **North Dakota:** the NDIC's Oil and Gas Division posts a well shapefile that is refreshed daily.
- **Colorado:** the ECMC's "Well Spots (APIs)" shapefile covers all wells, regardless of status, and is refreshed daily.
- **Kansas:** the KGS master list of oil and gas wells comes as a zipped text file. Its metadata says the latitudes use the NAD 1927 datum, which can put a point tens of meters from where NAD83 or WGS84 would; convert it before you compare it with a phone's GPS.

## Why a location can be wrong

Every one of these is what an operator filed, sometimes decades ago and sometimes from a survey plat, and the agencies publish it as filed. Old wells can be noticeably off; a few have no coordinates at all; a brand-new permit can take a day or more to reach the files. Plugged and cancelled wells stay in most files. Use the location to get close, then the lease sign and the operator's directions.

## Frequently asked questions

### Is oil and gas well location data public?

Yes. Each state's oil and gas regulator publishes its wells' locations, operators and statuses as public records, free to download or query, with no account.

### Which states publish their wells as a live map service?

Of the ten above, New Mexico, California, Ohio, Montana and West Virginia publish their wells as live public map services, and Texas publishes its well locations that way too. Oklahoma, North Dakota, Colorado and Kansas publish downloadable files.

### Why don't the coordinates line up with my GPS?

Some states store the older NAD27 datum (Kansas says so in its metadata), while phones use WGS84. The difference can be tens of meters. The filed location itself can also be off, especially for old wells.

## Sources

- [Railroad Commission of Texas: public GIS map services](https://gis.rrc.texas.gov/server/rest/services/rrc_public/RRC_Public_Viewer_Srvs/MapServer)
- [Railroad Commission of Texas: Well API manual (Statewide API Data)](https://www.rrc.texas.gov/media/bkyl5qvx/well-api-manual.pdf)
- [Railroad Commission of Texas: Drilling Permit Master and Trailer layout (OGA049M)](https://www.rrc.texas.gov/media/zgccdjpi/drillingpermitmasterpluslatitudeslongitudes_oga049m_july1.pdf)
- [New Mexico OCD: Oil and Gas Wells map service](https://gis.emnrd.nm.gov/arcgis/rest/services/OCDView/Wells_Public/MapServer/0)
- [Oklahoma Corporation Commission: Oil and Gas data files](https://oklahoma.gov/occ/divisions/oil-gas/oil-gas-data.html)
- [North Dakota Oil and Gas Division](https://www.dmr.nd.gov/oilgas/)
- [Colorado ECMC: data downloads](https://ecmc.colorado.gov/)
- [Kansas Geological Survey: oil and gas well database](https://www.kgs.ku.edu/PRS/petroDB.html)
- [Kansas Geological Survey: well data metadata (datum)](https://www.kgs.ku.edu/Magellan/Qualified/ogwell_fgdc.html)
- [CalGEM: GIS metadata ReadMe](https://www.conservation.ca.gov/calgem/maps/Documents/GIS-metadata-ReadMe.pdf)
- [Ohio DNR: Oil and Gas Wells map service](https://gis.ohiodnr.gov/arcgis/rest/services/DOG_Services/Oilgas_Wells_public/MapServer/0)
- [Montana Board of Oil and Gas Conservation](https://bogapps.dnrc.mt.gov/)
- [West Virginia DEP Office of Oil and Gas](https://dep.wv.gov/oil-and-gas/)
