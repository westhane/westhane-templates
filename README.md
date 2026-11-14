# WesthaneTemplates

A TiddlyWiki 5 plugin (`$:/plugins/westhane/WesthaneTemplates`) with custom view templates for a world-building wiki. Tiddlers get a body template chosen by their tags:

| Template | Applies to |
|---|---|
| Character | tag `Character`: Text / Statistics tabs, portrait |
| Place | tag `Place`: Text / Map tabs, parent/child sidebar |
| System | tag `System`: tag-index lists with Minor / Inactive folds |
| Inactive | tag `Inactive`, ahead of all the others |
| Standard | every other content tiddler |

Shared parts: an info box with a portrait, frontmatter (`summarytext` and parent link), backmatter (children with abbreviation pills, then a timeline), and a `<<timeline>>` procedure. Each template has a cascade for the core layout and for [TiddlyFlex](https://github.com/BurningTreeC/TiddlyFlex).

Requires TiddlyWiki 5.3.0 or later. The Place Map tab also needs [flibbles/graph](https://github.com/flibbles/tw5-graph) plus companion tiddlers that aren't in this plugin.

## Install

1. Run `python3 build.py`. It writes `dist/WesthaneTemplates.json`.
2. Drag that file onto your wiki and confirm the import.
3. Save and reload the wiki.

If your wiki holds edited copies of any of the plugin's tiddlers, those copies override the plugin's versions. Delete them to use the plugin's versions.

## Layout

```
plugins/westhane/WesthaneTemplates/
  plugin.info          plugin metadata and version
  readme.tid           shown in the wiki's plugin info
  tiddlers/            one .tid file per tiddler; path follows the title after $:/westhane/
```

`$:/core/ui/TagPickerTagTemplate` (an override of a core tiddler) is in `tiddlers/core-overrides/`.
