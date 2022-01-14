#/usr/bin/python3
__author__ = "w2k8"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "w2k8"

import requests
import optparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main(url, token, githost):
    r = requests.get('{}-/readiness?token={}'.format(url, token), verify=False)
    readness = r.json()

    r = requests.get('{}-/liveness?token={}'.format(url, token), verify=False)
    liveness = r.json()

    user_session_logins_total = 0
    gitlab_auth_user_unauthenticated_total = 0
    gitlab_auth_user_password_invalid_total = 0
    gitlab_auth_user_authenticated_total = 0
    gitlab_auth_user_session_destroyed_total = 0

    r = requests.get('{}-/metrics?token={}'.format(url, token), verify=False)
    for line in r.text.split('\n'):
        if line.startswith('user_session_logins_total'):
            user_session_logins_total = line.split()[1]
        if line.startswith('gitlab_auth_user_unauthenticated_total'):
            gitlab_auth_user_unauthenticated_total = line.split()[1]
        if line.startswith('gitlab_auth_user_password_invalid_total'):
            gitlab_auth_user_password_invalid_total = line.split()[1]
        if line.startswith('gitlab_auth_user_authenticated_total'):
            gitlab_auth_user_authenticated_total = line.split()[1]
        if line.startswith('gitlab_auth_user_session_destroyed_total'):
            gitlab_auth_user_session_destroyed_total = line.split()[1]

    print('readness_status={0}|readness_status={0}'.format(githost, readness['status']))
    print('readness_master_check={0}|readness_master_check={0}'.format(githost, readness['master_check'][0]['status']))
    print('liveness_status={0}|liveness_status={0}'.format(githost, liveness['status']))
    print('user_session_logins_total={0}|user_session_logins_total={0}'.format(user_session_logins_total))
    print('gitlab_auth_user_unauthenticated_total={0}|gitlab_auth_user_unauthenticated_total={0}'.format(gitlab_auth_user_unauthenticated_total))
    print('gitlab_auth_user_password_invalid_total={0}|gitlab_auth_user_password_invalid_total={0}'.format(gitlab_auth_user_password_invalid_total))
    print('gitlab_auth_user_authenticated_total={0}|gitlab_auth_user_authenticated_total={0}'.format(gitlab_auth_user_authenticated_total))
    print('gitlab_auth_user_session_destroyed_total={0}|gitlab_auth_user_session_destroyed_total={0}'.format(gitlab_auth_user_session_destroyed_total))


if __name__=='__main__':
    parser = optparse.OptionParser()

    parser.add_option('-t', '--token',
                action="store", dest="token",
                help="Gitlab token to access the gitlap api/ Example: qwertyuiop1234567890",
                default="qwertyuiop1234567890")
    parser.add_option('-u', '--url',
                action="store", dest="url",
                help="The gitlab url. Example: https://localhost/",
                default="https://localhost/")
    options, args = parser.parse_args()
    main(options.url, options.token, options.githost)
