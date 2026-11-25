# NAD27 and NAD83 well coordinates

> The same latitude and longitude mark different spots on the ground in NAD27 and NAD83, usually tens of meters apart and more in places. GPS and phone maps use WGS 84, which is close to NAD83, so NAD27 well coordinates typed into a phone land off the pad unless they are converted. The shift varies from place to place: there is no one number to add.

Source page: https://coderalert0.github.io/leaseway-site/nad27-nad83-well-coordinates.html
Checked against its sources on November 22, 2026. Published by Leaseway, an oil well map for iPhone and iPad.

## How far off

NOAA's National Geodetic Survey says the shifts between datums "are not uniform across the United States" and that no single value converts one to the other. Its NADCON guide works an example where the shift is 24 meters. You will also see about 200 meters: a USGS FAQ gives 210 as a general figure, and an Esri note gives 200 for the y coordinate in UTM or state plane, where part of the difference is the coordinate grid itself.

Building Leaseway's well data we measured it, comparing NAD27 positions with the agencies' own NAD83 ones for the same wells. Unconverted, they were a median 38 meters apart. Converted, they were within about 5 meters.

Thirty-eight meters is the difference between standing at the wellhead and standing across the lease road.

## Which datum a number is in

| Where it came from | Datum |
|---|---|
| A phone, or GPS set to its default | WGS 84, close to NAD83 |
| Railroad Commission of Texas digital map data | NAD27, according to the RRC's FAQ |
| Kansas Geological Survey | NAD27 and NAD83 both published |
| An older plat, permit or paper file | Often NAD27; look for the note near the seal or the title block |

Plats and permits usually name the datum near the coordinates. If one doesn't, the year is a hint and not an answer: check it against something you can see.

## How to tell in the field

1. Put the coordinates into a map with satellite imagery.
2. Find the pad. If every well on the lease sits the same distance and direction from its pad, it is a datum difference, not a bad record.
3. Convert with NOAA's [NCAT](https://geodesy.noaa.gov/NCAT/), which replaced NADCON, and look again.
4. One well off on its own is more likely a typing error, or a bottom-hole location.

## Surface or bottom hole

A horizontal well's bottom hole can be a mile or more from its surface location. Driving directions need the surface hole. If the coordinates land in an empty field with a pad a mile away, you probably have the bottom hole.

## In Leaseway

Leaseway shows surface locations in NAD83. Positions that a state publishes in NAD27 are converted when the state's pack is built, with one set of parameters for the lower 48; against the agencies' own NAD83 values the result was within 5 meters.

## Frequently asked questions

### Is WGS 84 the same as NAD83?

Not exactly, but they are within a couple of meters of each other in the lower 48, which doesn't matter for finding a wellhead.

### Can I add a fixed offset to convert NAD27 to NAD83?

No. The shift changes from place to place. Use NOAA's NCAT or software that has its grids.

### Why are all the wells on my map shifted the same way?

That pattern is what a datum difference looks like: NAD27 positions drawn as if they were NAD83 or WGS 84.

## Sources

- [NOAA National Geodetic Survey: NADCON](https://webarchive.library.unt.edu/web/20130215202018/http://www.ngs.noaa.gov/TOOLS/Nadcon/Nadcon.shtml)
- [NOAA National Geodetic Survey: NADCON (Professional Surveyor article)](https://nweb.ngs.noaa.gov/TOOLS/Professional_Surveyor_Articles/NADCON.pdf)
- [USGS: How large is the NAD 27 to NAD 83 shift?](https://www.usgs.gov/faqs/how-large-north-american-datum-nad-27-nad-83-shift)
- [Railroad Commission of Texas: Digital Map Information and GIS Data FAQ](https://rrc.texas.gov/about-us/faqs/general-faqs/digital-map-information-gis-data)
- [Esri: Transforming coverages between NAD27 and NAD83](https://resources.arcgis.com/en/help/main/10.2/0013/001300000052000000.htm)
- The 38 and 5 meter figures: our own comparison with Kansas and Texas agency data, November 2026
