
# Changelog

### V1.0.2 (21 Feb 2017)

[Possibly fixing issue 1](https://github.com/wiheto/fetchopenfmri/issues/1) by adding zf.close() and tf.close()

Removed try/except command in `get_dataset()` for an if statement. So if download fails for some reason, an error will be raised.

Added possibility for final character of dataset name to be a letter.

created CHANGELOG.md.

### V1.0.1 (20 Feb 2017)

Added an extra "/" when creating `dataDir + '/openfmri'` instead of `Datadir 'openfmri'` to avoid incorrect directory creation

### V1 (20 Feb 2017)

Initial release