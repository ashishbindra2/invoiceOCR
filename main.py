import os
# cwd = os.getcwd()
# os.system('cmd /c "cd {}/"'.format(cwd))
# os.system('cmd /c "conda activate invoice_env"')

import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=5100, reload=True)
# 192.168.1.3