# postalcode

[![Maintainability](https://api.codeclimate.com/v1/badges/489251733058eadc3d34/maintainability)](https://codeclimate.com/github/Elgismarus/postalcode/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/489251733058eadc3d34/test_coverage)](https://codeclimate.com/github/Elgismarus/postalcode/test_coverage)

`postalcode` will validate postal codes from different countries.

Currently supported countries:
- UK

# Include package
_Note_: This package is currently not published as package yet and needs to be pulled from GitHub.

Include the following line in your `requirements.txt`.

```
git+https://github.com/Elgismarus/postalcode@releases/tag/v0.0.1#egg=postalcode
```

# Usage
```
from postalcode import valid_postal_code, Countries

...

# Using enum
validate_postal_code(Countries.UK, 'EC1A 1BB') # => True
# Using capital string
validate_postal_code('UK', 'EC1A 1BB') # => True
# Using lower case string
validate_postal_code('uk', 'EC1A 1BB') # => True
# Unsupported country
validate_postal_code('FR', '15000') # => Country 'FR' not yet supported.

...
```

# Compatibility
| Name | Version |
| --- | --- |
| Pyton | 3.10.4 |

# Contribute easily with VSCode
This project has been built with VSCode in a devcontainer. This allows for development environment consistency across engineers and eases onboarding and setup. This avoids frustration when the environment version changes and the required programming languages and/or dependencies must be installed on the local machine.

1. Open Terminal
1. Clone project
1. `cd` into project root directory
1. Type `code .` (this will open VSCode in current directory)
1. In VSCode, `ctrl+shift+P` and select `Remote container: Rebuild Container`

It usually takes some time the first time to build (download images/container). Once built, you will have all the VSCode plugins required and be able to work on the project. The test explorer is a good tool for debugging and running specific tests visually.

# Testing
_Note: The command below assumed that you are running in the VSCode environment_

Run tests suite through command line:
```
python3 -m unittest discover -s ./tests -p '*_test.py'
```

Run coverage:
```
coverage -m unittest discover -s ./tests -p '*_test.py'
# Report via command line
coverage report -m
# HTML format for visual
coverage html
```

# Changelog
See [CHANGELOG](CHANGELOG.md)
