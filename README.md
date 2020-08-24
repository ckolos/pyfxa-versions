* pyfxa-versions

Simple script to query the __version__ endpoint on all the fxa porperties for a given env

When working properly, you should get output similar to this:

```
https://payments-stage.fxa.nonprod.cloudops.mozgcp.net/__version__
{
  "commit": "bd5b68e957203be6760dcfe41860965347d5ba1a",
  "l10n": "47b76a50cf78c2d77f44f7258d2d0854f404ba1b",
  "source": "https://github.com/mozilla/fxa",
  "version": "1.185.1"
}
.
.
.
https://eventbroker-stage.fxa.nonprod.cloudops.mozgcp.net/__version__
{
  "commit": "bd5b68e957203be6760dcfe41860965347d5ba1a",
  "source": "https://github.com/mozilla/fxa",
  "version": "1.185.1"
}
```

The script takes the following arguments:

 `-c / --config - Full path to configuration file (json)`
 `-e / --env    - Which env to check (dev/stage/prod/thingie/etc)`


