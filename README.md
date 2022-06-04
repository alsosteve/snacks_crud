# snacks_crud
# Python 401d1818
## Labs 28: Django CRUD and Forms
### Authors: Steve Ngo
​
## Overview
Add full Creating, Reading, Updating and Deleting, CRUD, functionality to a Django project.
​
## Implementation Notes:
Follow the demo [demo repo](https://github.com/codefellows/seattle-python-401d18/tree/main/class-28)

## Feature Tasks and Requirements
* Create `snacks_crud_project` Django project
* Create `snacks` app
* Create `Snack` model
  * title field
  * purchaser field
  * description field
  * Register model with admin
* Create `SnackListView` that extends appropriate generic view
  * associated url path is an empty string
* Create `SnackDetailView` that extends appropriate generic view
  * associated url path is `<int:pk>/`
* Create `SnackCreateView` that extends appropriate generic view
  * associated url path is `create/`
* Create `SnackUpdateView` that extends appropriate generic view
  * associated url path is `<int:pk>/update/`
* Create `SnackDeleteView` that extends appropriate generic view
  * associated url path is `<int:pk>/delete/`
* Add urls to support all views, with appropriate names
* Add templates to support all views
* Add navigation links in appropriate locations to access all pages
* Make all necessary changes to project level files for project to run
  * In other words, make it work

## User Acceptance Tests
* Test all Views
* Test Model
  * string representation
  * all fields

## Configuration
Create a virtual environment inside `snacks_crud`.

## Stretch Goals
* add multiple models
* use an alternate test runner
* add more advanced fields to models, e.g. created time stamp
* add styling