# cookiecutter-R-package #

[![Build Status](https://travis-ci.com/gjcooper/cookiecutter-R-analysis-pkg.svg?branch=main)](https://travis-ci.com/gjcooper/cookiecutter-R-analysis-pkg)

Cookiecutter template for an R package. See https://github.com/audreyr/cookiecutter.

* Adds package-name.R with boilerplate for [Roxygen2](https://cran.r-project.org/package=roxygen2)
* Adds basic .travis.yml file for [Travis-CI](http://docs.travis-ci.com/user/languages/r/) builds
* Includes .gitignore and .Rbuildignore to cover most use cases.
* Includes Rmarkdown vignette example with necessary DESCRIPTION file.
* Adds basic [testthat](https://cran.r-project.org/package=testthat) framework.
* Includes other basic R boilerplate code.

# Usage

Generate an R package project:

    `cookiecutter https://github.com/gjcooper/cookiecutter-R-analysis-pkg.git`

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
