<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *AI/ML models.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,ml-model,abtf-ssd-pytorch*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,ml-model,abtf-ssd-pytorch[,variations] `

2. `cmr "get ml-model abtf-ssd-pytorch[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,abtf-ssd-pytorch'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="get,ml-model,abtf-ssd-pytorch"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,abtf-ssd-pytorch) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model abtf-ssd-pytorch[ variations]" `

___
### Customization


#### Variations

  * Group "**epoch**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_e01`
      - Environment variables:
        - *CM_ML_MODEL_URL*: `https://www.dropbox.com/scl/fi/7nqt5z8gplgeaveo933eo/SSD_e1.pth?rlkey=7lyb4qs2hzg491bfprwcuvx54&dl=0`
        - *CM_ML_MODEL_FILENAME*: `SSD_e1.pth`
        - *CM_ML_MODEL_CHECKSUM*: `31d177228308bbe43917c912b01c2d67`
      - Workflow:
    * **`_e65`** (default)
      - Environment variables:
        - *CM_ML_MODEL_URL*: `https://www.dropbox.com/scl/fi/wkegl2qxvm8cefbqq00o3/SSD_e65.pth?rlkey=ez26jafjdcly665npl6pdqxl8&dl=0`
        - *CM_ML_MODEL_FILENAME*: `SSD_e65.pth`
        - *CM_ML_MODEL_CHECKSUM*: `f769eb0321ac7fc1c16f982db6131d2f`
      - Workflow:

    </details>


#### Default variations

`_e65`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * download,file,_wget
       * CM names: `--adr.['get-ml-model']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/_cm.json)
</details>

___
### Script output
`cmr "get ml-model abtf-ssd-pytorch[,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)