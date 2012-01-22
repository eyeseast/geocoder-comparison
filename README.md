Comparing Geocoders
===================

*This is a test project to generate data for a presentation at [NICAR12][n12]. Feel free to borrow any code you find here.*

 [n12]: http://ire.org/events-and-training/event/5/47/ "Own your own map stack: Open source maps from the ground up"

If you're thinking about moving off of Google Maps, by far the most difficult piece of the stack to replicate is its geocoder. Google probably has the most comprehensive database and by far the best address parsing. It also has this problematic line in its terms of service:

> Note: the Geocoding API may only be used in conjunction with a Google map; geocoding results without displaying them on a map is prohibited. For complete details on allowed usage, consult the [Maps API Terms of Service License Restrictions](http://code.google.com/apis/maps/terms.html#section_10_12).

So, no Google map, no Google geocoder.

We do have other options, of course:

 - [Yahoo Placefinder][y]
 - [Bing][b]
 - [Geocoder.us][g]
 - [Nominatum][n] (MapQuest)

 [y]: http://developer.yahoo.com/geo/placefinder/
 [b]: http://msdn.microsoft.com/en-us/library/cc966793.aspx
 [g]: http://geocoder.us/
 [n]: http://wiki.openstreetmap.org/wiki/Nominatim
 
To test these options against Google, I'm using a sample dataset that illustrates some of the known problems working with imperfect input. I've downloaded a list of crime incidents in Washington, DC, in 2011. We'll use the first 500 rows to keep from hitting rate limits.

Every geocoding run will overwrite the results data in a file called `data/<geocoder>.csv` and log the result to `data/results.csv`.