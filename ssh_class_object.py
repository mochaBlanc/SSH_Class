import paramiko
class Ssh_Class(object):
    ip=''
    port=22
    username=''
    timeout=0
    ssh=None

    def __init__(self,ip,username,port=22,timeout=30):
        self.ip=ip
        self.username=username
        self.port=port
        self.timeout=timeout
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh=ssh

    def connect_by_pwd(self,pwd):
        self.ssh.connect(hostname=self.ip,port=self.port,username=self.username,password=pwd)
        if self.ssh:
            print("connect by password successfully.")
        else:
            self.close()
            raise Exception("ERROR:connect by password.")
    
    def exec_command(self,command):
        if command:
            stdin,stdout,stderr=self.ssh.exec_command(command)
            result=stdout.read().decode('gbk')
            return result
        else:
            self.close()
            raise Exception("invalid command.")

    def download_file(self,remote_file_path:str,local_save_path):
        sftp: SFTPClient=self.ssh.open_sftp()
        try:
            sftp.get(remotepath=remote_file_path,localpath=local_save_path)
            print(f"file:{remote_file_path} download success!")
        except Exception as e:
            print(f"download file failed,please check whether the file path is correct!\nerror massage：{e} ")

    def upload_file(self,local_file_path:str,remote_save_path):
        sftp: SFTPClient=self.ssh.open_sftp()
        try:
            sftp.put(localpath=local_file_path,remotepath=remote_save_path)
            print(f"file:{local_file_path} upload success!")
        except Exception as e:
            print(f"upload file failed,please check whether the file path is correct!\nerror massage：{e} ")

    
    def connect_close(self):
        if self.ssh:
            self.ssh.close()
        else:
            raise Exception("ERROR:connect_close.")

if __name__=='__main__':
    mac_local_ssh_file_holder="/Users/yue/Downloads/code_mac/ssh_file_test/test_0.rar"
    win_remote_pull_file="C:/Users/helloWord/Desktop/etl_trace.rar"
    SSH=Ssh_Class("192.xxx.xx.x","xxxx@xx.com",port=22)
    SSH.connect_by_pwd("xxxxxxxx")
    print(SSH.exec_command("ipconfig"))
    SSH.download_file(win_remote_pull_file,mac_local_ssh_file_holder)
    SSH.connect_close()

            





