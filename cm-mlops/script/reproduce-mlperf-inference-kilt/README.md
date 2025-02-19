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

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt[,variations] [--input_flags]`

2. `cmr "reproduce mlcommons mlperf inference harness kilt-harness kilt[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt'
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

```cmr "cm gui" --script="reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "reproduce mlcommons mlperf inference harness kilt-harness kilt[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert_`
      - Environment variables:
        - *CM_BENCHMARK*: `STANDALONE_BERT`
        - *kilt_model_name*: `bert`
        - *kilt_model_seq_length*: `384`
        - *kilt_model_batch_size*: `384`
        - *kilt_model_bert_variant*: `BERT_PACKED`
        - *kilt_input_format*: `INT64,1,384:INT64,1,8:INT64,1,384:INT64,1,384`
        - *kilt_output_format*: `FLOAT32,1,384:FLOAT32,1,384`
        - *dataset_squad_tokenized_max_seq_length*: `384`
        - *loadgen_buffer_size*: `10833`
        - *loadgen_dataset_size*: `10833`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_transformers
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_safetensors
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_activation-count.#`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `#`
        - *CM_MLPERF_QAIC_ACTIVATION_COUNT*: `#`
      - Workflow:
    * `_bert-99,qaic`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * compile,qaic,model,_bert-99
             * CM names: `--adr.['qaic-model-compiler', 'bert-99-compiler']...`
             - CM script: [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic)
    * `_bert_,network-client`
      - Environment variables:
        - *CM_BENCHMARK*: `NETWORK_BERT_CLIENT`
      - Workflow:
    * `_bert_,network-server`
      - Environment variables:
        - *CM_BENCHMARK*: `NETWORK_BERT_SERVER`
      - Workflow:
    * `_bert_,singlestream`
      - Environment variables:
        - *kilt_model_batch_size*: `1`
      - Workflow:
    * `_bs.#`
      - Environment variables:
        - *kilt_model_batch_size*: `#`
      - Workflow:
    * `_dl2q.24xlarge,resnet50,offline`
      - Workflow:
    * `_dl2q.24xlarge,singlestream`
      - Environment variables:
        - *kilt_device_ids*: `0`
      - Workflow:
    * `_resnet50,qaic`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * compile,qaic,model,_resnet50
             * CM names: `--adr.['qaic-model-compiler', 'resnet50-compiler']...`
             - CM script: [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic)
    * `_resnet50,uint8`
      - Environment variables:
        - *kilt_input_format*: `UINT8,-1,224,224,3`
        - *kilt_device_qaic_skip_stage*: `convert`
        - *CM_IMAGENET_ACCURACY_DTYPE*: `int8`
      - Workflow:

    </details>


  * Group "**batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `#`
        - *CM_MLPERF_QAIC_BATCH_SIZE*: `#`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
        - *kilt_backend_type*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
        - *kilt_backend_type*: `gpu`
      - Workflow:
    * `_qaic`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `qaic`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `QAic`
        - *kilt_backend_type*: `qaic`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,qaic,apps-sdk
             - CM script: [get-qaic-apps-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-apps-sdk)
           * get,lib,protobuf,_tag.v3.11.4
             - CM script: [get-lib-protobuf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-protobuf)

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_glow`
      - Environment variables:
        - *device*: `qaic`
        - *CM_MLPERF_BACKEND*: `glow`
        - *CM_MLPERF_BACKEND_LIB_NAMESPEC*: `QAic`
      - Workflow:
    * **`_onnxruntime`** (default)
      - Environment variables:
        - *device*: `onnxrt`
        - *CM_MLPERF_BACKEND*: `onnxruntime`
        - *CM_MLPERF_BACKEND_LIB_NAMESPEC*: `onnxruntime`
      - Workflow:
    * `_tensorrt`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tensorrt`
        - *device*: `tensorrt`
        - *CM_MLPERF_BACKEND_NAME*: `TensorRT`
      - Workflow:

    </details>


  * Group "**loadgen-scenario**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_multistream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `MultiStream`
      - Workflow:
    * `_offline`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Offline`
      - Workflow:
    * `_server`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Server`
      - Workflow:
    * `_singlestream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `SingleStream`
        - *kilt_model_batch_size*: `1`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert-99`
      - Environment variables:
        - *CM_MODEL*: `bert-99`
        - *CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
      - Workflow:
    * `_bert-99.9`
      - Environment variables:
        - *CM_MODEL*: `bert-99.9`
        - *CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3733910/files/model.onnx`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
        - *kilt_model_name*: `resnet50`
        - *kilt_input_count*: `1`
        - *kilt_output_count*: `1`
        - *kilt_input_format*: `FLOAT32,-1,224,224,3`
        - *kilt_output_format*: `INT64,-1`
        - *dataset_imagenet_preprocessed_input_square_side*: `224`
        - *ml_model_has_background_class*: `YES`
        - *ml_model_image_height*: `224`
        - *loadgen_buffer_size*: `1024`
        - *loadgen_dataset_size*: `50000`
        - *CM_BENCHMARK*: `STANDALONE_CLASSIFICATION`
      - Workflow:
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/6617981/files/resnext50_32x4d_fpn.pth`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_Pillow
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**nsp**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_nsp.14`** (default)
      - Workflow:

    </details>


  * Group "**power-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_maxn`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_MAXN*: `True`
      - Workflow:
    * `_maxq`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_MAXQ*: `True`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fp32`
      - Environment variables:
        - *CM_IMAGENET_ACCURACY_DTYPE*: `float32`
      - Workflow:
    * `_uint8`
      - Workflow:

    </details>


  * Group "**run-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_network-client`
      - Environment variables:
        - *CM_RUN_MODE*: `network-client`
      - Workflow:
    * `_network-server`
      - Environment variables:
        - *CM_RUN_MODE*: `network-server`
      - Workflow:
    * **`_standalone`** (default)
      - Environment variables:
        - *CM_RUN_MODE*: `standalone`
      - Workflow:

    </details>


  * Group "**sut**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_dl2q.24xlarge`
      - Environment variables:
        - *kilt_device_ids*: `0,1,2,3,4,5,6,7`
        - *qaic_queue_length*: `6`
      - Workflow:

    </details>


