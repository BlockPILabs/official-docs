This page contains steps and technical advice to help you set up the Hypernode
## Hypernode hardware requirement

The following are the minimum configuration requirements for running nodes
	64-bit Linux distribution
	CPU with 6 cores
	16GB RAM
	Connection to Internet
	Public IP
	2TB*2 SSD


## Hypernode installation
### Install dependencies
Use YUM command（For OS such as CentOS、Fedora、Red Hat Enterprise Linux）
```
yum update
yum groupinstall "Development Tools"
apt-get install vim wget build-essential pkg-config unzip git jq
```

Use APT command（For OS Such as Ubuntu、Debian）
```
apt-get update
apt-get install vim wget build-essential pkg-config unzip git jq
```

### Install GO
If GO is already installed in your system and the version is above 1.7, skip this operation.
Otherwise, install the latest one.
```
# Clear old versions if necessary
# rm -rf /usr/local/go

# Install
name=go1.18.1.linux-amd64.tar.gz
wget https://dl.google.com/go/$name
tar -C /usr/local -xzf $name
rm -f $name
cat << EOF >> ~/.profile
# go
export GOPATH=/root/go
export PATH=/usr/local/go/bin:/root/go/bin:$PATH
EOF
source ~/.profile
```


### Install BlockPi HyperNode
```
git clone
cd
```


### Initialization
Initialization will create a Public Key in the directory where the current system resides, 
which is used for statistics encryption
It will generate a directory named 'keystore' and a private key in this directory. 
Then the address is generated and exported.

```
./HyperNode init
# Input and setup a passcode for for this private key
```

Configure config.yml
The configurations below need to be set up for individuals. Others stay default.

```
# Chain configurations are for the target blockchain network
chain:
  name: "klaytn"
  network: "8217"

# Node configuration is where to set up the back-end of the target blockchain network 
#(for both rpc and archive node)
Node:
  addr: "http://127.0.0.1:31271"

# beacon. Connect to the nearest beacon node to get the gateways list information and improve HyperNode performance. 
#连接最近的beacon 节点，可以分配最近的网关，提高自身网络请求到达率
beacon:
  [ "141.95.205.50:9090" ]
```



## Run HyperNode
### Run HyperNode directly
`./HyperNode --keystore_path keystore/key --password_path passwd.txt`

### Run HyperNode from systemd file
systemd file demo

`vim /etc/systemd/system/HyperNode.service`

```
[Unit]
Description=daemon
After=network-online.target

[Service]
User=root
WorkingDirectory=/root/HyperNode
ExecStart=/root/HyperNode/HyperNode --keystore_path keystore/key --password_path passwd.txt
LimitNOFILE=65536
StandardOutput=null
StandardError=null

[Install]
WantedBy=multi-user.target
```

Set the server to run HyperNode at startup 

`systemctl enable HyperNode`

And start the program

`systemctl start HyperNode`


## 验证执行

