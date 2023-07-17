
# Project: 0x13. Firewall
- **DevOps**, **SysAdmin**, **Security**  
### Resources
[Basic UFW (Uncomplicated Firewall) commands](https://serverspace.io/support/help/osnovnye-komandy-ufw/)  
## Tasks
- 0-block_all_incoming_traffic_but - install the ufw firewall and setup a few rules on web-01
- 100-port_forwarding - Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP  
**Hint**  
To add the `sudo ufw route allow proto tcp from any to any port 8080 redirect to 127.0.0.1 port 80` rule in UFW and have it persist across reboots or service restarts, you can add it to the `/etc/ufw/before.rules` file. Follow these steps:

1. Open the `/etc/ufw/before.rules` file in a text editor with root privileges:
   ```
   sudo nano /etc/ufw/before.rules
   ```

2. Locate the section in the file where the `*filter` rule is defined. It usually appears near the top.

3. Add the following rule just before the `*filter` line:
   ```
   *nat
   :PREROUTING ACCEPT [0:0]
   -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
   COMMIT
   ```

   This rule sets up NAT (Network Address Translation) to redirect incoming TCP traffic on port 8080 to port 80.

4. Save the changes and exit the text editor.

After adding the rule to the `before.rules` file, you can enable UFW to apply the new rule by running:
```
sudo ufw disable
sudo ufw enable
```

Now, the UFW rule for port forwarding from 8080 to 80 will be loaded each time UFW starts, ensuring the rule persists across reboots and service restarts.