#### Default variations

`_cpu,_nsp.14,_onnxruntime,_resnet50,_standalone`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--devices=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DEVICES=value`
* `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
* `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--skip_preprocess=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--skip_preprocessing=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "count":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_BATCH_COUNT: `1`
* CM_BATCH_SIZE: `1`
* CM_FAST_COMPILATION: `yes`
* CM_MLPERF_LOADGEN_SCENARIO: `Offline`
* CM_MLPERF_LOADGEN_MODE: `performance`
* CM_SKIP_PREPROCESS_DATASET: `no`
* CM_SKIP_MODEL_DOWNLOAD: `no`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `kilt`
* CM_MLPERF_SKIP_RUN: `no`
* CM_KILT_REPO_URL: `https://github.com/krai/kilt-mlperf`
* kilt_device_ids: `0`
* kilt_max_wait_abs: `10000`
* verbosity: `1`
* loadgen_trigger_cold_run: `0`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,git,repo
       * CM names: `--adr.['kilt-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
     * get,generic-python-lib,_mlperf_logging
       * CM names: `--adr.['mlperf-logging']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,dataset,imagenet,preprocessed,_for.resnet50,_NHWC,_full
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['imagenet-preprocessed', 'dataset-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,ml-model,resnet50,_fp32,_onnx,_from-tf
       * `if (CM_MODEL  == resnet50) AND (CM_MLPERF_DEVICE  != qaic)`
       * CM names: `--adr.['resnet50-model', 'ml-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,bert-large,_packed,_pytorch
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['bert-model']...`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,squad-vocab
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['bert-vocab']...`
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
     * get,dataset,tokenized,squad
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['squad-tokenized']...`
       - CM script: [get-preprocessed-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad)
     * get,dataset,original,openimages,_validation,_full,_custom-annotations
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-original']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,dataset,original,openimages,_calibration
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-calibration']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,mlcommons,inference,loadgen
       * CM names: `--adr.['inference-loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * generate,user-conf,mlperf,inference
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
     * get,lib,onnxruntime,lang-cpp,_cpu
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == cpu)`
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
     * get,lib,onnxruntime,lang-cpp,_cuda
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/_cm.yaml)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/_cm.yaml)***
     * compile,cpp-program
       * `if (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['compile-program']...`
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
     * benchmark-mlperf
       * `if (CM_MLPERF_SKIP_RUN not in ['yes', True])`
       * CM names: `--adr.['runner', 'mlperf-runner']...`
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
</details>

___
### Script output
`cmr "reproduce mlcommons mlperf inference harness kilt-harness kilt[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
* `CM_HW_NAME`
* `CM_IMAGENET_ACCURACY_DTYPE`
* `CM_MAX_EXAMPLES`
* `CM_MLPERF_*`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_DATASET_LIST`
* `CM_MLPERF_CONF`
* `CM_MLPERF_DEVICE`
* `CM_MLPERF_USER_CONF`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)