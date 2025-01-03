### Task: https://github.com/pbc/devtest (in Python, though)
___

### Notable differences with Django defaults/conventions

1. `project_name/__project_name__` renamed to `project_name/__config__`, as that's what it actually does.

2. Separate files for prod / nonprod `requirements.txt` (likewise for `settings.py`).

3. The views:
* have hierarchical `urls.py` files
  * tidbit: views imported inside those need no `__init__.py` in their respective directories
* delegate all queries to query objects
* delegate all business logic (calculations, crawling, validations) to services

4. The _migrations_ directory contains an optional database seeding tool, usable from command line / Python code.

5. In the absence of forms, Django serializers usually double up as params/data validators (they serialize both ways, so to speak).
The architecture introduces a separate (_services/validations_) module, to achieve greater separation of concerns.
The serializers, now dealing only with model serialization, have been moved to _models/serializers_. Opinions welcome.

6. RSpec-style factories have been added to _tests_ (as a subdirectory).

7. Entity Relationship Diagram:
![erd](https://user-images.githubusercontent.com/13955209/66204521-4e5ca000-e6ab-11e9-9f01-622d1f26d071.png)
