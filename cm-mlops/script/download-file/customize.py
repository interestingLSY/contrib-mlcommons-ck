from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_DOWNLOAD_LOCAL_FILE_PATH') and os.path.exists(env['CM_DOWNLOAD_LOCAL_FILE_PATH']):
        filepath = env['CM_DOWNLOAD_LOCAL_FILE_PATH']
        env['CM_DOWNLOAD_CMD'] = ""

    else:
        url = env.get('CM_DOWNLOAD_URL','')

        if url=='':
            return {'return':1, 'error': 'please specify URL using --url={URL} or --env.CM_DOWNLOAD_URL={URL}'}

        if '&' in url and env.get('CM_DOWNLOAD_TOOL','') != "cmutil":
            if os_info['platform'] == 'windows':
                url = '"'+url+'"'
            else:
                url = url.replace('&','\&')

        extra_download_options = env.get('CM_DOWNLOAD_EXTRA_OPTIONS', '')

        verify_ssl = env.get('CM_VERIFY_SSL', "True")
        if verify_ssl.lower() in [ "no", "false" ]:
            verify_ssl = False
            extra_download_options += " --no-check-certificate"
        else:
            verify_ssl = True

        if env.get('CM_DOWNLOAD_PATH', '') != '':
            download_path = env['CM_DOWNLOAD_PATH']
            if not os.path.exists(download_path):
                os.makedirs(download_path, exist_ok = True)
            os.chdir(download_path)

        if env.get('CM_DOWNLOAD_FILENAME', '') == '':
            urltail = os.path.basename(env['CM_DOWNLOAD_URL'])
            urlhead = os.path.dirname(env['CM_DOWNLOAD_URL'])
            if "." in urltail and "/" in urlhead:
                # Check if ? after filename
                j = urltail.find('?')
                if j>0:
                    urltail=urltail[:j]
                env['CM_DOWNLOAD_FILENAME'] = urltail
            else:
                env['CM_DOWNLOAD_FILENAME'] = "index.html"

        if env['CM_DOWNLOAD_TOOL'] == "cmutil":
            print ('')

            cm = automation.cmind
            r = cm.access({'action':'download_file',
                           'automation':'utils,dc2743f8450541e3',
                           'url':url,
                           'verify': verify_ssl})
            if r['return']>0: return r
            env['CM_DOWNLOAD_CMD'] = ""
            env['CM_DOWNLOAD_FILENAME'] = r['filename']

        elif env['CM_DOWNLOAD_TOOL'] == "wget":
            if env.get('CM_DOWNLOAD_FILENAME', '') != '':
                extra_download_options +=' -O '+env['CM_DOWNLOAD_FILENAME']+' '
            env['CM_DOWNLOAD_CMD'] = f"wget -nc {extra_download_options} {url}"

        elif env['CM_DOWNLOAD_TOOL'] == "curl":
            env['CM_DOWNLOAD_CMD'] = f"curl {extra_download_options} {url}"

        elif env['CM_DOWNLOAD_TOOL'] == "gdown":
            env['CM_DOWNLOAD_CMD'] = f"gdown {extra_download_options} {url}"

        filename = env['CM_DOWNLOAD_FILENAME']
        env['CM_DOWNLOAD_DOWNLOADED_FILENAME'] = filename

        filename = os.path.basename(env['CM_DOWNLOAD_FILENAME'])
        filepath = os.path.join(os.getcwd(), filename)

    env['CM_DOWNLOAD_DOWNLOADED_PATH'] = filepath

    #verify checksum if file already present
    if env.get('CM_DOWNLOAD_CHECKSUM', '') != '':
        x='*' if os_info['platform'] == 'windows' else ''
        env['CM_DOWNLOAD_CHECKSUM_CMD'] = "echo {} {}{} | md5sum -c".format(env.get('CM_DOWNLOAD_CHECKSUM'), x, env['CM_DOWNLOAD_FILENAME'])
    else:
        env['CM_DOWNLOAD_CHECKSUM_CMD'] = ""

    if os_info['platform'] == 'windows':
        # Check that if empty CMD, should add ""
        for x in ['CM_DOWNLOAD_CMD', 'CM_DOWNLOAD_CHECKSUM_CMD']:
            env[x+'_USED']='YES' if env.get(x,'')!='' else 'NO'

    return {'return':0}

def postprocess(i):

    env = i['env']

    filepath = env['CM_DOWNLOAD_DOWNLOADED_PATH']

    if not os.path.exists(filepath):
        return {'return':1, 'error': 'Downloaded path {} does not exist. Probably CM_DOWNLOAD_FILENAME is not set and CM_DOWNLOAD_URL given is not pointing to a file'.format(filepath)}

    if env.get('CM_DOWNLOAD_RENAME_FILE', '') != '':
        file_dir = os.path.dirname(filepath)
        new_file_name = env['CM_DOWNLOAD_RENAME_FILE']
        new_file_path = os.path.join(file_dir, new_file_name)
        os.rename(filepath, new_file_path)
        filepath = new_file_path


    if env.get('CM_DOWNLOAD_FINAL_ENV_NAME','') != '':
        env[env['CM_DOWNLOAD_FINAL_ENV_NAME']] = filepath

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  filepath

    return {'return':0}
