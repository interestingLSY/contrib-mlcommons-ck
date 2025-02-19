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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *AI/ML models.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation[,variations] [--input_flags]`

2. `cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation'
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

```cmr "cm gui" --script="get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_debug`
      - Environment variables:
        - *CM_ML_MODEL_DEBUG*: `yes`
      - Workflow:
    * `_onnx,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8025`
        - *CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb00_40M.onnx.tar`
        - *CM_UNTAR*: `yes`
        - *CM_ML_MODEL_FILE*: `tb00_40M.onnx`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `40000000`
      - Workflow:
    * `_onnx,fp32,debug`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8107`
        - *CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb0875_10M.onnx.tar`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `10000000`
        - *CM_UNTAR*: `yes`
        - *CM_ML_MODEL_FILE*: `tb0875_10M.onnx`
      - Workflow:
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8025`
        - *CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb00_40M.pt`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `40000000`
        - *CM_DOWNLOAD_CHECKSUM*: `2d49a5288cddb37c3c64860a06d79bb9`
      - Workflow:
    * `_pytorch,fp32,debug`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8107`
        - *CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb0875_10M.pt`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `10000000`
      - Workflow:
    * `_pytorch,fp32,weight_sharded`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8025`
        - *CM_PACKAGE_URL*: `https://cloud.mlcommons.org/index.php/s/XzfSeLgW8FYfR3S/download`
        - *CM_DAE_EXTRACT_DOWNLOADED*: `yes`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `40000000`
        - *CM_DOWNLOAD_FILENAME*: `download`
        - *CM_ML_MODEL_FILE*: `model_weights`
        - *CM_EXTRACT_UNZIP*: `yes`
        - *CM_TMP_MODEL_ADDITIONAL_NAME*: ``
        - *CM_DOWNLOAD_CHECKSUM*: ``
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_onnx`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
      - Workflow:
    * **`_pytorch`** (default)
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
        - *CM_TMP_MODEL_ADDITIONAL_NAME*: `dlrm_terabyte.pytorch`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
      - Workflow:

    </details>


  * Group "**type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_weight_sharded`** (default)
      - Environment variables:
        - *CM_DLRM_MULTIHOT_MODEL*: `yes`
      - Workflow:

    </details>


#### Default variations

`_fp32,_pytorch,_weight_sharded`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DOWNLOAD_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
  1. Run "preprocess" function from customize.py
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)***
     * download-and-extract,_wget
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
</details>

___
### Script output
`cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)