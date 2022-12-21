import os
import tempfile
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
from office365.runtime.auth.user_credential import UserCredential

client_id = "0000"
client_secret = "0000"
site_url = "https://hyperlounge.sharepoint.com/"
#file_url = "/sites/dev/Shared Documents/General/test/맘스터치권한세팅.xlsx"
file_url = "/sites/dev/Shared Documents/General/팀 회의 자료/PF_플랫폼팀/20220809_임시영문화_BE_관련_한글문구.xlsx"

ctx = ClientContext(site_url).with_credentials(UserCredential(client_id, client_secret) )

download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))

with open(download_path, "wb") as local_file:
    file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
    #file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()

print("[Ok] file has been downloaded into: {0}".format(download_path))