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

## Setup for Google Cloud Instances
```
sudo snap install google-cloud-cli --classic
gcloud auth application-default login
```

The above two commands will install google-cloud-cli and authorizes the user to access it. Once done, you can start creating gcp instance using CM commands like below. To destroy an instance just repeat the same command with `--destroy` option.

```
cm run script --tags=run,terraform,_gcp,_gcp_project.mlperf-inference-tests --cminit
```
Here, `mlperf-inference-tests` is the name of the google project as created in [Google cloud console](https://console.cloud.google.com/apis/dashboard)


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *Cloud automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,terraform*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=run,terraform[,variations] [--input_flags]`

2. `cmr "run terraform[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,terraform'
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

```cmr "cm gui" --script="run,terraform"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,terraform) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run terraform[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_amazon-linux-2-kernel.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE_OS*: `amazon-linux-2-kernel.#`
      - Workflow:
    * `_graviton`
      - Environment variables:
        - *CM_TERRAFORM_AWS_GRAVITON_INSTANCE*: `yes`
      - Workflow:
    * `_inferentia`
      - Environment variables:
        - *CM_TERRAFORM_AWS_INFERENTIA_INSTANCE*: `yes`
      - Workflow:
    * `_inferentia,amazon-linux-2-kernel.510`
      - Workflow:
    * `_rhel.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE_OS*: `rhel.#`
      - Workflow:
    * `_ubuntu.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE_OS*: `ubuntu.#`
      - Workflow:

    </details>


  * Group "**aws-instance-image**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_amazon-linux-2-kernel.510,arm64,us-west-2`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `ami-0f1a5f5ada0e7da53`
      - Workflow:
    * `_aws_instance_image.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `#`
      - Workflow:
    * `_aws_instance_image.ami-0735c191cf914754d`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `ami-0735c191cf914754d`
      - Workflow:
    * `_aws_instance_image.ami-0a0d8589b597d65b3`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `ami-0a0d8589b597d65b3`
      - Workflow:
    * `_rhel.9,x86,us-west-2`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `ami-0dda7e535b65b6469`
      - Workflow:
    * `_ubuntu.2204,arm64,us-west-2`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `ami-079f51a7bcca65b92`
      - Workflow:
    * `_ubuntu.2204,x86,us-west-2`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `ami-0735c191cf914754d`
      - Workflow:

    </details>


  * Group "**aws-instance-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_a1.2xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `a1.2xlarge`
      - Workflow:
    * `_a1.metal`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `a1.metal`
      - Workflow:
    * `_a1.xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `a1.xlarge`
      - Workflow:
    * `_aws_instance_type.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `#`
      - Workflow:
    * `_c5.12xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `c5.12xlarge`
      - Workflow:
    * `_c5.4xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `c5.4xlarge`
      - Workflow:
    * `_c5d.9xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `c5d.9xlarge`
      - Workflow:
    * `_g4dn.xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `g4dn.xlarge`
      - Workflow:
    * `_inf1.2xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `inf1.2xlarge`
      - Workflow:
    * `_inf1.xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `inf1.xlarge`
      - Workflow:
    * `_inf2.8xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `inf2.8xlarge`
      - Workflow:
    * `_inf2.xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `inf2.xlarge`
      - Workflow:
    * `_m7g.2xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `m7g.2xlarge`
      - Workflow:
    * `_m7g.xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `m7g.xlarge`
      - Workflow:
    * `_t2.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.#`
      - Workflow:
    * `_t2.2xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.2xlarge`
      - Workflow:
    * `_t2.large`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.large`
      - Workflow:
    * `_t2.medium`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.medium`
      - Workflow:
    * `_t2.micro`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.micro`
      - Workflow:
    * `_t2.nano`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.nano`
      - Workflow:
    * `_t2.small`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.small`
      - Workflow:
    * `_t2.xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.xlarge`
      - Workflow:

    </details>


  * Group "**cloud-provider**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_aws`** (default)
      - Environment variables:
        - *CM_TERRAFORM_CONFIG_DIR_NAME*: `aws`
      - Workflow:
    * `_gcp`
      - Environment variables:
        - *CM_TERRAFORM_CONFIG_DIR_NAME*: `gcp`
      - Workflow:

    </details>


  * Group "**gcp-instance-image**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_debian-cloud/debian-11`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `debian-cloud/debian-11`
      - Workflow:
    * `_gcp_instance_image.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `#`
      - Workflow:
    * `_ubuntu-2204-jammy-v20230114`
      - Environment variables:
        - *TF_VAR_INSTANCE_IMAGE*: `ubuntu-2204-jammy-v20230114`
      - Workflow:

    </details>


  * Group "**gcp-instance-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_f1-micro`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `f1-micro`
      - Workflow:
    * `_gcp_instance_type.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `#`
      - Workflow:
    * `_n1-highmem.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `n1-highmem-#`
      - Workflow:
    * `_n1-standard.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `n1-highmem-#`
      - Workflow:

    </details>


  * Group "**gcp-project**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_gcp_project.#`
      - Environment variables:
        - *TF_VAR_GCP_PROJECT*: `#`
      - Workflow:

    </details>


  * Group "**instance-name**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_instance_name.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_NAME*: `#`
      - Workflow:

    </details>


  * Group "**platform**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_arm64`
      - Environment variables:
        - *CM_INSTANCE_PLATFORM*: `arm64`
      - Workflow:
    * **`_x86`** (default)
      - Environment variables:
        - *CM_INSTANCE_PLATFORM*: `x86`
      - Workflow:

    </details>


  * Group "**region**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_region.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_REGION*: `#`
      - Workflow:
    * `_us-west-2`
      - Environment variables:
        - *TF_VAR_INSTANCE_REGION*: `us-west-2`
      - Workflow:

    </details>


  * Group "**storage-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_storage_size.#`
      - Environment variables:
        - *TF_VAR_DISK_GBS*: `#`
      - Workflow:
    * `_storage_size.8`
      - Environment variables:
        - *TF_VAR_DISK_GBS*: `8`
      - Workflow:

    </details>


  * Group "**zone**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_zone.#`
      - Environment variables:
        - *TF_VAR_INSTANCE_ZONE*: `#`
      - Workflow:

    </details>


#### Default variations

`_aws,_x86`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--cminit=value`  &rarr;  `CM_TERRAFORM_CM_INIT=value`
* `--destroy=value`  &rarr;  `CM_DESTROY_TERRAFORM=value`
* `--gcp_credentials_json_file=value`  &rarr;  `CM_GCP_CREDENTIALS_JSON_PATH=value`
* `--key_file=value`  &rarr;  `CM_SSH_KEY_FILE=value`
* `--run_cmds=value`  &rarr;  `CM_TERRAFORM_RUN_COMMANDS=value`
* `--ssh_key_file=value`  &rarr;  `CM_SSH_KEY_FILE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "cminit":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* TF_VAR_SECURITY_GROUP_ID: `sg-0783752c97d2e011d`
* TF_VAR_CPU_COUNT: `1`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)***
     * get,terraform
       - CM script: [get-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)***
     * destroy,terraform
       * `if (CM_DESTROY_TERRAFORM  == on)`
       * CM names: `--adr.['destroy-cmd']...`
       - CM script: [destroy-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform)
</details>

___
### Script output
`cmr "run terraform[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_TERRAFORM_CONFIG_DIR`
* `CM_TERRAFORM_RUN_DIR`
#### New environment keys auto-detected from customize

* `CM_TERRAFORM_CONFIG_DIR`
* `CM_TERRAFORM_RUN_DIR`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)