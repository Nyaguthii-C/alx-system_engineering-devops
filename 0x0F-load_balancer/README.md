
# Project: 0x0F. Load balancer
**DevOps**, **SysAdmin**

## Tasks
- **0-custom_http_response_header** - configure web-02 to be identical to web-01 and configure Nginx so that its HTTP response contains a custom header *X-Served-By*
- **1-install_load_balancer** - Install and configure HAproxy on lb-01 server and configure HAproxy so that it send traffic to web-01 and web-02 distributing requests using a roundrobin algorithm
- **2-puppet_custom_http_response_header.pp** - automate the task of creating a custom HTTP header response with puppet
