# Openseadragon testing

Working on the following ticket to do with rounding issues:

[2321: When loading some IIIF tilesets, incorrect URL's are being fetched for certain tiles](https://github.com/openseadragon/openseadragon/issues/2321)

OSD examples:

 * [Version 3.1.0](osd-3.1.0.html?image=https://glenrobson.github.io/iiif_stuff/rounding_issue/odd/info.json)
 * [Version 4.0.0](osd-4.0.0.html?image=https://glenrobson.github.io/iiif_stuff/rounding_issue/odd/info.json)
 * [Ruven's fix](osd-ruven.html?image=https://glenrobson.github.io/iiif_stuff/rounding_issue/odd/info.json) [pull request](https://github.com/openseadragon/openseadragon/pull/2337)
   * Tested:
     * Fixture image with no sizes [view](osd-ruven.html?image=https://iiif.io/api/image/3.0/example/reference/28473c77da3deebe4375c3a50572d9d3-laocoon/info.json)
     * Smithsonian image with no sizes [view](osd-ruven.html?image=https://ids.si.edu/ids/iiif/AAA-jacqself00001/info.json)
     * Odd dimensions image [view](osd-ruven.html?image=https://glenrobson.github.io/iiif_stuff/rounding_issue/odd/info.json)
     * Odd v3 fixtures (no sizes) [view](osd-ruven.html?image=https://iiif.io/api/image/3.0/example/reference/84fe52eee7ec9b64f6f35909572ebf36-odd/info.json)
     * Odd v2 fixtures (no sizes) [view](osd-ruven.html?image=https://iiif.io/api/image/2.1/example/reference/84fe52eee7ec9b64f6f35909572ebf36-odd/info.json)
     * Odd v1 fixtures (no sizes) [view](osd-ruven.html?image=https://iiif.io/api/image/1.0/example/reference/84fe52eee7ec9b64f6f35909572ebf36-odd/info.json)
     * Image from Simeon's tiler [view](osd-ruven.html?image=https://glenrobson.github.io/iiif/welsh_book/page001/info.json)
     * Odd image no sizes array [view](osd-ruven.html?image=https://glenrobson.github.io/iiif_stuff/rounding_issue/odd-no-sizes/info.json)