Simple application which displays useful information like memory usage per process,
CPU percentage etc using python and a micro framework called flask.


I had to do the following:
[http://www.upubuntu.com/2011/09/check-how-much-ram-programs-are-using.html]
* wget http://www.pixelbeat.org/scripts/ps_mem.py
* mv ps_mem.py /usr/local/sbin/
* chmod 755 /usr/local/sbin/ps_mem.py # Could not get this working though, I have to type my root password in the terminal when starting run.py

[http://www.leonardoborda.com/blog/how-to-configure-sysstatsar-on-ubuntudebian/]
* Step 1. Install sysstat
sudo apt-get install sysstat

* Step 2. Enable stat collection 
sudo vi /etc/default/sysstat
change ENABLED=”false” to ENABLED=”true”
save the file

* Step 3. Change the collection interval from every 10 minutes to every 2 minutes.
sudo vi /etc/cron.d/sysstat
Change
5-55/10 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1
To
*/2 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1
save the file

* Step 4. Restart sysstat
sudo service sysstat restart

* Step 5. If you want to see all statistics you can type:
sar -A

* Step 6. If you want to save the statistics for further analysis to a file use:
sudo sar -A > $(date +`hostname`-%d-%m-%y-%H%M.log)