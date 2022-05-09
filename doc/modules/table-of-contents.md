# Table of Contents
You can display a table of contents, showing a page tree of your confluence documentation.

## Syntax
```markdown
    ```TOC
    [options]
    ```
```
or
```markdown
    ```table-of-contents
    [options]
    ```
```

## Options
You can specify options for the page tree between the code blocks for the macro.

`[option]=[value]`

All options are optional, and can be left out.

### `root`
This option specifies the root of the page tree. The root can either be the name of a page under the page containing the tree, or you can use '@self' or '@home' to reference the page containing the tree, or the home page, respectivly.

Type = String (Not that ' and " will be considered as part of the name, and should therefore not encapsulate the string)
Default = @self

### `search_bar`
This options specifies if the page tree should feature a search bar at to top of the tree.

Type = boolean
Default = false

### `start-depth`
Any positive number representing the level to which child pages are shown when the page tree is first displayed.

Type = integer
Default = 1

## Examples
```markdown
    ```TOC
    root=Home Page
    start-depth=3
    search_bar=true
    ```
```

You can also create a tree with no specified options like so:

```markdown
    ```TOC
    ```
```