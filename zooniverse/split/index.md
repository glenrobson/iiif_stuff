# Zooniverse Testing - annoPage per canvas

I created [this script](https://github.com/glenrobson/iiif_stuff/blob/master/zooniverse/split/split.py) to split the annotations from:

[https://zooniverse.github.io/iiif-annotations/annotations/titles/0.json](https://zooniverse.github.io/iiif-annotations/annotations/titles/0.json)

into one file per IIIF canvas and then linked the Manifest [here](manifest.json) to all of the annotation pages. Looking at the edited manifest in Mirador:

<div id="mirador" style="width: 100%; height: calc(100vh - 3px); position: relative;"></div>
<script type='text/javascript' src='https://unpkg.com/mirador@latest/dist/mirador.min.js'></script>
<script type="text/javascript">
      var miradorInstance = Mirador.viewer({
        id: 'mirador',
        windows: [
            {
                manifestId: 'https://glenrobson.github.io/iiif_stuff/zooniverse/split/manifest.json',
                sideBarPanel: 'annotations',
                sideBarOpen: true
            }
        ],
      });
</script>      

The annotation pages generated are:

 * [annoPage-0.json](annoPage-0.json)
 * [annoPage-1.json](annoPage-1.json)
 * [annoPage-2.json](annoPage-2.json)
 * [annoPage-3.json](annoPage-3.json)
 * [annoPage-4.json](annoPage-4.json)
 * [annoPage-5.json](annoPage-5.json)
 * [annoPage-6.json](annoPage-6.json)
 * [annoPage-7.json](annoPage-7.json)
 * [annoPage-8.json](annoPage-8.json)
 * [annoPage-9.json](annoPage-9.json)
 * [annoPage-10.json](annoPage-10.json)
 * [annoPage-11.json](annoPage-11.json)
 * [annoPage-12.json](annoPage-12.json)
 * [annoPage-13.json](annoPage-13.json)
 * [annoPage-14.json](annoPage-14.json)
 * [annoPage-15.json](annoPage-15.json)
 * [annoPage-16.json](annoPage-16.json)
 * [annoPage-17.json](annoPage-17.json)
 * [annoPage-18.json](annoPage-18.json)
 * [annoPage-19.json](annoPage-19.json)
 * [annoPage-20.json](annoPage-20.json)
 * [annoPage-21.json](annoPage-21.json)
 * [annoPage-368.json](annoPage-368.json)

