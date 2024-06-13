# SharedProcessors

## PathReporter

This AutoPkg shared processor reports environment paths for current process context. This processor is for troubleshooting purposes only and should not be used in production recipes.

### Input variables

None.

### Output variables

- `path_report`: Contents of `$PATH`.

### Example output

```xml
<key>Output</key>
<dict>
    <key>path_report</key>
    <string>/usr/bin:/bin:/usr/sbin:/sbin</string>
</dict>
```
